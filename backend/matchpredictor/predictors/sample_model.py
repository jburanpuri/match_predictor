from matchpredictor.matchresults.result import Fixture, Outcome
from matchpredictor.predictors.predictor import Prediction, Predictor


class SampleModel(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:
        if Outcome.HOME > Outcome.AWAY:
            return Prediction(outcome=Outcome.HOME)

        else:
            return Prediction(outcome=Outcome.AWAY)
