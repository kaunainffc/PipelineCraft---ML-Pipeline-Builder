import sys
import os
import streamlit as st
from components.sidebar import step_sidebar
from components.visualization import show_pipeline_graph
from components.results import run_pipeline_and_display_results
from components.export_code import show_exported_code
from utils.pipeline_builder import get_pipeline
from utils.data_handler import load_data

st.set_page_config("PipelineCraft", layout="wide")
st.title("🛠️ PipelineCraft - ML Pipeline Builder")

# Sidebar
uploaded_file = step_sidebar()

# Main
data = load_data(uploaded_file)
st.subheader("📊 Data Preview")
st.write(data.head())

# Visualization
show_pipeline_graph()

# Run Pipeline
run_pipeline_and_display_results(data)

# Code Export
show_exported_code()
