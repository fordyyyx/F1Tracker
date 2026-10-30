"""Tests for rules.py"""

from f1_tracker.models import RaceResult, ResultStatus, SessionType
from f1_tracker.rules import FASTEST_LAP_ERA_POINTS_SYSTEM, NO_FASTEST_LAP_POINTS_SYSTEM, points_for


def test_winner_scores_25() -> None:
    result = RaceResult("VER", "RBR", 1, ResultStatus.FINISHED)
    assert points_for(result, SessionType.RACE, FASTEST_LAP_ERA_POINTS_SYSTEM) == 25


def test_p11_scores_zero() -> None:
    result = RaceResult("OCO", "HAS", 11, ResultStatus.FINISHED)
    assert points_for(result, SessionType.RACE, FASTEST_LAP_ERA_POINTS_SYSTEM) == 0


def test_disqualified_winner_scores_zero() -> None:
    result = RaceResult("VER", "RBR", 1, ResultStatus.DSQ)
    assert points_for(result, SessionType.RACE, FASTEST_LAP_ERA_POINTS_SYSTEM) == 0


def test_dns_scores_zero() -> None:
    result = RaceResult("ANT", "MER", 9, ResultStatus.DNS)
    assert points_for(result, SessionType.RACE, NO_FASTEST_LAP_POINTS_SYSTEM) == 0


def test_dnf_p8_scores_4() -> None:
    result = RaceResult("NOR", "MCL", 8, ResultStatus.DNF)
    assert points_for(result, SessionType.RACE, FASTEST_LAP_ERA_POINTS_SYSTEM) == 4


def test_fastest_lap_winner_scores_26_in_2022() -> None:
    result = RaceResult("VER", "RBR", 1, ResultStatus.FINISHED, fastest_lap=True)
    assert points_for(result, SessionType.RACE, FASTEST_LAP_ERA_POINTS_SYSTEM) == 26


def test_fastest_lap_winner_scores_25_in_2025() -> None:
    result = RaceResult("PIA", "MCL", 1, ResultStatus.FINISHED, fastest_lap=True)
    assert points_for(result, SessionType.RACE, NO_FASTEST_LAP_POINTS_SYSTEM) == 25


def test_fastest_lap_p11_scores_zero() -> None:
    result = RaceResult("OCO", "HAS", 11, ResultStatus.FINISHED, fastest_lap=True)
    assert points_for(result, SessionType.RACE, FASTEST_LAP_ERA_POINTS_SYSTEM) == 0


def test_fastest_lap_sprint_winner_scores_8() -> None:
    result = RaceResult("HAM", "MER", 1, ResultStatus.FINISHED, fastest_lap=True)
    assert points_for(result, SessionType.SPRINT, FASTEST_LAP_ERA_POINTS_SYSTEM) == 8


def test_p5_without_fastest_lap_scores_10_in_2022() -> None:
    result = RaceResult("NOR", "MCL", 5, ResultStatus.FINISHED)
    assert points_for(result, SessionType.RACE, FASTEST_LAP_ERA_POINTS_SYSTEM) == 10


def test_race_table_sums_to_101() -> None:
    assert sum(FASTEST_LAP_ERA_POINTS_SYSTEM.race_table.values()) == 101


def test_sprint_table_sums_to_36() -> None:
    assert sum(FASTEST_LAP_ERA_POINTS_SYSTEM.sprint_table.values()) == 36
