"""
对话记忆模块
维护多轮对话历史，支持窗口截断
"""
from collections import deque
from typing import List, Dict


class ConversationMemory:
    """对话记忆（滑动窗口）"""

    def __init__(self, window: int = 10):
        """
        :param window: 保留最近 N 轮对话（一轮 = 一问一答）
        """
        self.window = window
        # 用 deque 保存消息，每条是 {"role": ..., "content": ...}
        self._messages: deque = deque(maxlen=window * 2)  # 每轮两条消息

    def add_user(self, content: str):
        self._messages.append({"role": "user", "content": content})

    def add_assistant(self, content: str):
        self._messages.append({"role": "assistant", "content": content})

    def get_messages(self) -> List[Dict[str, str]]:
        return list(self._messages)

    def clear(self):
        self._messages.clear()

    def __len__(self):
        return len(self._messages)
