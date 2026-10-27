"""
智能体基类
定义所有教学智能体的公共接口
"""
from abc import ABC, abstractmethod
from typing import Optional

from utils.llm_client import llm_client
from agent.memory import ConversationMemory
from config import config


class BaseTeachingAgent(ABC):
    """教学智能体抽象基类"""

    # 子类覆盖：智能体名称
    name: str = "BaseAgent"
    # 子类覆盖：系统提示词
    system_prompt: str = ""

    def __init__(self, style: Optional[str] = None):
        self.memory = ConversationMemory(window=config.memory_window)
        self.style = style or config.teaching_style
        # 子类可在 init 后再修改 system_prompt
        self.llm = llm_client

    def _build_system_prompt(self) -> str:
        """组装最终系统提示词，注入教学风格"""
        style_hint = f"\n教学风格要求：{self.style}。"
        return self.system_prompt + style_hint

    def chat(self, user_input: str) -> str:
        """
        单轮对话入口：加入记忆 → 调用 LLM → 保存回复
        """
        self.memory.add_user(user_input)
        reply = self.llm.chat(
            messages=self.memory.get_messages(),
            system_prompt=self._build_system_prompt(),
        )
        self.memory.add_assistant(reply)
        return reply

    def chat_stream(self, user_input: str):
        """流式对话入口（生成器）"""
        self.memory.add_user(user_input)
        collected = []
        for delta in self.llm.chat_stream(
            messages=self.memory.get_messages(),
            system_prompt=self._build_system_prompt(),
        ):
            collected.append(delta)
            yield delta
        self.memory.add_assistant("".join(collected))

    def reset(self):
        """清空对话记忆"""
        self.memory.clear()

    @abstractmethod
    def description(self) -> str:
        """返回该智能体的功能描述（用于主菜单展示）"""
        ...
