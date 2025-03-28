# AUTO GENERATED FILE - DO NOT EDIT

export resizablenode

"""
    resizablenode(;kwargs...)

A ResizableNode component.

Keyword arguments:
- `data` (required): . data has the following type: lists containing elements 'label', 'handles'.
Those elements have the following types:
  - `label` (Bool | Real | String | Dict | Array; optional)
  - `handles` (required): . handles has the following type: Array of lists containing elements 'id', 'type', 'position', 'style', 'isConnectable', 'isConnectableStart', 'isConnectableEnd', 'onConnect', 'isValidConnection'.
Those elements have the following types:
  - `id` (String; required)
  - `type` (String; required)
  - `position` (String; required)
  - `style` (Dict; optional)
  - `isConnectable` (Bool; optional)
  - `isConnectableStart` (Bool; optional)
  - `isConnectableEnd` (Bool; optional)
  - `onConnect` (optional)
  - `isValidConnection` (optional)s
- `selected` (Bool; optional)
"""
function resizablenode(; kwargs...)
        available_props = Symbol[:data, :selected]
        wild_props = Symbol[]
        return Component("resizablenode", "ResizableNode", "dash_flows", available_props, wild_props; kwargs...)
end

