import json
from pathlib import Path
from typing import Final

import networkx as nx

from src.edge import next_turn_color, edge_match
from src.models.state import State, from_dict_to_state
from src.models.transition import Transition

PATH_TO_DIR: Final[Path] = Path(__file__).parent
PATH_TO_OUT: Final[Path] = PATH_TO_DIR / "out"


def line_to_graph(line: str) -> tuple[nx.Graph, int]:
    state: State = line_to_state(line)
    return state.to_graph(), state.variant


def line_to_state(line: str) -> State:
    json_dict: dict[str, str | int | None] = json.loads(line)
    return from_dict_to_state(json_dict)


def remove_an_edge_which_color_is(
    color: str, edges: list[tuple[int, int, dict[str, str]]]
) -> list[list[tuple[int, int, dict[str, str]]]]:
    def remove(edge: tuple[int, int, dict[str, str]]) -> list[tuple[int, int, dict[str, str]]]:
        temp_edges = edges.copy()
        temp_edges.remove(edge)
        return temp_edges

    return [remove(edge) for edge in edges if edge[2]["color"] == color]


def get_transitions(
    current_turn: int, next_color: str, current_turn_graphs: list[tuple[nx.Graph, int]], next_turn_states: list[State]
) -> list[Transition]:
    transitions: list[Transition] = []
    for next_turn_state in next_turn_states:
        for edges_without_an_edge in remove_an_edge_which_color_is(color=next_color, edges=next_turn_state.edges()):
            nodes: list[int] = []
            for i, j, _ in edges_without_an_edge:
                if i not in nodes:
                    nodes.append(i)
                if j not in nodes:
                    nodes.append(j)
            graph = nx.Graph()
            graph.add_nodes_from(nodes)
            graph.add_edges_from(edges_without_an_edge)
            transitions.extend(
                [
                    Transition(
                        current_turn=current_turn,
                        current_turn_variant=current_turn_variant,
                        next_turn_variant=next_turn_state.variant,
                    )
                    for current_turn_graph, current_turn_variant in current_turn_graphs
                    if nx.is_isomorphic(
                        current_turn_graph,
                        graph,
                        edge_match=edge_match,
                    )
                ]
            )
    return transitions


def main() -> None:
    for next_turn in range(15, 1, -1):
        current_turn: int = next_turn - 1
        print("current_turn")
        print(current_turn)
        with open(PATH_TO_OUT / f"{current_turn}.jsonl", mode="r", encoding="utf-8") as f:
            current_turn_graphs: list[tuple[nx.Graph, int]] = [line_to_graph(line) for line in f]
        with open(PATH_TO_OUT / f"{next_turn}.jsonl", mode="r", encoding="utf-8") as f:
            next_turn_states: list[State] = [line_to_state(line) for line in f]
        transitions: list[Transition] = get_transitions(
            current_turn=current_turn,
            next_color=next_turn_color(current_turn),
            current_turn_graphs=current_turn_graphs,
            next_turn_states=next_turn_states,
        )
        print("len(transitions)")
        print(len(transitions))
        transition_json_list: list[dict[str, int]] = [transition.to_dict() for transition in transitions]
        with open(PATH_TO_OUT / f"t_{current_turn}-{next_turn}.jsonl", mode="w", encoding="utf-8") as f:
            for transition_json in transition_json_list:
                json.dump(transition_json, f, ensure_ascii=False)
                f.write("\n")


if __name__ == "__main__":
    main()
