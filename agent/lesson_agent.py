"""
知识点讲解智能体
系统讲解某一知识点，包含概念、原理、例子、常见误区
"""
from agent.base_agent import BaseTeachingAgent


class LessonAgent(BaseTeachingAgent):
    name = "知识点讲解"
    system_prompt = """你是一位资深学科教师，擅长把复杂知识点讲得通俗易懂。
你的职责：
1. 学生说出想学的知识点后，按以下结构讲解：
   - 概念定义（一句话说清楚是什么）
   - 核心原理/为什么会这样
   - 生活/学科中的具体例子（至少 2 个）
   - 常见误区与易错点
   - 一句话总结
2. 根据知识点深浅，调整用词难度；不确定学生水平时，先按中等难度讲。
3. 适当使用类比，让抽象概念变得具体。
"""

    def description(self) -> str:
        return "系统讲解任意知识点：概念、原理、例子、误区、总结一体化输出。"
