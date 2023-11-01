import json
from pathlib import Path
from typing import Final

PATH_TO_DIR: Final[Path] = Path(__file__).parent
PATH_TO_OUT: Final[Path] = PATH_TO_DIR / "out"


def transition(line: str) -> tuple[int, int]:
    json_dict: dict[str, int] = json.loads(line)
    return json_dict["current_turn_variant"], json_dict["next_turn_variant"]


def main() -> None:
    goals: dict[int, list[int]] = {}
    for next_turn in range(15, 1, -1):
        current_turn: int = next_turn - 1
        print("current_turn")
        print(current_turn)
        with open(PATH_TO_OUT / f"{current_turn}.jsonl", mode="r", encoding="utf-8") as f:
            number_of_variants: int = len([line for line in f])
        with open(PATH_TO_OUT / f"t_{current_turn}-{next_turn}.jsonl", mode="r", encoding="utf-8") as f:
            transitions: list[tuple[int, int]] = [transition(line) for line in f]
        sources: set[int] = {i for i, _ in transitions}
        goals[current_turn] = [variant for variant in range(number_of_variants) if variant not in sources]
    with open(PATH_TO_OUT / "goals.json", mode="w", encoding="utf-8") as f:
        json.dump(goals, f, indent=4)


if __name__ == "__main__":
    main()
