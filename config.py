"""
教育教学智能体 - 全局配置
支持通过环境变量或 .env 文件覆盖默认值
"""
import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LLMConfig:
    """大语言模型配置"""
    # API 基础地址（DeepSeek 开放平台）
    base_url: str = field(default_factory=lambda: os.getenv("LLM_BASE_URL", "https://api.deepseek.com"))
    # API Key
    api_key: str = field(default_factory=lambda: os.getenv("LLM_API_KEY", "sk-e6b526be5eda4264a02acaf90551c71c"))
    # 模型名称（DeepSeek-Chat 通用对话模型）
    model: str = field(default_factory=lambda: os.getenv("LLM_MODEL", "deepseek-chat"))
    # 生成参数
    temperature: float = 0.7
    max_tokens: int = 2048
    # 请求超时（秒）
    timeout: int = 60


@dataclass
class AgentConfig:
    """智能体全局配置"""
    llm: LLMConfig = field(default_factory=LLMConfig)
    # 对话记忆窗口（保留最近 N 轮对话）
    memory_window: int = 10
    # 知识库目录
    knowledge_dir: str = os.path.join(os.path.dirname(__file__), "knowledge")
    # 默认教学风格：严谨 / 活泼 / 启发式
    teaching_style: str = "启发式"


# 全局单例
config = AgentConfig()
