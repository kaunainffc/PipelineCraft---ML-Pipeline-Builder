from sklearn.pipeline import Pipeline
import streamlit as st

def get_pipeline():
    return Pipeline(st.session_state.pipeline_steps)
