# AUTO GENERATED FILE - DO NOT EDIT

export animatedcirclenode

"""
    animatedcirclenode(;kwargs...)

An AnimatedCircleNode component.

Keyword arguments:
- `data` (required): . data has the following type: lists containing elements 'label'.
Those elements have the following types:
  - `label` (Bool | Real | String | Dict | Array; optional)
"""
function animatedcirclenode(; kwargs...)
        available_props = Symbol[:data]
        wild_props = Symbol[]
        return Component("animatedcirclenode", "AnimatedCircleNode", "dash_flows", available_props, wild_props; kwargs...)
end

