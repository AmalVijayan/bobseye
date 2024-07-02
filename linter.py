from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from prompt import RAG_PROMPT

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

class AILinter:
    def __init__(self, model_name):
        self._model = ChatOpenAI(model=model_name)
        self.results = []
        

    def lint_code_snippets_with_rag(self, inputs, retriever):
        ai_model_chain = self._create_rag_chain(retriever)
        self.results = self._process_inputs(inputs, ai_model_chain)

    def _create_rag_chain(self, retriever):
        rag_chain = (
            {"context": retriever | format_docs, "snippet": RunnablePassthrough()}
            | self._create_prompt_template()
            | self._model
            | StrOutputParser()
            )
        return rag_chain
    
    def _create_prompt_template(self):
        return ChatPromptTemplate.from_messages(
            [("system", RAG_PROMPT), ("user", "{snippet}"),]
        )

    def _process_inputs(self, inputs, ai_model_chain):
        return [ai_model_chain.invoke(input) for input in inputs]

    def write_results_to_file(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            for index, result in enumerate(self.results):
                file.write(f'snippet-{index + 1}, {result}\n')














                