import copy
import dataclasses
import json
from typing import List

import dacite
import jsonpickle
import networkx
import networkx
from readerwriterlock import rwlock
from readerwriterlock.rwlock import RWLockFairD

from dashflow_model.ReactConf import ReactFlowNode, ReactFlowEdge
from dashflow_model.conf import AppConfiguration

class Model:
    # initial_nodes: List[ReactFlowNode]
    # initial_edges: List[ReactFlowEdge]
    g: networkx.MultiDiGraph
    layout:object
    lock: RWLockFairD

    def __init__(self, g:networkx.MultiDiGraph, layout: object) -> None:
        # self.initial_nodes = initial_nodes
        # self.initial_edges = initial_edges
        self.lock = rwlock.RWLockFairD()
        self.g = g
        self.layout = layout

    @staticmethod
    def from_files(json_graph_file):
        with open(json_graph_file) as f:
            js_graph = json.load(f)
        G = networkx.node_link_graph(js_graph, edges="edges")
        networkx.set_node_attributes(G,
                                     {node[0]: jsonpickle.decode(json.dumps(node[1])) for node in G.nodes(data=True)})
        networkx.set_edge_attributes(G, {(node[0], node[1], node[2]): jsonpickle.decode(json.dumps(node[3])) for node in
                                         G.edges(data=True,keys=True)})
        # initial_nodes = []
        # with open(node_file) as json_data:
        #     import jsonpickle
        #     # initial_nodes = jsonpickle.decode(json_data.read())
        #     initial_nodes = [dacite.from_dict(data_class=ReactFlowNode, data=node) for node in jsonpickle.decode(json_data.read())]
        #     # initial_edges = json.load(json_data)
        #     # json_data.close()
        #
        # initial_edges = []
        # with open(edge_file) as json_data:
        #     import jsonpickle
        #     # initial_edges = jsonpickle.decode(json_data.read())
        #     initial_edges = [dacite.from_dict(data_class=ReactFlowEdge, data=node) for node in jsonpickle.decode(json_data.read())]
        #     # initial_edges = json.load(json_data)
        #     # json_data.close()
        return Model(G, None)

    def store_current_model(self, filename):
        from dashflow_model.utils import old_format_serialize
        old_format_serialize(self, filename)

    def read_layout(self):
        with self.lock.gen_rlock():
            if self.layout is None:
                return None
            else:
                return copy.deepcopy(self.layout)

    def read_nodes_copy(self):
        with self.lock.gen_rlock():
            return networkx.node_link_data(self.g, edges="edges", nodes="nodes")["nodes"] #[dataclasses.asdict(x) for x in self.initial_nodes]

    def read_edges_copy(self):
        with self.lock.gen_rlock():
            return networkx.node_link_data(self.g, edges="edges", nodes="nodes")["edges"] #[dataclasses.asdict(x) for x in self.initial_edges]

    def update_layout(self, layout):
        with self.lock.gen_wlock():
            self.layout = layout

    def update_nodes(self, novel_nodes):
        with self.lock.gen_wlock():
            current_nodes = set(self.g.nodes)
            new_nodes = list()
            update_nodes = dict()
            for node_obj in current_nodes:
                id = node_obj.pop("id")
                final = jsonpickle.decode(json.dumps(node_obj))
                if id in current_nodes:
                    update_nodes[id] = final
                else:
                    new_nodes.append((id, final))
            delete_nodes = current_nodes.difference(set(update_nodes.keys()))
            self.g.remove_nodes_from(delete_nodes)
            networkx.set_node_attributes(self.g, update_nodes)
            self.g.add_nodes_from(new_nodes)

    def update_edges(self, novel_edges):
        from dashflow_model.utils import serializable_json, clear_for_none
        with self.lock.gen_wlock():
            self.g = networkx.create_empty_copy(self.g, with_data=True)
            for edge in novel_edges:
                source = edge.pop("source")
                target = edge.pop("target")
                self.g.add_edge(source, target, **serializable_json(clear_for_none(edge)))
