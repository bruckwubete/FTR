import base64
from typing import Any, AsyncIterator, Dict, Iterator, List, Optional
from uuid import uuid4

import requests
from langchain_core.callbacks import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)
from langchain_core.language_models import BaseChatModel, SimpleChatModel
from langchain_core.messages import AIMessageChunk, BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult
from langchain_core.runnables import run_in_executor


class CienaGPTChatModel(BaseChatModel):
    """A custom chat model that echoes the first `n` characters of the input.

    When contributing an implementation to LangChain, carefully document
    the model including the initialization parameters, include
    an example of how to initialize the model and include any relevant
    links to the underlying models documentation or API.

    Example:

        .. code-block:: python

            model = CustomChatModel(n=2)
            result = model.invoke([HumanMessage(content="hello")])
            result = model.batch([[HumanMessage(content="hello")],
                                 [HumanMessage(content="world")]])
    """
    """The name of the model"""
    model_name: str
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
        """Override the _generate method to implement the chat model logic.

        This can be a call to an API, a call to a local model, or any other
        implementation that generates a response to the input prompt.

        Args:
            messages: the prompt composed of a list of messages.
            stop: a list of strings on which the model should stop generating.
                  If generation stops due to a stop token, the stop token itself
                  SHOULD BE INCLUDED as part of the output. This is not enforced
                  across models right now, but it's a good practice to follow since
                  it makes it much easier to parse the output of the model
                  downstream and understand why generation stopped.
            run_manager: A run manager with callbacks for the LLM.
        """
        # Replace this with actual logic to generate a response from a list
        # # of messages.
        # last_message = messages[-1]
        # tokens = last_message.content[: self.n]
        # message = AIMessage(
        #     content=tokens,
        #     additional_kwargs={},  # Used to add additional payload (e.g., function calling request)
        #     response_metadata={  # Use for response metadata
        #         "time_in_seconds": 3,
        #     },
        # )
        ##

        # return ChatResult(generations=[generation])

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
            "temperature": 0.4,
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
            print(f'success: {response.status_code}')
            response_json = response.json()
            print(response_json)
            message = AIMessage(
                content=response_json["result"]["choices"][0]["message"]["content"],
                additional_kwargs={},  # Used to add additional payload (e.g., function calling request)
                response_metadata={  # Use for response metadata
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
        """Stream the output of the model.

        This method should be implemented if the model can generate output
        in a streaming fashion. If the model does not support streaming,
        do not implement it. In that case streaming requests will be automatically
        handled by the _generate method.

        Args:
            messages: the prompt composed of a list of messages.
            stop: a list of strings on which the model should stop generating.
                  If generation stops due to a stop token, the stop token itself
                  SHOULD BE INCLUDED as part of the output. This is not enforced
                  across models right now, but it's a good practice to follow since
                  it makes it much easier to parse the output of the model
                  downstream and understand why generation stopped.
            run_manager: A run manager with callbacks for the LLM.
        """
        last_message = messages[-1]
        tokens = last_message.content[: self.n]

        for token in tokens:
            chunk = ChatGenerationChunk(message=AIMessageChunk(content=token))

            if run_manager:
                # This is optional in newer versions of LangChain
                # The on_llm_new_token will be called automatically
                run_manager.on_llm_new_token(token, chunk=chunk)

            yield chunk

        # Let's add some other information (e.g., response metadata)
        chunk = ChatGenerationChunk(
            message=AIMessageChunk(content="", response_metadata={"time_in_sec": 3})
        )
        if run_manager:
            # This is optional in newer versions of LangChain
            # The on_llm_new_token will be called automatically
            run_manager.on_llm_new_token(token, chunk=chunk)
        yield chunk

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
            "model_name": self.model_name,
        }
