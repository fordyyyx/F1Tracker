# F1Tracker

A Formula 1 championship tracker in Python: save and load seasons as JSON, and
calculate driver and team standings at any point in a season, including
tie-breaks decided by countback.

> **Status:** early development. The data models and the points rules are built
> and tested. Standings, saving and loading, and the command-line interface are
> next.

## Background

This is a rebuild of an object-oriented Python project I first wrote in
September 2022. The original had a mutable default argument bug, so this
version runs a linter rule (flake8-bugbear's B006, through Ruff) that catches
that mistake automatically.

## What it will do

- Save and load a season's teams, drivers and results as JSON
- Score every race and sprint using that season's points system
- Work out the driver and team standings after any round of the season
- Break ties by countback: most wins first, then most second places, and so on

## What's built so far

- **Data models** (`models.py`): teams, drivers, races and sprints, seasons,
  and each driver's result, including finishing status (finished, DNF, DNS,
  disqualified) and fastest lap
- **Points rules** (`rules.py`): race and sprint points tables, and a points
  system for each season. The bonus point for fastest lap, for a top-10
  finisher, applies from 2022 to 2024 and is dropped from 2025.
  `points_for()` scores a single result.
- **Tests** (`tests/test_rules.py`): 12 tests for the points rules

## How it's built

- Python 3.12 or later, with no runtime dependencies
- **pytest** for tests, **Ruff** for linting and formatting, and **mypy** in
  strict mode for type checking
- **GitHub Actions** runs all four checks on Python 3.12 to 3.15 for every
  push to `main` and every pull request

## How AI was used

AI suggested the overall structure of the repository. While I build it, AI
suggests ways to shape classes and name functions, and gives feedback on my
implementations, but I write the code myself.

## Running the tests

```
pip install -e ".[dev]"
pytest
```

## Licence

MIT. See [LICENSE](LICENSE).
