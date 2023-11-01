from dataclasses import dataclass

import networkx as nx

from src.edge import get_edges


@dataclass
class State:
    turn: int
    variant: int
    e01: str | None = None
    e02: str | None = None
    e03: str | None = None
    e04: str | None = None
    e05: str | None = None
    e12: str | None = None
    e13: str | None = None
    e14: str | None = None
    e15: str | None = None
    e23: str | None = None
    e24: str | None = None
    e25: str | None = None
    e34: str | None = None
    e35: str | None = None
    e45: str | None = None

    def state_id(self) -> str:
        return f"G{self.turn}-{self.variant}"

    def to_dict(self) -> dict[str, str | int | None]:
        return {
            "turn": self.turn,
            "variant": self.variant,
            "e01": self.e01,
            "e02": self.e02,
            "e03": self.e03,
            "e04": self.e04,
            "e05": self.e05,
            "e12": self.e12,
            "e13": self.e13,
            "e14": self.e14,
            "e15": self.e15,
            "e23": self.e23,
            "e24": self.e24,
            "e25": self.e25,
            "e34": self.e34,
            "e35": self.e35,
            "e45": self.e45,
        }

    def to_graph(self) -> nx.Graph:
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes())
        graph.add_edges_from(self.edges())
        return graph

    def nodes(self) -> list[int]:
        nodes: list[int] = []
        if self.e01 or self.e02 or self.e03 or self.e04 or self.e05:
            nodes.append(0)
        if self.e01 or self.e12 or self.e13 or self.e14 or self.e15:
            nodes.append(1)
        if self.e02 or self.e12 or self.e23 or self.e24 or self.e25:
            nodes.append(2)
        if self.e03 or self.e13 or self.e23 or self.e34 or self.e35:
            nodes.append(3)
        if self.e04 or self.e14 or self.e24 or self.e34 or self.e45:
            nodes.append(4)
        if self.e05 or self.e15 or self.e25 or self.e35 or self.e45:
            nodes.append(5)
        return nodes

    def edges(self) -> list[tuple[int, int, dict[str, str]]]:  # noqa: C901
        edges: list[tuple[int, int, dict[str, str]]] = []
        if self.e01:
            edges.append((0, 1, {"color": self.e01}))
        if self.e02:
            edges.append((0, 2, {"color": self.e02}))
        if self.e03:
            edges.append((0, 3, {"color": self.e03}))
        if self.e04:
            edges.append((0, 4, {"color": self.e04}))
        if self.e05:
            edges.append((0, 5, {"color": self.e05}))
        if self.e12:
            edges.append((1, 2, {"color": self.e12}))
        if self.e13:
            edges.append((1, 3, {"color": self.e13}))
        if self.e14:
            edges.append((1, 4, {"color": self.e14}))
        if self.e15:
            edges.append((1, 5, {"color": self.e15}))
        if self.e23:
            edges.append((2, 3, {"color": self.e23}))
        if self.e24:
            edges.append((2, 4, {"color": self.e24}))
        if self.e25:
            edges.append((2, 5, {"color": self.e25}))
        if self.e34:
            edges.append((3, 4, {"color": self.e34}))
        if self.e35:
            edges.append((3, 5, {"color": self.e35}))
        if self.e45:
            edges.append((4, 5, {"color": self.e45}))
        return edges


def from_dict_to_state(json: dict[str, str | int | None]) -> State:
    return State(
        turn=json["turn"],  # type: ignore
        variant=json["variant"],  # type: ignore
        e01=json["e01"],  # type: ignore
        e02=json["e02"],  # type: ignore
        e03=json["e03"],  # type: ignore
        e04=json["e04"],  # type: ignore
        e05=json["e05"],  # type: ignore
        e12=json["e12"],  # type: ignore
        e13=json["e13"],  # type: ignore
        e14=json["e14"],  # type: ignore
        e15=json["e15"],  # type: ignore
        e23=json["e23"],  # type: ignore
        e24=json["e24"],  # type: ignore
        e25=json["e25"],  # type: ignore
        e34=json["e34"],  # type: ignore
        e35=json["e35"],  # type: ignore
        e45=json["e45"],  # type: ignore
    )


def from_graph_to_state(graph: nx.Graph, turn: int, variant: int) -> State:  # noqa: C901
    state = State(turn=turn, variant=variant)
    for i, j, attribute in get_edges(graph):
        if i == 0 and j == 1 or i == 1 and j == 0:  # pylint: disable=compare-to-zero
            state.e01 = attribute["color"]
        if i == 0 and j == 2 or i == 2 and j == 0:  # pylint: disable=compare-to-zero
            state.e02 = attribute["color"]
        if i == 0 and j == 3 or i == 3 and j == 0:  # pylint: disable=compare-to-zero
            state.e03 = attribute["color"]
        if i == 0 and j == 4 or i == 4 and j == 0:  # pylint: disable=compare-to-zero
            state.e04 = attribute["color"]
        if i == 0 and j == 5 or i == 5 and j == 0:  # pylint: disable=compare-to-zero
            state.e05 = attribute["color"]
        if i == 1 and j == 2 or i == 2 and j == 1:
            state.e12 = attribute["color"]
        if i == 1 and j == 3 or i == 3 and j == 1:
            state.e13 = attribute["color"]
        if i == 1 and j == 4 or i == 4 and j == 1:
            state.e14 = attribute["color"]
        if i == 1 and j == 5 or i == 5 and j == 1:
            state.e15 = attribute["color"]
        if i == 2 and j == 3 or i == 3 and j == 2:
            state.e23 = attribute["color"]
        if i == 2 and j == 4 or i == 4 and j == 2:
            state.e24 = attribute["color"]
        if i == 2 and j == 5 or i == 5 and j == 2:
            state.e25 = attribute["color"]
        if i == 3 and j == 4 or i == 4 and j == 3:
            state.e34 = attribute["color"]
        if i == 3 and j == 5 or i == 5 and j == 3:
            state.e35 = attribute["color"]
        if i == 4 and j == 5 or i == 5 and j == 4:
            state.e45 = attribute["color"]
    return state
