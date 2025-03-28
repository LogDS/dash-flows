# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AnimatedCircleNode(Component):
    """An AnimatedCircleNode component.


Keyword arguments:

- data (dict; required)

    `data` is a dict with keys:

    - label (boolean | number | string | dict | list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flows'
    _type = 'AnimatedCircleNode'
    Data = TypedDict(
        "Data",
            {
            "label": NotRequired[typing.Any]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        data: typing.Optional["Data"] = None,
        **kwargs
    ):
        self._prop_names = ['data']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['data']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AnimatedCircleNode, self).__init__(**args)
