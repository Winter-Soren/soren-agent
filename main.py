import asyncio
from client.llm_client import LLMClient


async def main():
    client = LLMClient()
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    async for event in client.chat_completion(messages, stream=False):
        print(event)
    print("Hello from sovereign-agents!")


if __name__ == "__main__":
    asyncio.run(main())
