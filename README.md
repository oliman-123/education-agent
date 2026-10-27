# 📚 教育教学智能体

一个基于大语言模型的教育教学智能体 Demo，集成**答疑辅导、知识点讲解、学习计划、测验出题**四大教学模块，支持命令行和 Web 两种交互方式。

## ✨ 功能模块

| 模块 | 说明 |
|---|---|
| 🎯 答疑辅导 | 启发式苏格拉底提问，引导学生自己找到答案，不直接灌输 |
| 📖 知识点讲解 | 按"定义→原理→例子→误区→总结"结构系统化讲解任意知识点 |
| 📅 学习计划 | 根据目标、可用时间和当前水平，生成分阶段可执行的个性化计划 |
| ✏️ 测验出题 | 按学科/知识点/难度自动生成 5 道题（选择+简答），支持对答案 |

## 📁 项目结构

```
education_agent/
├── main.py              # 命令行入口
├── web_app.py           # Streamlit Web 界面
├── config.py            # 全局配置（API、模型、教学风格）
├── requirements.txt     # Python 依赖
├── agent/                # 智能体核心
│   ├── base_agent.py        # 抽象基类
│   ├── education_agent.py  # 主控制器（菜单路由）
│   ├── tutor_agent.py       # 答疑辅导
│   ├── lesson_agent.py       # 知识点讲解
│   ├── planner_agent.py      # 学习计划
│   ├── quiz_agent.py         # 测验出题
│   └── memory.py            # 对话记忆（滑动窗口）
├── utils/
│   └── llm_client.py     # LLM API 封装（兼容 OpenAI 协议）
└── knowledge/            # 课程知识库（可扩展为 RAG）
    └── sample_notes.md
```

## 🚀 快速开始

### 1. 安装依赖

```bash
cd education_agent
pip install -r requirements.txt
```

### 2. 配置大模型 API

编辑 `config.py`，或设置环境变量：

```bash
# Windows PowerShell
$env:LLM_BASE_URL = "https://api.openai.com/v1"
$env:LLM_API_KEY = "sk-你的key"
$env:LLM_MODEL = "gpt-3.5-turbo"
```

> 💡 本项目兼容所有 OpenAI 协议接口，可换成 DeepSeek、通义千问、本地 Ollama 等，只需改 `base_url` 和 `model`。

### 3. 运行命令行版

```bash
python main.py
```

启动后会看到菜单，输入数字切换模块，输入问题即可开始对话。

### 4. 运行 Web 版

```bash
streamlit run web_app.py
```

浏览器会自动打开，界面更友好，支持流式输出和侧边栏切换。

## 🎮 使用示例

**答疑辅导模式：**
```
[答疑辅导] 你：一元二次方程求根公式是什么？
[答疑辅导] AI：很好的问题！在告诉你公式之前，先想一想：
 你知道一元二次方程的一般形式是什么吗？它有几个系数？
 ...（引导你回忆 a、b、c 三个系数）
```

**知识点讲解模式：**
```
[知识点讲解] 你：讲一下牛顿第二定律
[知识点讲解] AI：
 ## 一、概念定义
 牛顿第二定律描述的是：物体加速度的大小跟作用力成正比...
 ## 二、核心原理
 ...
```

## 🔧 自定义扩展

- **修改教学风格**：在 `config.py` 中把 `teaching_style` 改成 `"严谨"` / `"活泼"` / `"幽默"` 等
- **新增智能体**：继承 `BaseTeachingAgent`，写好 `system_prompt` 和 `description()`，再注册到 `EducationAgent.AGENTS` 字典
- **接入知识库（RAG）**：在 `knowledge/` 目录放笔记，改造 `llm_client` 增加向量检索召回，把相关笔记拼进 system_prompt
- **调整记忆长度**：修改 `config.py` 里的 `memory_window`

## 📝 说明

- 本项目是教学演示用的代码框架，重点展示"多智能体分工 + 对话记忆 + 教学提示词工程"的思路
- 生产环境使用建议：接入真实数据库做长期记忆、增加教师端批改界面、加入权限管理
