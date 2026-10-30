"""F1 championship tracker."""

from importlib.metadata import version

from f1_tracker.models import Driver, RaceResult, Season, Team

__version__ = version("f1-tracker")
__all__ = ["Driver", "RaceResult", "Season", "Team"]
