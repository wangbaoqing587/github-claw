# memory/tools.md: 工具、API 与命令清单

本文件汇总已验证可用的工具、API、命令和他们的最佳用法。

---

## GitHub Copilot 技能 (Skills)

### 文件操作

| 工具 | 功能 | 最佳用法 |
|------|------|--------|
| `getfile` | 读取单个文件 | 快速查看现有文件内容，获取 sha |
| `create_or_update_file` | 创建/更新单个文件 | 更新现有文件（需要 sha），创建单个文件 |
| `push_files` | 批量推送文件 | 一次提交多个文件变更（高效） |
| `create_branch` | 创建新分支 | 隔离较大的功能开发 |

### 数据查询

| 工具 | 功能 | 最佳用法 |
|------|------|--------|
| `get-github-data` | GitHub REST API 查询 | 获取仓库信息、issue、PR、commit 等元数据 |
| `get-actions-job-logs` | 获取 workflow 日志 | 调试失败的 GitHub Actions |
| `semantic-code-search` | 语义代码搜索 | 按功能意图搜索相关代码 |
| `lexical-code-search` | 精确符号搜索 | 查找特定函数、类、变量 |

### 问题追踪

| 工具 | 功能 | 最佳用法 |
|------|------|--------|
| `github-issue` | 创建/管理 issue | 创建任务 issue，更新状态，管理关系 |
| `semantic_issues_search` | 语义 issue 搜索 | 按概念查找相关 issue |

---

## 常用 GitHub REST API 端点

### 仓库操作

```
GET    /repos/{owner}/{repo}                      # 仓库信息
POST   /repos/{owner}/{repo}/issues              # 创建 issue
GET    /repos/{owner}/{repo}/issues              # 列出 issue
POST   /repos/{owner}/{repo}/contents/{path}    # 创建文件
PUT    /repos/{owner}/{repo}/contents/{path}    # 更新文件
DELETE /repos/{owner}/{repo}/contents/{path}    # 删除文件
```

---

## Git 命令速查（参考）

**注意**：在 GitHub Copilot 中，文件操作优先使用 Copilot Skills，而非直接 git 命令。

```bash
# 本地 Git 流程（如需要）
git status                              # 查看状态
git add <file>                          # 暂存文件
git commit -m "[YYYY-MM-DD] message"   # 提交
git push origin <branch>                # 推送
```

---

## Markdown 与文档

### 推荐格式

- **标题**：使用 `#`、`##`、`###` 等（遵循层级）
- **代码块**：使用三反引号和语言标识符
- **列表**：无序列表用 `-`，有序列表用 `1.`
- **表格**：使用 `|` 分隔符
- **链接**：`[文本](URL)` 格式

### 文件头模板

```markdown
# memory/xxx.md: 简洁说明

本文件记录...

格式：...

---
```

---

## 快速参考

### 创建新任务
1. 在 WORK_LOG.md 中添加任务
2. 如果任务很大，创建 GitHub Issue
3. 使用 `create_branch` 如需隔离
4. 执行工作，定期 commit

### 完成任务
1. 更新 memory/learnings.md
2. 更新 memory/context.md
3. 提交所有变更
4. 清理 WORK_LOG.md

### 跨对话恢复
1. 读取 AGENTS.md
2. 读取 WORK_LOG.md
3. 根据 WORK_LOG 继续工作

---

## （后续使用中继续补充新工具和最佳实践）
