import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.DataFrame({
    "name":["Nanita","Harman","simarjit","komal","Riya"],
    "roll no":[101,102,103,104,105],
    "class":[10,11,12,10,12],
    "obtained _marks":[90,80,70,60,50]
})
fig=px.sunburst(df,path=["class","name"],values="roll no",title="student by class and roll no")
st.plotly_chart(fig)