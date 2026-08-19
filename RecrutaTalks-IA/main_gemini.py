from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from datetime import datetime

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
model = "gemini-3.5-flash"
temperature = 0.7

def get_date():
    """Obtem a data atual"""
    return datetime.now().strftime("%Y-%m-%d")

llm = ChatGoogleGenerativeAI(model=model, temperature=temperature, api_key=GOOGLE_API_KEY)

system_prompt = """
Você é um assistente útil e amigável. Você pode responder perguntas e realizar tarefas usando as ferramentas disponíveis. 
Use as ferramentas quando necessário para obter informações ou realizar ações. Seja claro e conciso em suas respostas.
"""

agent = create_agent(model=llm, tools=[get_date], system_prompt=system_prompt)
user_query = input("> ")
response = agent.invoke({"messages": [{"role": "user", "content": user_query}]})

print(response['messages'][-1].content[0]['text'])