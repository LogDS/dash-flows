# AUTO GENERATED FILE - DO NOT EDIT

export ''_devtools

"""
    ''_devtools(;kwargs...)

A DevTools component.
DevTools component for displaying debug information about the flow
Keyword arguments:
- `nodes` (required): Array of nodes to display information about. nodes has the following type: Array of lists containing elements 'id', 'type'.
Those elements have the following types:
  - `id` (String; required)
  - `type` (String; optional)s
- `viewport` (required): Current viewport information including position and zoom level. viewport has the following type: lists containing elements 'x', 'y', 'zoom'.
Those elements have the following types:
  - `x` (Real; required)
  - `y` (Real; required)
  - `zoom` (Real; required)
"""
function ''_devtools(; kwargs...)
        available_props = Symbol[:nodes, :viewport]
        wild_props = Symbol[]
        return Component("''_devtools", "DevTools", "dash_flows", available_props, wild_props; kwargs...)
end

