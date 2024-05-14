import os
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

db = SQLDatabase.from_uri(os.environ["DB_CONNECTION_STRING"])

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
