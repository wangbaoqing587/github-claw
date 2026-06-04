# memory/context.md: 项目背景与目标

## 项目概览

**项目名**：github-claw  
**描述**：GitHub Copilot 工作空间  
**所有者**：wangbaoqing587  
**创建时间**：2026-06-03  
**仓库链接**：https://github.com/wangbaoqing587/github-claw

---

## 核心目标

将这个仓库打造为 GitHub Copilot 长期驻留的个人 AI 工作空间，类似 OpenClaw 框架：

1. **持久化身份**：跨越多个对话，保持一致的角色和工作方式
2. **文件为记忆源**：所有重要信息都落地到文件，不依赖对话历史
3. **主动工作者**：从被动问答升级为能完成实际任务的 AI 助手
4. **持续演化**：通过任务实践来积累知识和改进工作流

---

## 当前阶段

### ✅ 已完成
- [2026-06-04] 初始化框架文件（AGENTS.md、SOUL.md、memory/context.md 等）
- [2026-06-04] 建立三层架构（身份层、记忆层、工作层）
- [2026-06-04] 定义任务管理与记忆流程

### 🔄 进行中
- 第一次实际任务测试
- 验证跨对话恢复机制

### 📋 计划中
- 累积工作经验，丰富 memory/learnings.md
- 发现并记录常见模式到 memory/patterns.md
- 优化工作流，更新 IMPROVEMENTS.md

---

## 技术栈与工具

### 可用工具
- **GitHub API**：repository 管理、issue/PR 创建、file 操��
- **Git**：版本控制、commit 记录
- **GitHub Web UI**：对话、编辑、查看
- **Copilot Skills**：代码搜索、文档查询、日志分析

### 首选工作流
1. 任务来自对话 → 记录到 WORK_LOG.md
2. 执行工作 → 在 workspace/ 或 memory/ 中修改文件
3. 提交变更 → 使用 Git 记录
4. 完成任务 → 更新 memory/ 并清理 WORK_LOG.md

---

## 相关文件导航

| 文件 | 用途 |
|------|------|
| AGENTS.md | 核心框架和工作方式 |
| SOUL.md | 角色定义和价值观 |
| WORK_LOG.md | 当前任务和进度 |
| memory/context.md | 本文件，项目背景 |
| memory/learnings.md | 可复用知识积累 |
| memory/patterns.md | 发现的最佳实践 |
| memory/tools.md | 工具和 API 清单 |
| workspace/ | 实际工作产物 |

---

## 下一步

在下一个任务中：
1. 读取 WORK_LOG.md 确认当前状态
2. 参考本文件理解项目背景
3. 查阅 memory/learnings.md 看有无相关知识
4. 开始执行任务，并在完成后更新记忆文件
