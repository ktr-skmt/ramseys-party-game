from itertools import chain
from typing import Final


import networkx as nx

ALL_EDGES: Final[list[tuple[int, int]]] = list(
    chain.from_iterable([[(i, j) for j in range(i + 1, 6)] for i in range(6)])
)


def edge_match(e1: dict[str, str], e2: dict[str, str]) -> bool:
    return e1["color"] == e2["color"]


def get_edges(graph: nx.Graph) -> list[tuple[int, int, dict[str, str]]]:
    return [(i, j, {"color": graph.edges[i, j]["color"]}) for i, j in nx.line_graph(graph)]


def contains_a_specific_edge(g: nx.Graph, edge: tuple[int, int]) -> bool:
    for i, j in nx.line_graph(g):
        if i < j:
            if edge[0] < edge[1] and edge == (i, j):
                return True
            if edge[1] < edge[0] and edge == (j, i):
                return True
        if j < i:
            if edge[0] < edge[1] and edge == (j, i):
                return True
            if edge[1] < edge[0] and edge == (i, j):
                return True
    return False


def remaining_edges(g: nx.Graph) -> list[tuple[int, int]]:
    return [edge for edge in ALL_EDGES if not contains_a_specific_edge(g, edge)]


def next_turn_color(current_turn: int) -> str:
    if not current_turn % 2:
        return "red"
    return "blue"
