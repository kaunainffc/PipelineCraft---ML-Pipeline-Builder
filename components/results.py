import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from utils.pipeline_builder import get_pipeline

def run_pipeline_and_display_results(df):
    steps = st.session_state.get("pipeline_steps", [])
    if not steps:
        return

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    pipeline = get_pipeline()

    if st.button("🚀 Run Pipeline"):
        try:
            pipeline.fit(X_train, y_train)
            preds = pipeline.predict(X_test)

            acc = accuracy_score(y_test, preds)
            cm = confusion_matrix(y_test, preds)

            st.success(f"✅ Accuracy: {acc:.2f}")

            st.subheader("📉 Confusion Matrix")
            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error: {e}")
