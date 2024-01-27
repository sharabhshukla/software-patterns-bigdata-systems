from matchpredictor.matchresults.result import Fixture, Outcome
from matchpredictor.predictors.predictor import Prediction, Predictor


class AlphabetPredictor(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:
        if fixture.away_team.name[0] < fixture.home_team.name[0]:
            return Prediction(outcome=Outcome.AWAY)
        elif fixture.home_team.name[0] < fixture.away_team.name[0]:
            return Prediction(outcome=Outcome.HOME)
        else:
            return Prediction(outcome=Outcome.DRAW)