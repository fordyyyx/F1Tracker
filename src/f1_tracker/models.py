"""Models - holds the classes for the teams, drivers, and races"""

from dataclasses import dataclass
from enum import StrEnum


@dataclass
class Team:
    """Class that stores a team."""

    team_id: str
    name: str


@dataclass
class Driver:
    """Class that stores a driver."""

    driver_id: str
    name: str


class ResultStatus(StrEnum):
    FINISHED = "FINISHED"
    DNF = "DNF"
    DNS = "DNS"
    DSQ = "DSQ"


@dataclass(frozen=True)
class RaceResult:
    """Class that holds a result for a single driver in a race."""

    driver_id: str
    team_id: str
    position: int
    status: ResultStatus
    fastest_lap: bool = False


class SessionType(StrEnum):
    RACE = "RACE"
    SPRINT = "SPRINT"


@dataclass
class Race:
    """Class that holds all data for a single race."""

    round_num: int
    name: str
    session_type: SessionType
    results: list[RaceResult]


@dataclass
class Season:
    """Class that holds all data for a single season."""

    year: int
    teams: dict[str, Team]
    drivers: dict[str, Driver]
    races: list[Race]
