from matchpredictor.matchresults.result import Fixture, Outcome
from matchpredictor.predictors.predictor import Prediction, Predictor


class AlphabetPredictor(Predictor):
    """
    Class AlphabetPredictor

    A class that predicts the outcome of a fixture based on the alphabetical order of the team names.

    Inherits from the Predictor class.

    Methods:
        predict(fixture: Fixture) -> Prediction
            Predicts the outcome of a fixture based on the alphabetical order of the team names.

    Parameters:
        fixture (Fixture): The fixture object containing information about the teams.

    Returns:
        Prediction: The prediction object containing the predicted outcome.

    """
    def predict(self, fixture: Fixture) -> Prediction:
        if fixture.away_team.name[0] < fixture.home_team.name[0]:
            return Prediction(outcome=Outcome.AWAY)
        elif fixture.home_team.name[0] < fixture.away_team.name[0]:
            return Prediction(outcome=Outcome.HOME)
        else:
            return Prediction(outcome=Outcome.DRAW)