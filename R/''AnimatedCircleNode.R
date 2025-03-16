# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''AnimatedCircleNode <- function(data=NULL) {
    
    props <- list(data=data)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'AnimatedCircleNode',
        namespace = 'dash_flows',
        propNames = c('data'),
        package = 'dashFlows'
        )

    structure(component, class = c('dash_component', 'list'))
}
