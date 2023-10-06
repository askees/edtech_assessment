from generator import Generator

class RubricGenerator(Generator):
    def __init__(self):
        super().__init__()

    def do(self, common_core_standard):
        params = {
            'common_core_standard': common_core_standard
        }
        response = super().generate_json(
            './prompts/rubric_system.txt',
            './prompts/rubric_human_do.txt',
            params
        )
        return response

    def qc(self, common_core_standard, rubric):
        params = {
            'common_core_standard': common_core_standard,
            'rubric': rubric
        }
        response = super().generate_json(
            './prompts/rubric_system.txt',
            './prompts/rubric_human_qc.txt',
            params
        )
        return response
