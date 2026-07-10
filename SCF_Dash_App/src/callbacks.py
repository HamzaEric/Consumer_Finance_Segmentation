# src/callbacks.py
import plotly.express as px
from dash import Input, Output, html
from app import app
from src.engine import get_high_var_features, get_model_metrics, get_pca_labels

@app.callback(
    Output("bar-chart", "figure"),
    Input("trim-button", "value"),
)
def serve_bar_chart(trimmed):
    top_five = get_high_var_features(trimmed=trimmed)
    fig = px.bar(
        x=top_five.values,
        y=top_five.index,
        orientation="h",
        title="Top 5 High-Variance Features",
    )
    fig.update_layout(
        xaxis_title="Variance",
        yaxis_title="Feature",
        yaxis={"categoryorder": "total ascending"},
    )
    return fig

@app.callback(
    Output("metrics", "children"),
    Input("trim-button", "value"),
    Input("k-slider", "value"),
)
def serve_metrics(trimmed, k):
    metrics = get_model_metrics(trimmed, k, return_metrics=True)
    return [
        html.H3(f"Inertia: {metrics['inertia']:,}"),
        html.H3(f"Silhouette Score: {metrics['silhouette']}"),
    ]

@app.callback(
    Output("pca-scatter", "figure"),
    Input("trim-button", "value"),
    Input("k-slider", "value"),
)
def serve_scatter_plot(trimmed, k):
    fig = px.scatter(
        data_frame=get_pca_labels(trimmed=trimmed, k=k),
        x="PC1",
        y="PC2",
        color="labels",
        title=f"PCA Space Cluster Assignment (k={k})",
        category_orders={"labels": [str(i) for i in range(k)]},
    )
    fig.update_layout(
        xaxis_title="Principal Component 1",
        yaxis_title="Principal Component 2",
    )
    return fig