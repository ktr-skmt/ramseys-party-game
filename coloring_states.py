import json
from pathlib import Path
from typing import Final

from src.models.transition import Transition, json_to_transition
from src.models.territory import Territory

PATH_TO_DIR: Final[Path] = Path(__file__).parent
PATH_TO_OUT: Final[Path] = PATH_TO_DIR / "out"


def has_no_none(territories: list[str | None]) -> bool:
    return not any(territory is None for territory in territories)


def main() -> None:
    territories: list[list[str | None]] = []  # NOTE: territories[turn][variant] = "red" | "blue" | None
    turn_number_of_variants_map: dict[int, int] = {}
    for turn in range(15):
        if not turn:
            territories.append([])
        else:
            with open(PATH_TO_OUT / f"{turn}.jsonl", mode="r", encoding="utf-8") as f:
                number_of_variants: int = len(list(f))
            territories.append([None for _ in range(number_of_variants)])
            turn_number_of_variants_map[turn] = number_of_variants
    with open(PATH_TO_OUT / "goals.jsonl", mode="r", encoding="utf-8") as f:
        goals: list[dict[str, int | list[int]]] = [json.loads(line) for line in f]
    for goal in goals:
        turn: int = goal["turn"]
        for variant in goal["goals"]:
            result: str = "red" if turn % 2 else "blue"
            territories[turn][variant] = result
    for turn in range(14, 0, -1):
        if has_no_none(territories[turn]):
            continue
        with open(PATH_TO_OUT / f"t_{turn}-{turn + 1}.jsonl", mode="r", encoding="utf-8") as f:
            transitions: list[Transition] = [json_to_transition(json.loads(line)) for line in f]
        number_of_variants: int = turn_number_of_variants_map[turn]
        for variant in range(number_of_variants):
            if not territories[turn][variant]:
                option: set[str] = set()
                for transition in transitions:
                    if transition.current_turn_variant == variant:
                        result: str | None = territories[turn + 1][transition.next_turn_variant]
                        if result and result not in option:
                            option.add(result)
                match len(option):
                    case 1:
                        territories[turn][variant] = option.pop()
                    case 2:
                        territories[turn][variant] = "blue" if turn % 2 else "red"

    with open(PATH_TO_OUT / "territories.jsonl", mode="w", encoding="utf-8") as f:
        for turn in range(1, 15):
            for variant in range(len(territories[turn])):
                territory: Territory = Territory(turn, variant, territories[turn][variant])
                json.dump(territory.__dict__, f, ensure_ascii=False)
                f.write("\n")


if __name__ == "__main__":
    main()
