import streamlit as st
import pandas as pd

st.title("Dashboard Utama")

df = pd.read_excel("Data.xlsx")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.metric(
            label="Total IXP",
            value=df["IXP"].sum()
        )

with col2:
    with st.container(border=True):
        st.metric(
            label="Total Data Center",
            value=df["Data Center"].sum()
        )

with col3:
    with st.container(border=True):
        st.metric(
            label="Total Landing Point",
            value=df["Landing Point"].sum()
        )

st.subheader("Sebaran IXP")
ixp_chart = df.set_index("Kota")[["IXP"]]
st.write(ixp_chart)

st.subheader("Sebaran Data Center")
dc_chart = df.set_index("Kota")[["Data Center"]]
st.write(dc_chart)

st.subheader("Sebaran Landing Point")
lp_chart = df.set_index("Kota")[["Landing Point"]]
st.write(lp_chart)

st.markdown(
    """
    <style>
        [data-testid="stMainBlockContainer"] {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)
