from dash import dcc, html


def build_layout():
    return html.Div([
        html.H1("Survey of Consumer Finances"),

        html.H2("High Variance Features"),
        dcc.Graph(id="bar-chart"),
        dcc.RadioItems(
            options=[
                {"label": "Trimmed", "value": True},
                {"label": "Full", "value": False},
            ],
            value=True,
            id="trim-button",
        ),

        html.H2("K-means Clustering"),
        html.H3("Number of Clusters (k)"),
        dcc.Slider(min=2, max=12, step=1, value=2, id="k-slider"),

        html.Div(id="metrics"),
        dcc.Graph(id="pca-scatter"),
    ])