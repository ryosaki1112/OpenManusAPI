# app/service/flow_runner.py

import asyncio
import time

from app.agent.manus import Manus
from app.flow.flow_factory import FlowFactory, FlowType
from app.logger import logger


async def run_flow_with_prompt(prompt: str) -> str:
    agents = {
        "manus": Manus(),  # create()が不要な仕様前提
    }

    flow = FlowFactory.create_flow(
        flow_type=FlowType.PLANNING,
        agents=agents,
    )

    try:
        start_time = time.time()
        result = await asyncio.wait_for(
            flow.execute(prompt),
            timeout=3600,
        )
        elapsed_time = time.time() - start_time
        logger.info(f"Request processed in {elapsed_time:.2f} seconds")
        return result
    except asyncio.TimeoutError:
        logger.error("Flow execution timed out after 1 hour")
        return "Execution timed out. Try a simpler request."
    except Exception as e:
        logger.error(f"Flow execution error: {str(e)}")
        return f"Error occurred: {str(e)}"
