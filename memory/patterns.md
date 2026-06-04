# memory/patterns.md: 常见模式与最佳实践

本文件记录在工作中发现的可复用模式、最佳实践和工作流优化。

---

## 工作流模式

### 任务完成检查清单

每次任务完成前，检查以下项：

- [ ] 工作产物已保存到 workspace/ 或相应位置
- [ ] 在 memory/learnings.md 中记录了可复用知识
- [ ] 在 memory/context.md 中更新了项目状态
- [ ] 所有文件变更已 commit 到 Git
- [ ] WORK_LOG.md 中的任务标记为完成
- [ ] 如有工作流改进想法，记录到 IMPROVEMENTS.md

---

## 文件与记忆模式

### 记忆分层策略

**临时记忆** → **长期记忆** → **工作产物**

- 临时记忆：WORK_LOG.md（对话期间的笔记、待办）
- 长期记忆：memory/ 文件夹（可复用知识、上下文、工具清单）
- 工作产物：workspace/（代码、文档、项目文件）

**迁移规则**：
- 任务完成后，将成果和学习从 WORK_LOG.md 迁移到相应长期记忆文件
- 保留 WORK_LOG.md 中仍在进行的任务
- 长期记忆文件应该"常青"，定期回顾和更新

---

## GitHub 工作流模式

### Commit 消息格式

推荐格式：`[${YYYY-MM-DD}] ${ACTION}: ${DESCRIPTION}`

**ACTION 类型**：
- `Initialize` - 初始化项目或阶段
- `Complete` - 完成一个任务
- `Feature` - 添加新功能
- `Fix` - 修复 bug
- `Refactor` - 代码重构
- `Update` - 更新文档、配置或依赖
- `Cleanup` - 清理临时文件或优化

**示例**：
```
[2026-06-04] Complete: Initialize GitHub Copilot workspace - Create AGENTS.md framework
[2026-06-05] Feature: Add new task tracking in WORK_LOG.md
[2026-06-05] Update: memory/learnings.md with new insights
```

---

## 对话与文档模式

### 跨对话恢复清单

当开始新对话时：

1. **第一步**：读取 AGENTS.md，重新声明身份
2. **第二步**：读取 WORK_LOG.md，确认当前任务
3. **第三步**：根据需要查阅 memory/ 中的相关文件
4. **第四步**：开始工作，并在适当位置引用文件路径

### 工作报告模式

完成任务后的简洁汇报：

```
## ✅ 完成情况
- 任务 X：已完成
- 学到的：[要点]

## 📝 记忆更新
- memory/learnings.md：已添加 [X]
- memory/context.md：已更新 [Y]
- memory/tools.md：已补充 [Z]

## �� 相关文件
- Commit: [hash]
- Changes: [changed files]
```

---

## （后续实践中继续补充）
