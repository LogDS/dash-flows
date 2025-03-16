
module DashFlows
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.3"

include("jl/''_animatedcirclenode.jl")
include("jl/''_animatednodeedge.jl")
include("jl/''_dashflows.jl")
include("jl/''_devtools.jl")
include("jl/''_resizablenode.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_flows",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_flows.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_flows.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
