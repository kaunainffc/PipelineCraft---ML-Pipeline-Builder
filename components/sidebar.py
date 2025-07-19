import streamlit as st
from config.steps_config import AVAILABLE_STEPS

def step_sidebar():
    st.sidebar.header("Step Selection & Configuration")
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

    step_type = st.sidebar.selectbox("Step Type", list(AVAILABLE_STEPS.keys()))
    step_name = st.sidebar.selectbox("Step", list(AVAILABLE_STEPS[step_type].keys()))

    if "pipeline_steps" not in st.session_state:
        st.session_state.pipeline_steps = []

    if st.sidebar.button("Add Step"):
        step_class = AVAILABLE_STEPS[step_type][step_name]
        st.session_state.pipeline_steps.append((step_name.lower(), step_class()))

    return uploaded_file
