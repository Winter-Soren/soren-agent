from typing import AsyncGenerator

from agent.events import AgentEvent
from client.llm_client import LLMClient
from client.responses import StreamEventType


class Agent:
    def __init__(self):
        self.client = LLMClient()

    async def _agentic_loop(self, ) -> AsyncGenerator[AgentEvent, None]:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]
        async for event in self.client.chat_completion(messages, stream=True):
            if event.type == StreamEventType.TEXT_DELTA:
                content = event.text_delta.content
                yield AgentEvent.text_delta(content)
            elif event.type == StreamEventType.ERROR:
                yield AgentEvent.agent_error(event.error)