import json
from pathlib import Path
from typing import Final

from src.edge import ALL_EDGES, contains_a_specific_edge_

from src.models.state import State, from_dict_to_state

PATH_TO_DIR: Final[Path] = Path(__file__).parent
PATH_TO_OUT: Final[Path] = PATH_TO_DIR / "out"
PATH_TO_DOCS: Final[Path] = PATH_TO_DIR / "docs"
PATH_TO_TURN: Final[Path] = PATH_TO_DOCS / "script" / "turn"


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
        with open(PATH_TO_TURN / f"dot{turn}.js", mode="w", encoding="utf-8") as f:
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
        match turn:
            case 4:
                for i in range(2):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_21_25.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_21_25 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(20, 25)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 5:
                for i in range(6):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_61_64.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_61_64 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(60, 64)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 6:
                for i in range(16):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_161_166.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_161_166 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(160, 166)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 7:
                for i in range(30):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_301_303.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_301_303 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(300, 303)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 8:
                for i in range(50):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
            case 9:
                for i in range(48):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_481_489.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_481_489 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(480, 489)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 10:
                for i in range(41):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_411_415.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_411_415 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(410, 415)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 11:
                for i in range(18):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_181_183.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_181_183 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(180, 183)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 12:
                for i in range(7):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_71.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_71 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(70, 71)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)
            case 13:
                for i in range(1):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"dot{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            f"export const dot{turn}_{base + 1}_{base + 10} = "
                            + "{"
                            + "'description': ["
                            + ",".join(
                                [
                                    f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                    for state in states
                                    if state.variant in range(base, base + 10)
                                ]
                            )
                            + "]}"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"dot{turn}_11_12.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        f"export const dot{turn}_11_12 = "
                        + "{"
                        + "'description': ["
                        + ",".join(
                            [
                                f"['{state_dot(turn=state.turn, variant=state.variant, edges=state.edges())}']"
                                for state in states
                                if state.variant in range(10, 12)
                            ]
                        )
                        + "]}"
                    )
                    f.write(text)

        with open(PATH_TO_DOCS / f"turn{turn}.html", mode="w", encoding="utf-8") as f:
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
        match turn:
            case 4:
                for i in range(2):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_21_25.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_21_25"
                        + "}"
                        + f" from './dot{turn}_21_25.js';"
                        + "for (let i = 0; i < 5; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_21_25.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_21-25.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(5)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_21_25.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 5:
                for i in range(6):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_61_64.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_61_64"
                        + "}"
                        + f" from './dot{turn}_61_64.js';"
                        + "for (let i = 0; i < 4; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_61_64.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_61-64.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(4)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_61_64.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 6:
                for i in range(16):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_161_166.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_161_166"
                        + "}"
                        + f" from './dot{turn}_161_166.js';"
                        + "for (let i = 0; i < 6; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_161_166.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_161-166.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(6)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_161_166.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 7:
                for i in range(30):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_301_303.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_301_303"
                        + "}"
                        + f" from './dot{turn}_301_303.js';"
                        + "for (let i = 0; i < 3; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_301_303.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_301-303.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(3)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_301_303.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 8:
                for i in range(50):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)

            case 9:
                for i in range(48):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_481_489.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_481_489"
                        + "}"
                        + f" from './dot{turn}_481_489.js';"
                        + "for (let i = 0; i < 9; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_481_489.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_481-489.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(9)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_481_489.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 10:
                for i in range(41):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_411_415.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_411_415"
                        + "}"
                        + f" from './dot{turn}_411_415.js';"
                        + "for (let i = 0; i < 5; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_411_415.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_411-415.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(5)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_411_415.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 11:
                for i in range(18):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_181_183.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_181_183"
                        + "}"
                        + f" from './dot{turn}_181_183.js';"
                        + "for (let i = 0; i < 3; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_181_183.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_181-183.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(3)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_181_183.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 12:
                for i in range(7):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_71.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_71"
                        + "}"
                        + f" from './dot{turn}_71.js';"
                        + "for (let i = 0; i < 1; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_71.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_71.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(1)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_71.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)
            case 13:
                for i in range(1):
                    base: int = i * 10
                    with open(PATH_TO_TURN / f"turn{turn}_{base + 1}_{base + 10}.js", mode="w", encoding="utf-8") as f:
                        text: str = (
                            "import {"
                            + f"dot{turn}_{base + 1}_{base + 10}"
                            + "}"
                            + f" from './dot{turn}_{base + 1}_{base + 10}.js';"
                            + "for (let i = 0; i < 10; i++)"
                            + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                            + f"dot{turn}_{base + 1}_{base + 10}.description[i].join('')); "
                            + "}"
                        )
                        f.write(text)
                    with open(
                        PATH_TO_DOCS / f"turn{turn}_{base + 1}-{base + 10}.html", mode="w", encoding="utf-8"
                    ) as f:
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
                                [
                                    f'<div id="graph{variant}" style="text-align: center;"></div>'
                                    for variant in range(10)
                                ]
                            )
                            + f'<script type="module" src="script/turn/turn{turn}_{base + 1}_{base + 10}.js"></script>'
                            + "</body>"
                            + "</html>"
                        )
                        f.write(text)
                with open(PATH_TO_TURN / f"turn{turn}_11_12.js", mode="w", encoding="utf-8") as f:
                    text: str = (
                        "import {"
                        + f"dot{turn}_11_12"
                        + "}"
                        + f" from './dot{turn}_11_12.js';"
                        + "for (let i = 0; i < 2; i++)"
                        + " { d3.select(`#graph${i}`).graphviz().fade(false).renderDot("
                        + f"dot{turn}_11_12.description[i].join('')); "
                        + "}"
                    )
                    f.write(text)
                with open(PATH_TO_DOCS / f"turn{turn}_11-12.html", mode="w", encoding="utf-8") as f:
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
                            [f'<div id="graph{variant}" style="text-align: center;"></div>' for variant in range(2)]
                        )
                        + f'<script type="module" src="script/turn/turn{turn}_11_12.js"></script>'
                        + "</body>"
                        + "</html>"
                    )
                    f.write(text)


if __name__ == "__main__":
    main()
