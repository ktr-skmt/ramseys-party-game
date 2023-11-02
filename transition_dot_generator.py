import json
from pathlib import Path
from typing import Final

from src.models.state import State, from_dict_to_state
from src.models.territory import Territory, json_to_territory
from src.models.transition import Transition, json_to_transition

PATH_TO_DIR: Final[Path] = Path(__file__).parent
PATH_TO_OUT: Final[Path] = PATH_TO_DIR / "out"


def nodes_text(turn: int, number_of_variants: int) -> str:
    return ";".join([f'"{turn}-{variant + 1}"' for variant in range(number_of_variants)])


def rank_dot(turn: int, number_of_variants: int) -> str:
    return "{" + f"rank = same; {nodes_text(turn, number_of_variants)}" + "};"


def ranks_dot(turn_number_of_variants_pairs: list[tuple[int, int]]) -> str:
    return "".join([rank_dot(turn, number_of_variants) for turn, number_of_variants in turn_number_of_variants_pairs])


def node_dot(turn: int, variant: int, color: str) -> str:
    return f'"{turn}-{variant + 1}" [fillcolor = {color}, style = filled];'


def nodes_dot(turn_variant_color_tuples: list[tuple[int, int, str]]) -> str:
    return "".join([node_dot(turn, variant, color) for turn, variant, color in turn_variant_color_tuples])


def link_dot(current_turn: int, current_variant: int, next_variant: int) -> str:
    color: str = "blue" if current_turn % 2 else "red"
    return f'"{current_turn}-{current_variant}" -> "{current_turn + 1}-{next_variant}" [color = {color}];'


def links_dot(transitions: list[Transition]) -> str:
    return "".join(
        [
            link_dot(transition.current_turn, transition.current_turn_variant, transition.next_turn_variant)
            for transition in transitions
        ]
    )


def transition_dot(
    transitions: list[Transition],
    turn_number_of_variants_pairs: list[tuple[int, int]],
    turn_variant_color_tuples: list[tuple[int, int, str]],
) -> str:
    return (
        "digraph transitions {"
        + "  graph ["
        + '    charset = "UTF-8";'
        + '    label = "K6 - Transitions",'
        + '    labelloc = "t",'
        + '    labeljust = "c",'
        + '    bgcolor = "#f0f0f0",'
        + "    fontcolor = black,"
        + "    fontsize = 18,"
        + '    style = "filled",'
        + "    rankdir = LR,"
        + "    margin = 0.2,"
        + "    splines = spline,"
        + "    ranksep = 1.0,"
        + "    nodesep = 0.9"
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
        + "    height = 0.6,"
        + "    width = 1.2"
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
        + "    arrowhead = normal"
        + "  ];"
        + "  rankdir = LR;"
        + ranks_dot(turn_number_of_variants_pairs)
        + nodes_dot(turn_variant_color_tuples)
        + links_dot(transitions)
        + "}"
    )


def main() -> None:
    turn_number_of_variants_pairs: list[tuple[int, int]] = []
    for turn in range(1, 15):
        with open(PATH_TO_OUT / f"{turn}.jsonl", mode="r", encoding="utf-8") as f:
            states: list[State] = [from_dict_to_state(json.loads(line)) for line in f]
        turn_number_of_variants_pairs.append((turn, len(states)))
    with open(PATH_TO_OUT / "territories.jsonl", mode="r", encoding="utf-8") as f:
        territories: list[Territory] = [json_to_territory(json.loads(line)) for line in f]
    turn_variant_color_tuples: list[tuple[int, int, str]] = [
        (territory.turn, territory.variant, territory.what_color_wins) for territory in territories
    ]
    transitions: list[Transition] = []
    for turn in range(1, 15):
        with open(PATH_TO_OUT / f"t_{turn}-{turn + 1}.jsonl", mode="r", encoding="utf-8") as f:
            transitions.extend([json_to_transition(json.loads(line)) for line in f])
    with open(PATH_TO_DIR / "docs" / "script" / "dot.js", mode="w", encoding="utf-8") as f:
        text: str = (
            "const dot = {'description': [["
            + transition_dot(transitions, turn_number_of_variants_pairs, turn_variant_color_tuples)
            + "]]}"
        )
        f.write(text)


if __name__ == "__main__":
    main()
