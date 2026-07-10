# src/engine.py
import pandas as pd
from scipy.stats.mstats import trimmed_var
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import config

# Run data wrangling once at startup to create a global dataframe
def wrangle(filepath):
    df = pd.read_csv(filepath)
    mask = (df["TURNFEAR"] == 1) & (df["NETWORTH"] < 2e6)
    return df[mask]

df = wrangle(config.DATA_PATH)

def get_high_var_features(trimmed=True, return_feat_names=False):
    if trimmed:
        top_five = df.apply(trimmed_var, limits=(0.1, 0.1)).sort_values().tail(5)
    else:
        top_five = df.var().sort_values().tail(5)

    if return_feat_names:
        return top_five.index.tolist()
    return top_five

def get_model_metrics(trimmed=True, k=2, return_metrics=False):
    features = get_high_var_features(trimmed=trimmed).index
    X = df[features]

    model = make_pipeline(StandardScaler(), KMeans(n_clusters=k, random_state=42))
    model.fit(X)

    if return_metrics:
        kmeans_step = model.named_steps["kmeans"]
        inertia = kmeans_step.inertia_
        ss = silhouette_score(X, kmeans_step.labels_)
        return {"inertia": round(inertia), "silhouette": round(ss, 3)}

    return model

def get_pca_labels(trimmed=True, k=2):
    features = get_high_var_features(trimmed=trimmed, return_feat_names=True)
    X = df[features]

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    X_pca_df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])

    model = get_model_metrics(trimmed=trimmed, k=k, return_metrics=False)
    X_pca_df["labels"] = model.named_steps["kmeans"].labels_.astype(str).astype(object)
    X_pca_df.sort_values(by="labels", inplace=True)

    return X_pca_df