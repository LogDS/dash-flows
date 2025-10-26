import dataclasses
from typing import Optional
import dash_flows
import dacite
import dash
import yaml
import dash_mantine_components as dmc
from dash import html, Input, Output, dcc
from dash_extensions import WebSocket

@dataclasses.dataclass
class AppConfiguration:
    name:str
    port:int=7777
    host:str='127.0.0.1'
    debug:bool=True

    @staticmethod
    def from_yaml(filename) -> Optional['AppConfiguration']:
        with open(filename) as f:
            data = yaml.safe_load(f)
            return dacite.from_dict(data_class=AppConfiguration, data=data)
        return None

    def init(self, model):
        app = dash.Dash(self.name, assets_folder="assets", external_stylesheets=dmc.styles.ALL)
        with open("data/clientside_callback.js", "r") as f:
            call = f.read()
            # Create a clientside callback to handle layout changes
            app.clientside_callback(
                call,
                Output(
                    "layout-config", "data"
                ),  # Change output target to DashFlow's layoutOptions
                Input("btn-vertical", "n_clicks"),
                Input("btn-horizontal", "n_clicks"),
                Input("btn-radial", "n_clicks"),
                Input("btn-force", "n_clicks"),
                prevent_initial_call=True,
            )
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
                    id="View",
                    nodes=model.read_nodes_copy(),
                    edges=model.read_edges_copy(),
                    showDevTools=True,
                    style={"height": "600px"},
                    layoutOptions=None,  # Add this prop
                ),
                # Hidden div for storing layout options
                html.Div(id="layout-options", style={"display": "none"}),
                # Store component to hold nodes data
                dcc.Store(id="layout-config", data=model.read_layout()),
                # dcc.Store(id="edges-store", data=model.read_edges_copy()),
                # dcc.Store(id="post-processed-data", data={}),
                # Preformatted text to display nodes data as JSON
                # html.Pre(id="nodes-json", style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"}),
                WebSocket(id="ws", url=f"ws://{self.host}:{self.port}/model_update")
                # dcc.Interval(id='interval-time', interval=5000, n_intervals=10000)
            ]
        )
        return app

    def run(self, app):
        app.run(debug=self.debug, port=self.port, host=self.host)
