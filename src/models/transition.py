from dataclasses import dataclass


@dataclass
class Transition:
    current_turn: int
    current_turn_variant: int
    next_turn_variant: int

    def next_turn(self) -> int:
        return self.current_turn + 1

    def to_dict(self) -> dict[str, int]:
        return {
            "current_turn": self.current_turn,
            "current_turn_variant": self.current_turn_variant,
            "next_turn_variant": self.next_turn_variant,
        }


def json_to_transition(json: dict[str, int]) -> Transition:
    return Transition(
        current_turn=json["current_turn"],
        current_turn_variant=json["current_turn_variant"],
        next_turn_variant=json["next_turn_variant"],
    )
