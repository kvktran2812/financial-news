import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create a Dash app
app = dash.Dash(__name__)

# Layout with Tabs
app.layout = html.Div(
    [
        dcc.Tabs(
            id="tabs-example",
            value="tab-1",
            children=[
                dcc.Tab(label="Tab 1", value="tab-1"),
                dcc.Tab(label="Tab 2", value="tab-2"),
                dcc.Tab(label="Tab 3", value="tab-3"),
            ],
        ),
        html.Div(id="tabs-content-example"),
    ]
)


# Callback to update content based on selected tab
@app.callback(
    Output("tabs-content-example", "children"), [Input("tabs-example", "value")]
)
def render_content(tab):
    if tab == "tab-1":
        return html.Div(
            [
                html.H3("Content for Tab 1"),
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": [1, 2, 3],
                                "y": [4, 1, 2],
                                "type": "bar",
                                "name": "Tab 1 Data",
                            },
                        ],
                        "layout": {"title": "Graph for Tab 1"},
                    }
                ),
            ]
        )
    elif tab == "tab-2":
        return html.Div(
            [
                html.H3("Content for Tab 2"),
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": [1, 2, 3],
                                "y": [2, 4, 5],
                                "type": "line",
                                "name": "Tab 2 Data",
                            },
                        ],
                        "layout": {"title": "Graph for Tab 2"},
                    }
                ),
            ]
        )
    elif tab == "tab-3":
        return html.Div(
            [
                html.H3("Content for Tab 3"),
                html.P(
                    "Here, you can display data, text, or even other interactive elements."
                ),
            ]
        )


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
