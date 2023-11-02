from dataclasses import dataclass


@dataclass
class Territory:
    turn: int
    variant: int
    what_color_wins: str | None = None


def json_to_territory(json: dict[str, int | str | None]) -> Territory:
    return Territory(json["turn"], json["variant"], json["what_color_wins"])
