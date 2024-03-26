from unittest import TestCase

from matchpredictor.matchresults.results_provider import validation_results
from matchpredictor.evaluation.evaluator import Evaluator
from matchpredictor.predictors.sample_model import SampleModel
from test.predictors import csv_location


class TestSamplePredictor(TestCase):
    def test_accuracy(self) -> None:
        validation_data = validation_results(csv_location, 2019)
        accuracy, _ = Evaluator(
            SampleModel()).measure_accuracy(validation_data)

        self.assertGreaterEqual(accuracy, .33)
