import pandas as pd
from sklearn.datasets import load_iris

def load_data(uploaded_file):
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        iris = load_iris(as_frame=True)
        df = iris.frame
    return df
