# AUTO GENERATED FILE - DO NOT EDIT

export dashflows

"""
    dashflows(;kwargs...)

A DashFlows component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): CSS class name for the container div
- `edges` (optional): Array of edges defining connections between nodes. edges has the following type: Array of lists containing elements 'id', 'source', 'target', 'type', 'data', 'style', 'markerEnd'.
Those elements have the following types:
  - `id` (String; required)
  - `source` (String; required)
  - `target` (String; required)
  - `type` (String; optional)
  - `data` (Dict; optional)
  - `style` (Dict; optional)
  - `markerEnd` (optional): . markerEnd has the following type: lists containing elements 'type', 'color', 'size'.
Those elements have the following types:
  - `type` (String; required)
  - `color` (String; optional)
  - `size` (Real; optional)s
- `elementsSelectable` (Bool; optional): Enable/disable the ability to select elements
- `layoutOptions` (String; optional): Layout options for arranging nodes using the ELK layout engine
- `nodes` (optional): Array of nodes to display in the flow. nodes has the following type: Array of lists containing elements 'id', 'type', 'data', 'position', 'style'.
Those elements have the following types:
  - `id` (String; required)
  - `type` (String; optional)
  - `data` (Dict; required)
  - `position` (required): . position has the following type: lists containing elements 'x', 'y'.
Those elements have the following types:
  - `x` (Real; required)
  - `y` (Real; required)
  - `style` (Dict; optional)s
- `nodesConnectable` (Bool; optional): Enable/disable the ability to make new connections between nodes
- `nodesDraggable` (Bool; optional): Enable/disable node dragging behavior
- `showBackground` (Bool; optional): Show/hide the background pattern
- `showControls` (Bool; optional): Show/hide the control panel
- `showDevTools` (Bool; optional): Show/hide the developer tools panel
- `showMiniMap` (Bool; optional): Show/hide the minimap navigation component
- `style` (Dict; optional): Custom CSS styles for the container div
"""
function dashflows(; kwargs...)
        available_props = Symbol[:id, :className, :edges, :elementsSelectable, :layoutOptions, :nodes, :nodesConnectable, :nodesDraggable, :showBackground, :showControls, :showDevTools, :showMiniMap, :style]
        wild_props = Symbol[]
        return Component("dashflows", "DashFlows", "dash_flows", available_props, wild_props; kwargs...)
end

