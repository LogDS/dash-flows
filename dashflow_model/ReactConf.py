import dataclasses
from typing import Optional


@dataclasses.dataclass
class Position:
    x: float
    y: float

@dataclasses.dataclass
class ReactFlowShape:
    type: str
    color: Optional[str] = None
    size: Optional[float] = None

@dataclasses.dataclass
class ReactFlowNode:
    id: str
    data: object
    position: Position
    type: Optional[str] = None
    style: Optional[object] = None

@dataclasses.dataclass
class ReactFlowEdge:
    id: str
    source: str
    target: str
    type: Optional[str] = None
    data: Optional[object] = None
    style: Optional[object] = None
    markerEnd: Optional[ReactFlowShape] = None