import streamlit as st
import pandas as pd
df = pd.DataFrame([c.dict() for c in comments])
st.title("Example")
df
