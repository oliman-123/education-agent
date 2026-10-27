"""
教育教学智能体 - Web 界面（Streamlit）
运行方式：streamlit run web_app.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from agent.education_agent import EducationAgent


st.set_page_config(page_title="教育教学智能体", page_icon="📚", layout="wide")


def init_agent():
    if "edu_agent" not in st.session_state:
        st.session_state.edu_agent = EducationAgent()


def main():
    init_agent()
    agent: EducationAgent = st.session_state.edu_agent

    st.title("📚 教育教学智能体")
    st.caption("答疑辅导 · 知识点讲解 · 学习计划 · 测验出题")

    # 侧边栏：模块选择
    with st.sidebar:
        st.header("功能模块")
        options = {f"{k}. {v.name}": k for k, v in agent.agents.items()}
        current_label = f"{agent.current_key}. {agent.current.name}"
        selected_label = st.radio(
            "选择模块",
            options=list(options.keys()),
            index=list(options.keys()).index(current_label),
        )
        agent.switch(options[selected_label])

        st.divider()
        st.write(f"**当前模块：** {agent.current.name}")
        st.info(agent.current.description())

        if st.button("🗑️ 清空当前对话"):
            agent.current.reset()
            st.rerun()

    # 主区域：对话历史
    for msg in agent.current.memory.get_messages():
        with st.chat_message("user" if msg["role"] == "user" else "assistant"):
            st.markdown(msg["content"])

    # 输入框
    user_input = st.chat_input("输入你的问题或需求...")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            placeholder = st.empty()
            collected = ""
            for delta in agent.current.chat_stream(user_input):
                collected += delta
                placeholder.markdown(collected + "▌")
            placeholder.markdown(collected)


if __name__ == "__main__":
    main()
