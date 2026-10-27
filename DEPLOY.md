# 🌐 部署到公网（外网访问）指南

## 方案：Streamlit Community Cloud（免费）

部署后你会得到一个 `https://你的项目名.streamlit.app` 的公网链接，任何人都能打开。

---

## 准备工作（只需一次）

### 第一步：注册 GitHub 账号

如果没有 GitHub，先去注册：
```
https://github.com/signup
```
用邮箱注册就行，免费。

### 第二步：上传项目到 GitHub

1. 登录 GitHub，点右上角「+」→「New repository」
2. 仓库名填 `education-agent`，选 Public（公开）
3. 点「Create repository」
4. 选择「uploading an existing file」
5. 把 `education_agent` 文件夹里的**所有文件**拖进去上传
   - 注意：上传的是文件夹**里面的内容**，不是文件夹本身
   - 确保 `web_app.py`、`config.py`、`requirements.txt` 在根目录
6. 点「Commit changes」

---

## 部署到 Streamlit Cloud

### 第三步：打开 Streamlit Cloud

访问：
```
https://share.streamlit.io/
```

点「Sign in」，用你的 GitHub 账号登录。

### 第四步：部署应用

1. 点「New app」
2. Repository 选你刚建的 `你的用户名/education-agent`
3. Branch 选 `main`
4. Main file 选 `web_app.py`
5. 点「Deploy!」

等 1-2 分钟，部署完成后你会看到：
```
https://education-agent-xxxx.streamlit.app
```

这个链接就是公网地址，发给任何人都能打开。

---

## ⚠️ 注意事项

1. **API Key 安全**：公网暴露后，任何人都能用你的 API 额度。建议：
   - 不要把链接发给太多人
   - 或者在 `config.py` 里限制每日调用次数
   - 用完就去 Streamlit Cloud 把 app 停掉

2. **免费额度**：Streamlit Cloud 免费版每个月有一定时长限制，个人用足够。

3. **休眠机制**：15 分钟没人访问会自动休眠，再打开需要等几秒钟唤醒，正常现象。

---

## 如果你不想用 GitHub

也可以用其他方式（需要命令行操作）：
- **ngrok**：注册后下载客户端，运行 `ngrok http 8501` 得到临时链接
- **Cloudflare Tunnel**：免费，不需要注册，运行后得到临时域名

需要哪种方式告诉我，我带你操作。
