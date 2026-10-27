"""
LLM 客户端封装
统一对接 OpenAI 兼容协议的大模型接口，支持流式与非流式调用
"""
from typing import List, Dict, Generator, Optional
from openai import OpenAI

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config


class LLMClient:
    """大语言模型客户端"""

    def __init__(self, llm_config=None):
        cfg = llm_config or config.llm
        self.client = OpenAI(
            base_url=cfg.base_url,
            api_key=cfg.api_key or "sk-placeholder",  # 占位，避免初始化报错
            timeout=cfg.timeout,
        )
        self.model = cfg.model
        self.temperature = cfg.temperature
        self.max_tokens = cfg.max_tokens

    def chat(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
    ) -> str:
        """
        非流式对话，返回完整回复文本
        :param messages: 消息列表 [{"role": "user"/"assistant", "content": "..."}]
        :param system_prompt: 系统提示词（可选，会插入到消息最前面）
        """
        full_messages = []
        if system_prompt:
            full_messages.append({"role": "system", "content": system_prompt})
        full_messages.extend(messages)

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=full_messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"[LLM 调用失败] {e}\n请检查 config.py 中的 API 配置（base_url / api_key / model）。"

    def chat_stream(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
    ) -> Generator[str, None, None]:
        """
        流式对话，逐段 yield 回复内容
        """
        full_messages = []
        if system_prompt:
            full_messages.append({"role": "system", "content": system_prompt})
        full_messages.extend(messages)

        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=full_messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield delta
        except Exception as e:
            yield f"\n[LLM 调用失败] {e}\n请检查 config.py 中的 API 配置。"


# 全局单例
llm_client = LLMClient()
