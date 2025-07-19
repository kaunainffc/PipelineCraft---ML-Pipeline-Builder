from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

AVAILABLE_STEPS = {
    "Preprocessing": {
        "StandardScaler": StandardScaler,
        "PCA": PCA
    },
    "Model": {
        "LogisticRegression": LogisticRegression,
        "RandomForestClassifier": RandomForestClassifier
    }
}
