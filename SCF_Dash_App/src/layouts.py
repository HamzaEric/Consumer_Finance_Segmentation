from dash import dcc, html

def get_floating_card_style(padding='20px', width='auto'):
    """
    Returns a CSS dictionary for a modern, floating card with a purple tech border.
    """
    return {
        'border': '2px solid #636EFA',
        'border-radius': '12px',
        'background-color': '#F8F9FA',
        'box-shadow': '0px 12px 30px rgba(0, 0, 0, 0.15)',
        'padding': padding,
        'width': width,
        'transition': 'box-shadow 0.3s ease-in-out'
    }


def build_layout():
    return html.Div([
        html.Div(
        style={
                'border': '2px solid #636EFA',
                'border-radius': '12px',
                'background-color': '#F8F9FA',
                'box-shadow': '0px 12px 30px rgba(0, 0, 0, 0.15)',
                'padding': '20px',
                'margin': '10px',
                 **get_floating_card_style(),

            },

        children=[
        html.H1("Survey of Consumer Finances",style={'color':'#636EFA'}),
        html.I("Designed & Engineered by Eric Maina" ,style={'color':'#636EFA'}),
        html.Br(),
        html.I("Data Scientist & Backend Developer" ,style={'color':'#636EFA'}),
        ]
        ),
        html.Div(
        style={
            'display': 'flex',
            'flex-direction': 'row',
            'justify-content': 'center',
            'gap': '10px',
            'padding':'10px 60px 10px 60px',


        },
        children=[
            # Image 1 (Left)
            html.Img(
                src='https://i.pinimg.com/1200x/94/b0/01/94b0016820b1d25222c3421dad597832.jpg',
                style={**get_floating_card_style(width='50%')  },# Takes up half the container
            ),

            # Image 2 (Right)
            html.Img(
                src='https://i.pinimg.com/1200x/4b/e2/43/4be243ae4aaff2fb76848787cdaeb88a.jpg',
                style={**get_floating_card_style(width='50%') },
            )
            ]
            ),

        html.Div(
            style={**get_floating_card_style(),'margin': '10px'},
        children=[
        html.H1("High Variance Features", style={'color': '#636EFA'}),
        dcc.Graph(id="bar-chart"),
        html.Div(
            style={**get_floating_card_style(), 'margin-top': '20px'},
            children=[
        dcc.RadioItems(
            options=[
                {"label": "Trimmed", "value": True},
                {"label": "Full", "value": False},
            ],
            value=True,
            id="trim-button",
        ),
        ]
        ),

        ],
        ),

        html.Div(
            style={**get_floating_card_style(),'margin': '10px'},
            children=[
        html.H1("K-means Clustering",style={'color':'#636EFA'}),
        html.Div(
            style={**get_floating_card_style(),'margin': '3px','margin-bottom':'10px'},
            children=[
        html.H3("Number of Clusters (k)", style={'color': '#636EFA'}),
        dcc.Slider(min=2, max=12, step=1, value=2, id="k-slider"),
        html.Div(id="metrics", style={'color': '#636EFA'}),
            ]
        ),

        dcc.Graph(id="pca-scatter"),
            ]
        ),
        html.Div(
            style={**get_floating_card_style(),'margin': '10px'},
            children=[
        html.A(
            "View Source Code on GitHub",
            href="https://github.com/HamzaEric/Consumer_Finance_Segmentation",
            target="_blank",
            style={
                'color': '#636EFA',
                'text-decoration': 'none',
                'font-weight': 'bold',
                'font-size': '14px',
                'transition': 'color 0.3s'
            },
        ),
            ],
        )
    ])