from generator import Generator

class FeedbackGenerator(Generator):
    ''' This class generates feedback for a given common core standard, rubric, passage, and answers. '''

    def __init__(self):
        super().__init__()

    def do(self, common_core_standard, rubric, passage, answers):
        params = {
            'common_core_standard': common_core_standard,
            'rubric': rubric,
            'passage': passage,
            'answers': answers
        }
        response = super().generate_json(
            './prompts/feedback_system.txt',
            './prompts/feedback_human_do.txt',
            params
        )
        return response

    def qc(self, common_core_standard, rubric, passage, answers, feedback):
        params = {
            'common_core_standard': common_core_standard,
            'rubric': rubric,
            'passage': passage,
            'answers': answers,
            'feedback': feedback
        }
        response = super().generate_json(
            './prompts/feedback_system.txt',
            './prompts/feedback_human_qc.txt',
            params
        )
        return response