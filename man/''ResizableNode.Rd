% Auto-generated: do not edit by hand
\name{''ResizableNode}

\alias{''ResizableNode}

\title{ResizableNode component}

\description{

}

\usage{
''ResizableNode(data=NULL, selected=NULL)
}

\arguments{
\item{data}{Lists containing elements 'label', 'handles'.
those elements have the following types:
  - label (logical | numeric | character | named list | unnamed list; optional)
  - handles (required): . handles has the following type: list of lists containing elements 'id', 'type', 'position', 'style', 'isconnectable', 'isconnectablestart', 'isconnectableend', 'onconnect', 'isvalidconnection'.
those elements have the following types:
  - id (character; required)
  - type (character; required)
  - position (character; required)
  - style (named list; optional)
  - isconnectable (logical; optional)
  - isconnectablestart (logical; optional)
  - isconnectableend (logical; optional)
  - onconnect (optional)
  - isvalidconnection (optional)s. }

\item{selected}{Logical. }
}

\value{named list of JSON elements corresponding to React.js properties and their values}

