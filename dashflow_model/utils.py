import json

from werkzeug.exceptions import UnsupportedMediaType


def clear_for_none(obj):
    if obj is None:
        raise UnsupportedMediaType()
    elif isinstance(obj, list):
        return [clear_for_none(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: clear_for_none(v) for k, v in obj.items() if v is not None}
    else:
        return obj

def serializable_json(obj):
    import jsonpickle
    return json.loads(jsonpickle.encode(obj))

def old_format_serialize(model, filename="data/react-flow-example.json"):
    import networkx
    G = networkx.DiGraph()
    for node in model.read_nodes_copy():
        id = node.pop("id")
        G.add_node(id, **serializable_json(clear_for_none(node)))
    for edge in model.read_edges_copy():
        source = edge.pop("source")
        target = edge.pop("target")
        G.add_edge(source, target, **serializable_json(clear_for_none(edge)))
    # networkx.write_gexf(G, "data/react-flow-example.gexf")
    with open(filename, "w") as f:
        json.dump(networkx.node_link_data(G, edges="edges", nodes="nodes"), f, indent=4)