from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompts = PromptTemplate(
    template="Generate 5 interesting facts about {Topic}",
    input_variables=["Topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

chain = prompts | model | parser
result = chain.invoke({"Topic": "football world cup 2026"})
print(result)

chain.get_graph().print_ascii()