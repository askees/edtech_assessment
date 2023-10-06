from generator import Generator

class QuestionsGenerator(Generator):
    def __init__(self):
        super().__init__()

    def do(self, common_core_standard, passage, number_of_questions):
        params = {
            'common_core_standard': common_core_standard,
            'passage': passage,
            'number_of_questions': number_of_questions
        }
        response = super().generate_json(
            './prompts/questions_system.txt',
            './prompts/questions_human_do.txt',
            params
        )
        return response

    def qc(self, common_core_standard, passage, number_of_questions, questions):
        params = {
            'common_core_standard': common_core_standard,
            'passage': passage,
            'number_of_questions': number_of_questions,
            'questions': questions
        }
        response = super().generate_json(
            './prompts/questions_system.txt',
            './prompts/questions_human_qc.txt',
            params
        )
        return response
