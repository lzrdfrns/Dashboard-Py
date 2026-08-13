import streamlit as st

st.set_page_config(
    page_title="Internet Dashboard",
    page_icon="🌐",
    layout="wide"
)

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

st.title("Internet Dashboard")
st.sidebar.success("Select Pages")