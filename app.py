import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Smart Analytics Tool")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Missing Value Analysis")
    st.write(df.isnull().sum())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:

        col = st.selectbox(
            "Select Column",
            numeric_cols
        )

        st.subheader("Histogram")

        fig1 = px.histogram(df, x=col)
        st.plotly_chart(fig1)

        st.subheader("Box Plot")

        fig2 = px.box(df, y=col)
        st.plotly_chart(fig2)

        st.subheader("Scatter Plot")

        fig3 = px.scatter(df, x=col, y=col)
        st.plotly_chart(fig3)