import json
from pathlib import Path
from typing import Final

from src.edge import ALL_EDGES, contains_a_specific_edge_

# from src.models.territory import Territory, json_to_territory
from src.models.state import State, from_dict_to_state

PATH_TO_DIR: Final[Path] = Path(__file__).parent
PATH_TO_OUT: Final[Path] = PATH_TO_DIR / "out"


def edge_dot(edge: tuple[int, int, dict[str, str]]) -> str:
    return f'{edge[0] + 1} -> {edge[1] + 1}[label = "E{edge[0] + 1}{edge[1] + 1}", color = {edge[2]["color"]}, penwidth = 3];'


def get_attribute(i: int, j: int, edges: list[tuple[int, int, dict[str, str]]]) -> dict[str, str] | None:
    for edge in edges:
        if i == edge[0] and j == edge[1]:
            return edge[2]
        if j == edge[0] and i == edge[1]:
            return edge[2]
    return None


def edges_dot(edges: list[tuple[int, int, dict[str, str]]]) -> str:
    edges_text: str = ""
    for i, j in ALL_EDGES:
        if contains_a_specific_edge_([(x, y) for x, y, _ in edges], (i, j)):
            edges_text += edge_dot((i, j, get_attribute(i, j, edges)))
        else:
            edges_text += f'{i + 1} -> {j + 1}[label = "E{i + 1}{j + 1}"];'
    return edges_text


def state_dot(turn: int, variant: int, edges: list[tuple[int, int, dict[str, str]]]) -> str:
    return (
        "digraph graph_name "
        + "{"
        + "  graph ["
        + '    charset = "UTF-8";'
        + f'    label = "K6 - Turn {turn}-{variant + 1}",'
        + '    labelloc = "t",'
        + '    labeljust = "c",'
        + '    bgcolor = "#f0f0f0",'
        + "    fontcolor = black,"
        + "    fontsize = 18,"
        + '    style = "filled",'
        + "    rankdir = TB,"
        + "    margin = 0.2,"
        + "    splines = spline,"
        + "    ranksep = 1.0,"
        + "    nodesep = 0.9"
        + "    layout = neato"
        + "  ];"
        + "  node ["
        + '    colorscheme = "greys9"'
        + '    style = "solid,filled",'
        + "    fontsize = 16,"
        + "    fontcolor = 9,"
        + '    fontname = "Migu 1M",'
        + "    color = 9,"
        + "    fillcolor = 1,"
        + "    fixedsize = true,"
        + "    height = 0.3,"
        + "    width = 0.3"
        + "  ];"
        + "  edge ["
        + "    style = solid,"
        + "    fontsize = 14,"
        + "    fontcolor = black,"
        + '    fontname = "Migu 1M",'
        + "    color = black,"
        + "    labelfloat = true,"
        + "    labeldistance = 2.5,"
        + "    labelangle = 70"
        + "    arrowhead = none"
        + "  ];"
        + "  rankdir = TB;"
        + "  {rank = same; 1};"
        + "  {rank = same; 2;6};"
        + "  {rank = same; 3;5};"
        + "  {rank = same; 4};"
        + '  1[pos="1,1!"];'
        + '  2[pos="1.866,0.5!"];'
        + '  3[pos="1.866,-0.5!"];'
        + '  4[pos="1,-1!"];'
        + '  5[pos="0.134,-0.5!"];'
        + '  6[pos="0.134,0.5!"];'
        + edges_dot(edges)
        + "}"
    )


def main() -> None:
    for turn in range(1, 15):
        with open(PATH_TO_OUT / f"{turn}.jsonl", mode="r", encoding="utf-8") as f:
            states: list[State] = [from_dict_to_state(json.loads(line)) for line in f]
        with open(PATH_TO_DIR / "docs" / "script" / "turn" / f"dot{turn}.js", mode="w", encoding="utf-8") as f:
            text: str = (
                f"export const dot{turn} = "
                + "{"
                + "'description': ["
                + ",".join(
                    [
                        f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                        for state in states
                    ]
                )
                + "]}"
            )

            f.write(text)
        with open(PATH_TO_DIR / "docs" / f"turn{turn}.html", mode="w", encoding="utf-8") as f:
            text: str = (
                "<!DOCTYPE html>"
                + '<html lang="ja">'
                + "<head>"
                + '<meta charset="UTF-8">'
                + "</head>"
                + "<body>"
                + '<script src="//d3js.org/d3.v4.min.js"></script>'
                + '<script src="https://unpkg.com/viz.js@1.8.0/viz.js" type="javascript/worker"></script>'
                + '<script src="https://unpkg.com/d3-graphviz@1.4.0/build/d3-graphviz.min.js"></script>'
                + "".join(
                    [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(len(states))]
                )
                + f'<script type="module" src="script/turn/turn{turn}.js"></script>'
                + "</body>"
                + "</html>"
            )
            f.write(text)


if __name__ == "__main__":
    main()
