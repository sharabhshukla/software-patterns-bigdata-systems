from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Team(object):
    """
    This class represents a team.

    Attributes:
        name (str): The name of the team.

    """
    name: str


@dataclass(frozen=True)
class Fixture(object):
    """
    This class represents a fixture in a sports league.

    Attributes:
        home_team (Team): The home team participating in the fixture.
        away_team (Team): The away team participating in the fixture.
        league (str): The name of the league in which the fixture is taking place.
    """
    home_team: Team
    away_team: Team
    league: str


@dataclass(frozen=True)
class Scenario(object):
    """

    This class represents a scenario in a sports match.

    Attributes:
        minutes_elapsed (int): The number of minutes elapsed in the match.
        home_goals (int): The number of goals scored by the home team.
        away_goals (int): The number of goals scored by the away team.

    """
    minutes_elapsed: int
    home_goals: int
    away_goals: int


class Outcome(str, Enum):
    """
    Outcome

    This class represents the possible outcomes of a game or event. It is a subclass of the str class and extends the Enum class.

    Attributes:
        HOME (Outcome): Represents the outcome where the home team wins.
        AWAY (Outcome): Represents the outcome where the away team wins.
        DRAW (Outcome): Represents the outcome where the game ends in a draw.

    Example:
        outcome = Outcome.HOME

        outcome.value = "home"
    """
    HOME = "home"
    AWAY = "away"
    DRAW = "draw"


@dataclass
class Result(object):
    """

    This class represents a result of a sports fixture.

    Attributes:
        fixture (Fixture): The fixture object representing the matchup.
        outcome (Outcome): The outcome of the fixture (win, loss, draw).
        home_goals (int): The number of goals scored by the home team.
        away_goals (int): The number of goals scored by the away team.
        season (int): The season in which the fixture took place.

    """
    fixture: Fixture
    outcome: Outcome
    home_goals: int
    away_goals: int
    season: int
