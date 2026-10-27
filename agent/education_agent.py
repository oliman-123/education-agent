"""
教育教学智能体 - 主控制器
统一管理四个子智能体，提供菜单式切换
"""
from typing import Dict, Type

from agent.base_agent import BaseTeachingAgent
from agent.tutor_agent import TutorAgent
from agent.lesson_agent import LessonAgent
from agent.quiz_agent import QuizAgent
from agent.planner_agent import PlannerAgent


class EducationAgent:
    """教育教学智能体主入口"""

    # 子智能体注册表
    AGENTS: Dict[str, Type[BaseTeachingAgent]] = {
        "1": TutorAgent,
        "2": LessonAgent,
        "3": PlannerAgent,
        "4": QuizAgent,
    }

    def __init__(self):
        # 实例化所有子智能体（每个有独立记忆）
        self.agents: Dict[str, BaseTeachingAgent] = {
            key: cls() for key, cls in self.AGENTS.items()
        }
        self.current_key: str = "1"  # 默认选中答疑辅导

    @property
    def current(self) -> BaseTeachingAgent:
        return self.agents[self.current_key]

    def switch(self, key: str):
        """切换当前子智能体"""
        if key in self.agents:
            self.current_key = key
            return True
        return False

    def menu_text(self) -> str:
        """生成主菜单文本"""
        lines = ["=" * 40, "  📚 教育教学智能体", "=" * 40]
        for key, agent in self.agents.items():
            marker = "👉" if key == self.current_key else "  "
            lines.append(f"{marker} {key}. {agent.name}")
            lines.append(f"      {agent.description()}")
        lines.append("-" * 40)
        lines.append("输入数字切换模块，输入 r 清空当前对话，输入 q 退出")
        return "\n".join(lines)
