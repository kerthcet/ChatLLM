from typing import List

from llms.chat import SYSTEM_PROMPT
from apis.messages import ChatMessage
from utils.log import LOGGER


def general_validations(
    messages: List[ChatMessage], support_system_prompt: bool
) -> bool:
    if len(messages) == 0:
        LOGGER.error("no prompt provided")
        return False

    if messages[0].role == SYSTEM_PROMPT and not support_system_prompt:
        LOGGER.error("system prompt not supported")
        return False

    return True