"""
测验生成智能体
根据学科、知识点和难度，生成选择题/简答题并附答案解析
"""
from agent.base_agent import BaseTeachingAgent


class QuizAgent(BaseTeachingAgent):
    name = "测验出题"
    system_prompt = """你是一位经验丰富的命题老师。
你的职责：
1. 根据学生指定的学科、知识点和难度（简单/中等/困难），生成 5 道测验题。
2. 题型混合：至少 3 道选择题（含 A/B/C/D 四个选项）+ 2 道简答题。
3. 每道题后面先不要给答案，等学生说"对答案"时再统一给出答案和详细解析。
4. 题目要考察理解和应用，不要出死记硬背的偏题怪题。
5. 难度要与学生要求一致。
"""

    def description(self) -> str:
        return "按学科/知识点/难度自动生成 5 道测验题（选择+简答），支持后续对答案。"
