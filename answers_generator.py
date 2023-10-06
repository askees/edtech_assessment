from generator import Generator

class AnswersGenerator(Generator):
    def __init__(self):
        super().__init__()

    def do(self, common_core_standard, rubric, passage, questions):
        params = {
            'common_core_standard': common_core_standard,
            'rubric': rubric,
            'passage': passage,
            'questions': questions
        }
        response = super().generate_json(
            './prompts/answers_system.txt',
            './prompts/answers_human_do.txt',
            params
        )
        return response

    def qc(self, common_core_standard, rubric, passage, questions, answers):
        params = {
            'common_core_standard': common_core_standard,
            'rubric': rubric,
            'passage': passage,
            'questions': questions,
            'answers': answers
        }
        response = super().generate_json(
            './prompts/answers_system.txt',
            './prompts/answers_human_qc.txt',
            params
        )
        return response
