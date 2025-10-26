
from dash import html, Input, Output, ctx, State, clientside_callback, _dash_renderer, dcc
from dashflow_model import Model, AppConfiguration

_dash_renderer._set_react_version("18.2.0")

model = Model.from_files("data/initial_nodes.json", "data/initial_edges.json")
conf = AppConfiguration.from_yaml("data/app_conf.yaml")
app = conf.init(model)


@app.callback(
    Output("react-flow-example", "nodes"),
    Output("react-flow-example", "edges"),
    Output("react-flow-example", "layoutOptions"),
    Input("ws", "msg"),
    Input("layout-config", "data"),
suppress_callback_exceptions=True,
    prevent_initial_call=True,
)
def Controller(ws_value, layout):
    triggered_id = ctx.triggered_id
    if (triggered_id == "layout-config") and layout:
        model.update_layout(layout)
    else:
        if ws_value and ws_value is not None:
            print(f"do something with: {ws_value}")
            # model.update_nodes() / model.update_edges()
        else:
            print("pass")
    return model.read_nodes_copy(), model.read_edges_copy(), model.read_layout()

if __name__ == "__main__":
    conf.run(app)