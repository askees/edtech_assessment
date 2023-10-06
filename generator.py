import os
import json
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

class Generator:
    ''' This class is the base class for all generators. '''
    
    def __init__(self):
        ''' The .env file should contain OPENAI_API_KEY=<key> '''
        with open('.env', 'r', encoding='utf-8') as file:
            for line in file:
                env_vars = line.strip().split('=')
                os.environ[env_vars[0]] = env_vars[1]

    def generate_json(self, system_prompt_file, human_prompt_file, params):
        ''' This prototype assumes a single system prompt and a single human prompt. '''
        with open(system_prompt_file, 'r', encoding='utf-8') as file:
            system_template = file.read()
        with open(human_prompt_file, 'r', encoding='utf-8') as file:
            human_do_template = file.read()

        chat_prompt = ChatPromptTemplate.from_messages([
            ('system', system_template),
            ('human', human_do_template)
        ])
        openai = ChatOpenAI(model_name='gpt-4')
        parser = StrOutputParser()
        chain = chat_prompt | openai | parser
        response = chain.invoke(params)
        response_json = json.loads(response)
        return response_json

    def do(self):
        ''' Each generator should implement their do method. This should generate the response. '''
        raise NotImplementedError

    def qc(self):
        ''' Each generator should implement their qc method. This should validate the response meets the quality bar. '''
        raise NotImplementedError
