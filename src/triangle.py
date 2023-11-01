from itertools import combinations


import networkx as nx

from src.edge import edge_match, get_edges


red_triangle = nx.Graph()
red_triangle.add_nodes_from([0, 1, 2])
red_triangle.add_edges_from([(0, 1), (1, 2), (2, 0)], color="red")

blue_triangle = nx.Graph()
blue_triangle.add_nodes_from([0, 1, 2])
blue_triangle.add_edges_from([(0, 1), (1, 2), (2, 0)], color="blue")


def is_a_specific_triangle(g: nx.Graph, triangle: nx.Graph) -> bool:
    if nx.is_isomorphic(g, triangle, edge_match=edge_match):
        return True
    return False


def contains_a_specific_triangle(g: nx.Graph, triangle: nx.Graph) -> bool:
    edges: list[tuple[int, int, dict[str, str]]] = get_edges(g)
    for edge1, edge2, edge3 in combinations(edges, 3):
        nodes = {edge1[0], edge1[1], edge2[0], edge2[1], edge3[0], edge3[1]}
        if len(nodes) == 3:
            combination_graph = nx.Graph()
            combination_graph.add_nodes_from(list(nodes))
            combination_graph.add_edges_from([edge1, edge2, edge3])
            if is_a_specific_triangle(combination_graph, triangle):
                return True
    return False


def contains_a_red_triangle(g: nx.Graph) -> bool:
    return contains_a_specific_triangle(g, red_triangle)


def contains_a_blue_triangle(g: nx.Graph) -> bool:
    return contains_a_specific_triangle(g, blue_triangle)
