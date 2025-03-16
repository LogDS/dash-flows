# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''DevTools <- function(nodes=NULL, viewport=NULL) {
    
    props <- list(nodes=nodes, viewport=viewport)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DevTools',
        namespace = 'dash_flows',
        propNames = c('nodes', 'viewport'),
        package = 'dashFlows'
        )

    structure(component, class = c('dash_component', 'list'))
}
