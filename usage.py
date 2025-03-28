import dash
from dash import html, Input, Output, State, clientside_callback, _dash_renderer, dcc
import dash_flows
import dash_mantine_components as dmc
import json

_dash_renderer._set_react_version("18.2.0")

app = dash.Dash(__name__, assets_folder="assets", external_stylesheets=dmc.styles.ALL)

initial_nodes = [
    # First node stays the same
    {
        "id": "1",
        "type": "resizable",
        "data": {
            "label": html.Div(
                [
                    html.Img(
                        src="https://avatars.githubusercontent.com/u/120129682?v=4",
                        style={"width": "100%", "height": "100%"},
                    ),
                ],
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "gap": "10px",
                    "padding": "10px",
                },
            ),
            "handles": [
                {
                    "type": "target",
                    "position": "top",
                    "id": "handle1",
                    "style": {"background": "#555"},
                },
                {
                    "type": "source",
                    "position": "left",
                    "id": "handle2",
                    "style": {"background": "#555"},
                },
            ],
        },
        "position": {"x": 250, "y": 25},
        "style": {
            "width": 300,
            "height": 300,
        },
    },
    # Add a second node
    {
        "id": "2",
        "type": "resizable",
        "data": {
            "label": html.Div(
                [
                    html.Img(
                        src="https://avatars.discourse-cdn.com/v4/letter/h/50afbb/288.png",
                        style={"width": "100%", "height": "100%"},
                    ),
                ],
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "gap": "10px",
                    "padding": "10px",
                },
            ),
            "handles": [
                {
                    "type": "source",
                    "position": "right",
                    "id": "handle3",
                    "style": {"background": "#555"},
                },
                {
                    "type": "target",
                    "position": "bottom",
                    "id": "handle4",
                    "style": {"background": "#555"},
                },
            ],
        },
        "position": {"x": 250, "y": 150},
        "style": {
            "width": 300,
            "height": 300,
        },
    },
    # Add an animated node
    {
        "id": "animated1",
        "type": "circle",
        "data": {"label": "🔄"},
        "position": {"x": 250, "y": 150},
        "style": {
            "width": 60,
            "height": 60,
        },
    },
    # Third node stays the same
    {
        "id": "3",
        "type": "resizable",
        "data": {
            "label": html.Div(
                [html.Button(id="btn_example", children="button")],
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "gap": "10px",
                    "padding": "10px",
                },
            ),
            "handles": [
                {
                    "type": "source",
                    "position": "right",
                    "id": "handle5",
                    "style": {"background": "#555"},
                },
                {
                    "type": "target",
                    "position": "bottom",
                    "id": "handle6",
                    "style": {"background": "#555"},
                },
            ],
        },
        "position": {"x": 600, "y": 25},
        "style": {
            "width": 300,
            "height": 300,
        },
    },
]
initial_edges = [
    {
        "id": "e1-2",
        "source": "1",
        "sourceHandle": "handle2",
        "target": "2",
        "targetHandle": "handle4",
        "type": "animated",
        "data": {"animatedNode": "animated1"},  # Reference the dedicated animated node
        "style": {"strokeWidth": 2, "stroke": "#555"},
    },
    {
        "id": "e2-3",
        "source": "2",
        "sourceHandle": "handle3",
        "target": "3",
        "markerEnd": {
            "type": "arrowclosed",
            "color": "#555",
        },
        "targetHandle": "handle6",
        "type": "default",  # Changed to default type
        "style": {"strokeWidth": 2, "stroke": "#555"},
    },
]


# Add layout buttons above the DashFlow component
layout_buttons = dmc.Group(
    [
        dmc.Button("Vertical Layout", id="btn-vertical", variant="outline"),
        dmc.Button("Horizontal Layout", id="btn-horizontal", variant="outline"),
        dmc.Button("Radial Layout", id="btn-radial", variant="outline"),
        dmc.Button("Force Layout", id="btn-force", variant="outline"),
    ],
    mt="md",
    mb="md",
)

app.layout = dmc.MantineProvider(
    [
        layout_buttons,
        dash_flows.DashFlows(
            id="react-flow-example",
            nodes=initial_nodes,
            edges=initial_edges,
            showDevTools=True,
            style={"height": "600px"},
            layoutOptions=None,  # Add this prop
        ),
        # Hidden div for storing layout options
        html.Div(id="layout-options", style={"display": "none"}),
        # Store component to hold nodes data
        dcc.Store(id="nodes-store", data=initial_nodes),
        # Preformatted text to display nodes data as JSON
        html.Pre(id="nodes-json", style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"}),
    ]
)

@app.callback(
    Output("nodes-store", "data"),
    Input("react-flow-example", "nodes"),
    prevent_initial_call=True,
)
def update_nodes_store(nodes):
    return nodes


# Callback to update the nodes JSON display
@app.callback(
    Output("nodes-json", "children"),
    Input("nodes-store", "data")
)
def update_nodes_json(nodes_data):
    return json.dumps(nodes_data, indent=2)


# Create a clientside callback to handle layout changes
app.clientside_callback(
    """
    function(n_vertical, n_horizontal, n_radial, n_force) {
        const triggered = dash_clientside.callback_context.triggered[0];
        if (!triggered) return window.dash_clientside.no_update;

        const btnId = triggered.prop_id.split('.')[0];
        let options = {};

        switch(btnId) {
            case 'btn-vertical':
                options = {
                    'elk.algorithm': 'layered',
                    'elk.direction': 'DOWN',
                    'elk.spacing.nodeNode': 80,
                    'elk.layered.spacing.nodeNodeBetweenLayers': 100
                };
                break;
            case 'btn-horizontal':
                options = {
                    'elk.algorithm': 'layered',
                    'elk.direction': 'RIGHT',
                    'elk.spacing.nodeNode': 80,
                    'elk.layered.spacing.nodeNodeBetweenLayers': 100
                };
                break;
            case 'btn-radial':
                options = {
                    'elk.algorithm': 'org.eclipse.elk.radial',
                    'elk.radial.radius': 200
                };
                break;
            case 'btn-force':
                options = {
                    'elk.algorithm': 'org.eclipse.elk.force',
                    'elk.force.iterations': 300,
                    'elk.spacing.nodeNode': 80
                };
                break;
            default:
                return window.dash_clientside.no_update;
        }
        return JSON.stringify(options);
    }
    """,
    Output(
        "react-flow-example", "layoutOptions"
    ),  # Change output target to DashFlow's layoutOptions
    Input("btn-vertical", "n_clicks"),
    Input("btn-horizontal", "n_clicks"),
    Input("btn-radial", "n_clicks"),
    Input("btn-force", "n_clicks"),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run(debug=True, port=7777)