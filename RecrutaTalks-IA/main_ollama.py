from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from datetime import datetime

model = "qwen3.5:9b"
temperature = 0.7

def get_date():
    """Obtem a data atual"""
    return datetime.now().strftime("%Y-%m-%d")

llm = ChatOllama(model=model, temperature=temperature)

system_prompt = """
Você é um assistente útil e amigável. 
Você pode responder perguntas e realizar tarefas usando as ferramentas disponíveis. 
Use as ferramentas quando necessário para obter informações ou realizar ações. 
Seja claro e conciso em suas respostas.
"""

agent = create_agent(model=llm, tools=[get_date], system_prompt=system_prompt)
user_query = input("> ")
response = agent.invoke({"messages": [{"role": "user", "content": user_query}]})

print(response,"\n\n\n")
print(response['messages'][-1].content)