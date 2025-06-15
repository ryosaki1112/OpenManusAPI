# app/service/agent_runner.py

from app.agent.manus import Manus
from app.logger import logger

async def process_prompt(prompt: str) -> str:
    agent = await Manus.create()
    try:
        logger.info(f"Running agent with prompt: {prompt}")
        result = await agent.run(prompt)
        logger.info("Agent run complete")
        return result
    finally:
        await agent.cleanup()
