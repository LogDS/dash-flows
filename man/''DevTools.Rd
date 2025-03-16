% Auto-generated: do not edit by hand
\name{''DevTools}

\alias{''DevTools}

\title{DevTools component}

\description{
DevTools component for displaying debug information about the flow
}

\usage{
''DevTools(nodes=NULL, viewport=NULL)
}

\arguments{
\item{nodes}{List of lists containing elements 'id', 'type'.
those elements have the following types:
  - id (character; required)
  - type (character; optional)s. Array of nodes to display information about}

\item{viewport}{Lists containing elements 'x', 'y', 'zoom'.
those elements have the following types:
  - x (numeric; required)
  - y (numeric; required)
  - zoom (numeric; required). Current viewport information including position and zoom level}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

