import networkx as nx

final_graph = nx.Graph()
final_graph.add_nodes_from([0, 1, 2, 3, 4, 5])
final_graph.add_edges_from(
    [
        (0, 1, {"color": "red"}),
        (0, 2, {"color": "blue"}),
        (0, 3, {"color": "red"}),
        (0, 4, {"color": "blue"}),
        (0, 5, {"color": "red"}),
        (1, 2, {"color": "blue"}),
        (1, 3, {"color": "blue"}),
        (1, 4, {"color": "red"}),
        (1, 5, {"color": "blue"}),
        (2, 3, {"color": "red"}),
        (2, 4, {"color": "red"}),
        (2, 5, {"color": "red"}),
        (3, 4, {"color": "blue"}),
        (3, 5, {"color": "red"}),
        (4, 5, {"color": "blue"}),
    ]
)
pre_final_graph = nx.Graph()
pre_final_graph.add_nodes_from([0, 1, 2, 3, 4, 5])
pre_final_graph.add_edges_from(
    [
        (0, 1, {"color": "red"}),
        (0, 2, {"color": "blue"}),
        (0, 3, {"color": "red"}),
        (0, 4, {"color": "blue"}),
        (0, 5, {"color": "red"}),
        (1, 2, {"color": "blue"}),
        (1, 3, {"color": "blue"}),
        (1, 4, {"color": "red"}),
        (1, 5, {"color": "blue"}),
        (2, 3, {"color": "red"}),
        (2, 4, {"color": "red"}),
        (2, 5, {"color": "red"}),
        (3, 4, {"color": "blue"}),
        (4, 5, {"color": "blue"}),
    ]
)
