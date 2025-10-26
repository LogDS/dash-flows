# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class DashFlows(Component):
    """A DashFlows component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; default ''):
    CSS class name for the container div.

- edges (list of dicts; optional):
    Array of edges defining connections between nodes.

    `edges` is a list of dicts with keys:

    - id (string; required)

    - source (string; required)

    - target (string; required)

    - type (string; optional)

    - data (dict; optional)

    - style (dict; optional)

    - markerEnd (dict; optional)

        `markerEnd` is a dict with keys:

        - type (string; required)

        - color (string; optional)

        - size (number; optional)

- elementsSelectable (boolean; default True):
    Enable/disable the ability to select elements.

- layoutOptions (string; optional):
    Layout options for arranging nodes using the ELK layout engine.

- nodes (list of dicts; optional):
    Array of nodes to display in the flow.

    `nodes` is a list of dicts with keys:

    - id (string; required)

    - type (string; optional)

    - data (dict; required)

    - position (dict; required)

        `position` is a dict with keys:

        - x (number; required)

        - y (number; required)

    - style (dict; optional)

- nodesConnectable (boolean; default True):
    Enable/disable the ability to make new connections between nodes.

- nodesDraggable (boolean; default True):
    Enable/disable node dragging behavior.

- showBackground (boolean; default True):
    Show/hide the background pattern.

- showControls (boolean; default True):
    Show/hide the control panel.

- showDevTools (boolean; default False):
    Show/hide the developer tools panel.

- showMiniMap (boolean; default True):
    Show/hide the minimap navigation component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flows'
    _type = 'DashFlows'
    NodesPosition = TypedDict(
        "NodesPosition",
            {
            "x": NumberType,
            "y": NumberType
        }
    )

    Nodes = TypedDict(
        "Nodes",
            {
            "id": str,
            "type": NotRequired[str],
            "data": dict,
            "position": "NodesPosition",
            "style": NotRequired[dict]
        }
    )

    EdgesMarkerEnd = TypedDict(
        "EdgesMarkerEnd",
            {
            "type": str,
            "color": NotRequired[str],
            "size": NotRequired[NumberType]
        }
    )

    Edges = TypedDict(
        "Edges",
            {
            "id": str,
            "source": str,
            "target": str,
            "type": NotRequired[str],
            "data": NotRequired[dict],
            "style": NotRequired[dict],
            "markerEnd": NotRequired["EdgesMarkerEnd"]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        nodesDraggable: typing.Optional[bool] = None,
        nodesConnectable: typing.Optional[bool] = None,
        elementsSelectable: typing.Optional[bool] = None,
        showMiniMap: typing.Optional[bool] = None,
        showControls: typing.Optional[bool] = None,
        showBackground: typing.Optional[bool] = None,
        nodes: typing.Optional[typing.Sequence["Nodes"]] = None,
        edges: typing.Optional[typing.Sequence["Edges"]] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        showDevTools: typing.Optional[bool] = None,
        layoutOptions: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'edges', 'elementsSelectable', 'layoutOptions', 'nodes', 'nodesConnectable', 'nodesDraggable', 'showBackground', 'showControls', 'showDevTools', 'showMiniMap', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'edges', 'elementsSelectable', 'layoutOptions', 'nodes', 'nodesConnectable', 'nodesDraggable', 'showBackground', 'showControls', 'showDevTools', 'showMiniMap', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashFlows, self).__init__(**args)

setattr(DashFlows, "__init__", _explicitize_args(DashFlows.__init__))
