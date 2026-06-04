# memory/learnings.md: 知识与学习积累

本文件记录在各个任务中学到的、可复用的知识、技巧和洞察。

格式：`[日期] 任务或主题: 具体内容`

---

## GitHub Copilot & OpenClaw

### [2026-06-04] 个人 AI 助手框架设计
**学到的**：
- OpenClaw 框架的核心是将 AI 变成"能做事"的助手，而不仅仅是回答问题
- 三层架构（身份层、记忆层、工作层）能有效支持跨对话的持久化
- 文件系统是比对话历史更可靠的记忆来源
- GitHub 仓库天然适合作为长期工作空间：支持文件版本控制、issue 追踪、协作

**应用**：
- 使用 AGENTS.md 作为核心框架文件
- 建立 memory/ 文件夹存储持久知识
- 每个任务完成后立即更新记忆文件并 commit
- 在新对话开始时自动读取框架文件，恢复身份和上下文

---

## GitHub API & 工具链

### [2026-06-04] GitHub Copilot 可用工具
**可用能力**：
- `getfile` - 读取仓库中的单个文件
- `create_or_update_file` - 创建或更新文件（需要 sha 参数更新现有文件）
- `push_files` - 批量推送多个文件到分支
- `create_branch` - 创建新分支
- `get-github-data` - 调用 GitHub REST API
- `lexical-code-search` - 精确符号和文本搜索
- `semantic-code-search` - 语义代码搜索
- `get-actions-job-logs` - 获取 workflow 日志

**最佳实践**：
- 创建多个文件时用 `push_files` 比逐个 `create_or_update_file` 高效
- 跨对话恢复身份时，优先用 `getfile` 读取 AGENTS.md、SOUL.md、WORK_LOG.md
- 更新现有文件前，用 `getfile` 获取当前内容和 sha

---

## （后续任务会继续补充）
