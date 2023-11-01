import json
from pathlib import Path
from typing import Final

import networkx as nx

from src.edge import edge_match, remaining_edges, next_turn_color
from src.models.state import State, from_graph_to_state
from src.triangle import contains_a_blue_triangle, contains_a_red_triangle

PATH_TO_DIR: Final[Path] = Path(__file__).parent
PATH_TO_OUT: Final[Path] = PATH_TO_DIR / "out"


def temp_next_turn_graphs(current_turn_graphs: list[nx.Graph], current_turn: int) -> list[nx.Graph]:
    t_next_turn_graphs: list[nx.Graph] = []
    next_color: str = next_turn_color(current_turn)
    for current_turn_graph in current_turn_graphs:
        for r_edge in remaining_edges(current_turn_graph):
            temp_graph: nx.Graph = current_turn_graph.copy()
            temp_graph.add_edge(r_edge[0], r_edge[1], color=next_color)
            if (
                next_color == "blue"
                and not contains_a_blue_triangle(temp_graph)
                or next_color == "red"
                and not contains_a_red_triangle(temp_graph)
            ):
                t_next_turn_graphs.append(temp_graph)
    return t_next_turn_graphs


def remove_isomorphic_graphs(graphs: list[nx.Graph]) -> list[nx.Graph]:
    new_graphs: list[nx.Graph] = []
    for graph in graphs:
        contains_in_list: bool = False
        for new_graph in new_graphs:
            if nx.is_isomorphic(graph, new_graph, edge_match=edge_match):
                contains_in_list = True
                break
        if not contains_in_list:
            new_graphs.append(graph)
    return new_graphs


def next_turn_graphs(current_turn_graphs: list[nx.Graph], current_turn: int) -> list[nx.Graph]:
    return remove_isomorphic_graphs(temp_next_turn_graphs(current_turn_graphs, current_turn))


def main() -> None:
    turn: int = 0
    g_list = [nx.Graph()]
    while g_list:  # pylint: disable=while-used
        g_list = next_turn_graphs(current_turn_graphs=g_list, current_turn=turn)
        turn += 1
        print(f"turn {turn}")
        print(f"{len(g_list)} states")
        state_list: list[State] = [
            from_graph_to_state(graph=g, turn=turn, variant=index) for index, g in enumerate(g_list)
        ]
        json_list: list[dict[str, str | int | None]] = [state.to_dict() for state in state_list]
        with open(PATH_TO_OUT / f"{turn}.jsonl", mode="w", encoding="utf-8") as f:
            for json_dict in json_list:
                json.dump(json_dict, f, ensure_ascii=False)
                f.write("\n")


if __name__ == "__main__":
    main()
