from rubric_generator import RubricGenerator
from passage_generator import PassageGenerator
from questions_generator import QuestionsGenerator
from answers_generator import AnswersGenerator
from feedback_generator import FeedbackGenerator

class Api:
    ''' This class is the API for the system. It is the only class that should be called from outside the system. '''
    
    def __init__(self):
        self.rubric_generator = RubricGenerator()
        self.passage_generator = PassageGenerator()
        self.questions_generator = QuestionsGenerator()
        self.answers_generator = AnswersGenerator()
        self.feedback_generator = FeedbackGenerator()

    def rubric_do(self, common_core_standard):
        return self.rubric_generator.do(common_core_standard)

    def rubric_qc(self, common_core_standard, rubric):
        return self.rubric_generator.qc(common_core_standard, rubric)

    def passage_do(self, common_core_standard, topic_of_interest, number_of_words):
        return self.passage_generator.do(common_core_standard, topic_of_interest, number_of_words)

    def passage_qc(self, common_core_standard, topic_of_interest, number_of_words, passage):
        return self.passage_generator.qc(common_core_standard, topic_of_interest, number_of_words, passage)

    def questions_do(self, common_core_standard, passage, number_of_questions):
        return self.questions_generator.do(common_core_standard, passage, number_of_questions)

    def questions_qc(self, common_core_standard, passage, number_of_questions, questions):
        return self.questions_generator.qc(common_core_standard, passage, number_of_questions, questions)

    def answers_do(self, common_core_standard, rubric, passage, questions):
        return self.answers_generator.do(common_core_standard, rubric, passage, questions)

    def answers_qc(self, common_core_standard, rubric, passage, questions, answers):
        return self.answers_generator.qc(common_core_standard, rubric, passage, questions, answers)

    def feedback_do(self, common_core_standard, rubric, passage, answers):
        return self.feedback_generator.do(common_core_standard, rubric, passage, answers)

    def feedback_qc(self, common_core_standard, rubric, passage, answers, feedback):
        return self.feedback_generator.qc(common_core_standard, rubric, passage, answers, feedback)

