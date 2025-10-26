import copy
import dataclasses
from typing import List

import dacite
from readerwriterlock import rwlock
from readerwriterlock.rwlock import RWLockFairD

from dashflow_model.ReactConf import ReactFlowNode, ReactFlowEdge
from dashflow_model.conf import AppConfiguration

class Model:
    initial_nodes: List[ReactFlowNode]
    initial_edges: List[ReactFlowEdge]
    layout:object
    lock: RWLockFairD

    def __init__(self, initial_nodes: List[ReactFlowNode], initial_edges: List[ReactFlowEdge], layout: object) -> None:
        self.initial_nodes = initial_nodes
        self.initial_edges = initial_edges
        self.lock = rwlock.RWLockFairD()
        self.layout = layout

    @staticmethod
    def from_files(node_file, edge_file):
        initial_nodes = []
        with open(node_file) as json_data:
            import jsonpickle
            # initial_nodes = jsonpickle.decode(json_data.read())
            initial_nodes = [dacite.from_dict(data_class=ReactFlowNode, data=node) for node in jsonpickle.decode(json_data.read())]
            # initial_edges = json.load(json_data)
            # json_data.close()

        initial_edges = []
        with open(edge_file) as json_data:
            import jsonpickle
            # initial_edges = jsonpickle.decode(json_data.read())
            initial_edges = [dacite.from_dict(data_class=ReactFlowEdge, data=node) for node in jsonpickle.decode(json_data.read())]
            # initial_edges = json.load(json_data)
            # json_data.close()

        return Model(initial_nodes, initial_edges, None)

    def read_layout(self):
        with self.lock.gen_rlock():
            if self.layout is None:
                return None
            else:
                return copy.deepcopy(self.layout)

    def read_nodes_copy(self):
        with self.lock.gen_rlock():
            return [dataclasses.asdict(x) for x in self.initial_nodes]

    def read_edges_copy(self):
        with self.lock.gen_rlock():
            return [dataclasses.asdict(x) for x in self.initial_edges]

    def update_layout(self, layout):
        with self.lock.gen_wlock():
            self.layout = layout

    def update_nodes(self, novel_nodes):
        with self.lock.gen_wlock():
            self.initial_nodes = novel_nodes

    def update_edges(self, novel_edges):
        with self.lock.gen_wlock():
            self.initial_edges = novel_edges