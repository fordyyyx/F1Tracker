"""Module holding the customisable rules for the tracker."""

from dataclasses import dataclass
from f1_tracker.models import RaceResult, SessionType


@dataclass(frozen=True)
class PointsSystem:
    race_table: dict[int, int]
    sprint_table: dict[int, int]
    fastest_lap_point: bool = False


RACE_POINTS_TABLE: dict[int, int] = {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1,
}
SPRINT_POINTS_TABLE: dict[int, int] = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 3,
    7: 2,
    8: 1,
}

FASTEST_LAP_ERA_POINTS_SYSTEM = PointsSystem(
    race_table=RACE_POINTS_TABLE, sprint_table=SPRINT_POINTS_TABLE, fastest_lap_point=True
)
NO_FASTEST_LAP_POINTS_SYSTEM = PointsSystem(
    race_table=RACE_POINTS_TABLE, sprint_table=SPRINT_POINTS_TABLE, fastest_lap_point=False
)

POINTS_SYSTEMS: dict[int, PointsSystem] = {
    2022: FASTEST_LAP_ERA_POINTS_SYSTEM,
    2023: FASTEST_LAP_ERA_POINTS_SYSTEM,
    2024: FASTEST_LAP_ERA_POINTS_SYSTEM,
    2025: NO_FASTEST_LAP_POINTS_SYSTEM,
    2026: NO_FASTEST_LAP_POINTS_SYSTEM,
}


def points_for(result: RaceResult, session_type: SessionType, rules: PointsSystem) -> int:
    position = result.position
    if result.status in ("DSQ", "DNS"):
        return 0
    if session_type == "RACE":
        points = rules.race_table.get(position, 0)
        return (
            points + 1
            if rules.fastest_lap_point and result.fastest_lap and position <= 10
            else points
        )
    elif session_type == "SPRINT":
        return rules.sprint_table.get(position, 0)
    return 0
