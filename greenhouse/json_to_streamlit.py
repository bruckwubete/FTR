#%%
import pandas as pd
import json
#%%
from sklearn.datasets import load_iris
data = load_iris()
#%%
df = pd.DataFrame(data=data.data, columns=data.feature_names)
#%%
df.groupby('sepal length (cm)').sum()
#%%
# A profile has Posts and Posts have comments
from pydantic import BaseModel, ConfigDict

class Profile(BaseModel):
    model_config = ConfigDict(strict=True)
    name: str
class Post(BaseModel):
    model_config = ConfigDict(strict=True)
    id: int
    title: str
class Comment(BaseModel):
    model_config = ConfigDict(strict=True)
    id: int
    body: str
    post: Post

import requests
json_data = requests.get('https://my-json-server.typicode.com/typicode/demo/db').json()
profiles = []
try:
   profiles.append(Profile.model_validate(json_data.get('profile')))
except ValueError as e:
    print(f"ERROR: parsing profile {p} failed: {e}")

profiles
#%%
posts = []
for p in json_data.get('posts', []):
    try:
        posts.append(Post.model_validate(p))
    except ValueError as e:
        print(f"ERROR: parsing post {p} failed: {e}")
posts
#%%
comments = []
for c in json_data.get('comments', []):
    try:
        c['post'] = [p for p in posts if p.id == c['postId']][0]
        comments.append(Comment.model_validate(c))
    except ValueError as e:
        print(f"ERROR: parsing comment {p} failed: {e}")
    except Exception as e:
        print(f'ERROR: parsing due to {e}')
comments
#%%
import streamlit as st
import pandas as pd
df = pd.DataFrame([c.dict() for c in comments])
st.title("Example")
df
#%%
