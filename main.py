"""
教育教学智能体 - 命令行入口
运行方式：python main.py
"""
import sys
import os

# 确保项目根目录在 sys.path 中
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent.education_agent import EducationAgent


def main():
    agent = EducationAgent()
    print(agent.menu_text())

    while True:
        try:
            user_input = input(f"\n[{agent.current.name}] 你：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！祝你学习顺利～")
            break

        if not user_input:
            continue

        # 命令处理
        if user_input.lower() == "q":
            print("再见！祝你学习顺利～")
            break
        if user_input.lower() == "r":
            agent.current.reset()
            print(f"[已清空「{agent.current.name}」的对话记录]")
            continue
        if user_input in agent.agents:
            agent.switch(user_input)
            print(agent.menu_text())
            continue

        # 正常对话（流式输出）
        print(f"[{agent.current.name}] AI：", end="", flush=True)
        for delta in agent.current.chat_stream(user_input):
            print(delta, end="", flush=True)
        print()


if __name__ == "__main__":
    main()
