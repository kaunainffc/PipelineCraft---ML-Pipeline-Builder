import streamlit as st

def show_exported_code():
    steps = st.session_state.get("pipeline_steps", [])
    if not steps:
        return

    imports = []
    pipeline_code = []

    for name, comp in steps:
        cls = comp.__class__
        module = cls.__module__
        imports.append(f"from {module} import {cls.__name__}")
        pipeline_code.append(f"    ('{name}', {cls.__name__}())")

    full_code = (
        "\n".join(set(imports)) +
        "\nfrom sklearn.pipeline import Pipeline\n\n" +
        "pipeline = Pipeline([\n" + ",\n".join(pipeline_code) + "\n])"
    )

    st.subheader("📤 Exported Code")
    st.code(full_code, language="python")
    st.download_button("📥 Download Code", full_code, file_name="pipeline.py")
