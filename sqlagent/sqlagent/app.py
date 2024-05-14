from typing import Any

from fastapi import FastAPI

from langchain.pydantic_v1 import BaseModel
from langserve import add_routes


from sqlagent.main import agent_executor

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using LangChain's Runnable interfaces",
)


# We need to add these input/output schemas because the current AgentExecutor
# is lacking in schemas.
class Input(BaseModel):
    input: str


class Output(BaseModel):
    output: Any


# Adds routes to the app for using the chain under:
# /invoke
# /batch
# /stream
# /stream_events
add_routes(app, agent_executor, input_type=Input, output_type=Output)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
