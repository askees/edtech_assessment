import json
import unittest
from api import Api

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api = Api()
        self.common_core_standard = 'CCSS.ELA-LITERACY.W.4.9'
        self.topic_of_interest = 'baseball'

    @unittest.skip
    def test_rubric_qc_fail(self):
        rubric_qc = self.api.rubric_qc(self.common_core_standard, 'This should fail')
        self.assertEqual(rubric_qc['Outcome'], 'Fail')

    @unittest.skip
    def test_rubric_qc_pass(self):
        rubric_do = self.api.rubric_do(self.common_core_standard)
        rubric_qc = self.api.rubric_qc(self.common_core_standard, rubric_do)
        self.assertEqual(rubric_qc['Outcome'], 'Pass')
        #with open('./results/rubric.json', 'w', encoding='utf-8') as file:
        #    file.write(json.dumps(rubric_do))

    @unittest.skip
    def test_passage_qc_fail(self):
        passage_qc = self.api.passage_qc(self.common_core_standard, self.topic_of_interest, 100, 'This is a story about dogs.')
        self.assertEqual(passage_qc['Outcome'], 'Fail')

    @unittest.skip
    def test_passage_qc_pass(self):
        passage_do = self.api.passage_do(self.common_core_standard, self.topic_of_interest, 100)
        passage_qc = self.api.passage_qc(self.common_core_standard, self.topic_of_interest, 100, passage_do)
        self.assertEqual(passage_qc['Outcome'], 'Pass')
        #with open('./results/passage.json', 'w', encoding='utf-8') as file:
        #    file.write(json.dumps(passage_do))

    @unittest.skip
    def test_questions_qc_fail(self):
        questions_qc = self.api.questions_qc(self.common_core_standard, 'This is a story about dogs.', 3, 'These are bad questions.')
        self.assertEqual(questions_qc['Outcome'], 'Fail')

    @unittest.skip
    def test_questions_qc_pass(self):
        with open('./results/passage.json', 'r', encoding='utf-8') as file:
            passage = json.loads(file.read())
        questions_do = self.api.questions_do(self.common_core_standard, passage, 3)
        questions_qc = self.api.questions_qc(self.common_core_standard, passage, 3, questions_do)
        self.assertEqual(questions_qc['Outcome'], 'Pass')
        #with open('./results/questions.json', 'w', encoding='utf-8') as file:
        #    file.write(json.dumps(questions_do))
    
    @unittest.skip
    def test_answers_qc_fail(self):
        answers_qc = self.api.answers_qc(self.common_core_standard, 'This is a bad rubric.', 'This is a story about dogs.', 'These are bad questions.', 'These are bad answers.')
        self.assertEqual(answers_qc['Outcome'], 'Fail')

    @unittest.skip
    def test_answers_qc_pass(self):
        with open('./results/rubric.json', 'r', encoding='utf-8') as file:
            rubric = json.loads(file.read())
        with open('./results/passage.json', 'r', encoding='utf-8') as file:
            passage = json.loads(file.read())
        with open('./results/questions.json', 'r', encoding='utf-8') as file:
            questions = json.loads(file.read())
        answers_do = self.api.answers_do(self.common_core_standard, rubric, passage, questions)
        answers_qc = self.api.answers_qc(self.common_core_standard, rubric, passage, questions, answers_do)
        self.assertEqual(answers_qc['Outcome'], 'Pass')
        #with open('./results/answers.json', 'w', encoding='utf-8') as file:
        #    file.write(json.dumps(answers_do))

    @unittest.skip
    def test_feedback_qc_fail(self):
        feedback_qc = self.api.feedback_qc(self.common_core_standard, 'This is a bad rubric.', 'This is a story about dogs.', 'These are bad answers.', 'This is bad feedback.')
        self.assertEqual(feedback_qc['Outcome'], 'Fail')

    def test_feedback_qc_pass(self):
        with open('./results/rubric.json', 'r', encoding='utf-8') as file:
            rubric = json.loads(file.read())
        with open('./results/passage.json', 'r', encoding='utf-8') as file:
            passage = json.loads(file.read())
        with open('./results/answers.json', 'r', encoding='utf-8') as file:
            answers = json.loads(file.read())
        feedback_do = self.api.feedback_do(self.common_core_standard, rubric, passage, answers)
        feedback_qc = self.api.feedback_qc(self.common_core_standard, rubric, passage, answers, feedback_do)
        self.assertEqual(feedback_qc['Outcome'], 'Pass')
        #with open('./results/feedback.json', 'w', encoding='utf-8') as file:
        #    file.write(json.dumps(feedback_do))

if __name__ == "__main__":
    unittest.main()
