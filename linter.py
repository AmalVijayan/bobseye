from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from prompt import SYSTEM_PROMPT

class AILinter:
    def __init__(self, model_name):
        self._model = ChatOpenAI(model=model_name)
        self.results = []

    def lint_code_snippets(self, inputs):
        ai_model_chain = self._create_ai_model_chain()
        self.results = self._process_inputs(inputs, ai_model_chain)

    def _create_ai_model_chain(self):
        prompt_template = self._create_prompt_template()
        parser = StrOutputParser()
        chained_model = prompt_template | self._model | parser
        return chained_model

    def _create_prompt_template(self):
        return ChatPromptTemplate.from_messages(
            [("system", SYSTEM_PROMPT), ("user", "{snippet}")]
        )

    def _process_inputs(self, inputs, ai_model_chain):
        return [ai_model_chain.invoke(input) for input in inputs]

    def write_results_to_file(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            for index, result in enumerate(self.results):
                file.write(f'snippet-{index + 1}, {result}\n')














                