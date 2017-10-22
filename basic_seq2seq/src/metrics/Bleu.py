from nltk.translate import bleu_score
from datetime import datetime
import os


class Bleu:
    def __init__(self, model):
        self.model = model
        self.hypothesis_reference = {
            'hyp': None,
            'ref': None
            }
        self.hypothesis = ''
        self.references = []

        self.BLEU_RESULT_DIR = '../../../evaluations/' + self.model
        if not os.path.exists(self.BLEU_RESULT_DIR):
            os.mkdir(self.BLEU_RESULT_DIR)
        self.FILE_NAME = model + '_' + datetime.strftime(datetime.now(), "%Y%m%d_%H-%M-%S") + '.txt'
        self.FILE_PATH = self.BLEU_RESULT_DIR + '/' + self.FILE_NAME

    def evaluate_single_hypothesis(self, hypothesis: str, references: list):
        """
        Evaluates predictions via the bleu score metric
        :param references: A list of references against which the predicted string is measured. If only one reference
        is available this method accepts it as a string and converts it to a single-item list
        :param hypothesis: The predicted string(s)
        :type hypothesis: list
        :type references: list
        """
        self.hypothesis = hypothesis
        self.references = references
        if not type(self.references) == list:
            self.references = [self.references]
        self.hypothesis_reference['hyp'] = self.hypothesis
        self.hypothesis_reference['ref'] = self.references
        with open(self.FILE_PATH, 'w') as file:
            print('Score: {:.12f} \t Hypothesis: {} \t Reference(s): {}'.
                  format(bleu_score.sentence_bleu(hypothesis=self.hypothesis_reference['hyp'],
                                                  references=self.hypothesis_reference['ref']),
                         self.hypothesis, self.references), file=file)
