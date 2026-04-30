from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompts1 = PromptTemplate(
    template="Generate a detailed report on {Topic}",
    input_variables=["Topic"]
)
prompts2 = PromptTemplate(
    template="Generate a 5 pointer Summary from the following text\n {text}",
    input_variables=["text"]
)

model = ChatOpenAI()
parser = StrOutputParser()

chain = prompts1 | model | parser | prompts2 | model | parser
result = chain.invoke({"Topic": "Unemployment in India"})

print(result)

# chain.get_graph().print_ascii()  # Requires grandalf package