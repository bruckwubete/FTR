import base64
from typing import Any, Dict, Iterator, List, Optional
from uuid import uuid4

import requests
from langchain_core.callbacks import (
    CallbackManagerForLLMRun,
)
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult


class BpaOpenAILLM(BaseChatModel):
    model_id: str
    base_address: str
    okta_domain: str
    okta_custom_scope: str
    client_secret: str
    client_id: str

    def _generate(
            self,
            messages: List[BaseMessage],
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> ChatResult:

        jwt_token = self._get_okta_token()
        user_id = self._get_user_id(jwt_token)

        conversation_identifier = str(uuid4())

        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "userId": str(user_id)
        }

        json_payload = {
            "conversationIdentifier": conversation_identifier,
            "choicesPerPrompt": 1,
            "maxTokens": 1500,
            "systemMessage": '',
            "message": {
                "content": '',
                "role": "user",
            },
            "nucleusSamplingFactor": 0,
            "presencePenalty": 0,
            "temperature": 0,
            "modelId": self.model_id
        }

        endpoint_url = f"{self.base_address}api/openai/createcompletion"

        for m in messages:
            if type(m) is SystemMessage:
                json_payload['systemMessage'] = m.content
            elif type(m) is HumanMessage:
                json_payload['message']['content'] = m.content
        generations = []
        response = requests.post(endpoint_url, headers=headers, json=json_payload)

        if response.status_code == 200:
            response_json = response.json()
            message = AIMessage(
                content=response_json["result"]["choices"][0]["message"]["content"],
                additional_kwargs={},
                response_metadata={
                    "time_in_seconds": response.elapsed.total_seconds(),
                },
            )
            generations.append(ChatGeneration(message=message))
        else:
            print(f'failure: {response.status_code}')
        return ChatResult(generations=generations)

    def _get_okta_token(self):
        token_endpoint = f"https://{self.okta_domain}/oauth2/default/v1/token"

        headers = {
            "Authorization": f"Basic {base64.b64encode(f'{self.client_id}:{self.client_secret}'.encode()).decode()}"
        }

        data = {
            "grant_type": "client_credentials",
            "scope": self.okta_custom_scope
        }

        response = requests.post(token_endpoint, headers=headers, data=data)

        if response.status_code == 200:
            response_json = response.json()
            return response_json["access_token"]
        else:
            raise Exception(f"Failed to retrieve token. Status code: {response.status_code}")

    def _get_user_id(self, jwt_token):
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        response = requests.get(f"{self.base_address}api/Auth/GetUserInfo", headers=headers)

        if response.status_code == 200:
            response_json = response.json()
            return response_json["result"]["id"]
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")

    def _stream(
            self,
            messages: List[BaseMessage],
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> Iterator[ChatGenerationChunk]:
        raise NotImplementedError(
            "The '_stream' method is not implemented for BpaOpenApiLLM"
        )

    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model."""
        return "echoing-chat-model-advanced"

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Return a dictionary of identifying parameters.

        This information is used by the LangChain callback system, which
        is used for tracing purposes make it possible to monitor LLMs.
        """
        return {
            # The model name allows users to specify custom token counting
            # rules in LLM monitoring applications (e.g., in LangSmith users
            # can provide per token pricing for their model and monitor
            # costs for the given LLM.)
            "model_id": self.model_id,
        }
