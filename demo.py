import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.DataFrame({
    "name":["Nanita","Harman","simarjit","komal","Riya"],
    "roll no":[101,102,103,104,105],
    "obtained _marks":[90,80,70,60,50]
})
fig = px.bar(df["name"],df["obtained _marks"],text=df["obtained _marks"])
st.plotly_chart(fig)

