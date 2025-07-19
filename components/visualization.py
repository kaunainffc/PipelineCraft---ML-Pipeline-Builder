import streamlit as st
from graphviz import Digraph

def show_pipeline_graph():
    steps = st.session_state.get("pipeline_steps", [])
    if not steps:
        st.info("No pipeline steps added.")
        return

    dot = Digraph()
    for i, (name, _) in enumerate(steps):
        dot.node(str(i), name)
        if i > 0:
            dot.edge(str(i - 1), str(i))
    st.subheader("🧩 Pipeline Visualization")
    st.graphviz_chart(dot)
