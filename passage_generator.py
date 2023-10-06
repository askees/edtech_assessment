from generator import Generator

class PassageGenerator(Generator):
    ''' This class generates a passage for a given common core standard and topic of interest. '''

    def __init__(self):
        super().__init__()

    def do(self, common_core_standard, topic_of_interest, number_of_words):
        params = {
            'common_core_standard': common_core_standard,
            'topic_of_interest': topic_of_interest,
            'number_of_words': number_of_words
        }
        response = super().generate_json(
            './prompts/passage_system.txt',
            './prompts/passage_human_do.txt',
            params
        )
        return response

    def qc(self, common_core_standard, topic_of_interest, number_of_words, passage):
        params = {
            'common_core_standard': common_core_standard,
            'topic_of_interest': topic_of_interest,
            'number_of_words': number_of_words,
            'passage': passage
        }
        response = super().generate_json(
            './prompts/passage_system.txt',
            './prompts/passage_human_qc.txt',
            params
        )
        return response

