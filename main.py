import asyncio
from typing import Any
from client.llm_client import LLMClient
import click

async def run(messages: dict[str, Any]) -> None:

@click.command()
@click.argument("prompt", required=False)
def main(prompt: str | None = None):
    client = LLMClient()
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    async for event in client.chat_completion(messages, stream=True):
        print(event)
    print("Hello from sovereign-agents!")


if __name__ == "__main__":
    asyncio.run(main())
