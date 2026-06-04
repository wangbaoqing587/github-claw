# memory/learnings.md: 知识与学习积累

本文件记录在各个任务中学到的、可复用的知识、技巧和洞察。

格式：`[日期] 任务或主题: 具体内容`

---

## [2026-06-04] 多媒体处理平台开发总结

### 技术栈整合

#### 前端框架
- **Vue 3** 提供组件化开发，Vue Router 处理多页面路由
- **Vite** 比 Webpack 更快的构建和开发体验
- **Axios** 简洁的 HTTP 客户端，自动 JSON 序列化
- 关键：配置 vite.config.js 中的代理，避免 CORS 问题

#### 后端框架
- **Flask** 轻量级框架，适合快速 REST API 开发
- **Flask-CORS** 必须启用，否则前端无法跨域请求
- **SQLite** 适合小型应用，无需额外部署
- **Blueprint** 用于模块化路由组织

### 多媒体处理实现

#### 图片处理 (Pillow)
```python
from PIL import Image

# 关键：处理 RGBA 转 RGB（特别是 PNG 和 GIF）
img = Image.open(path)
if img.mode == 'RGBA':
    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
    rgb_img.paste(img, mask=img.split()[3])
    img = rgb_img

# 优化：使用 optimize=True 和适当的质量参数
img.save(output_path, 'JPEG', quality=85, optimize=True)
```

#### 音频处理 (FFmpeg)
```bash
# 基本命令格式
ffmpeg -i input.mp3 -acodec libmp3lame -ab 192k output.mp3

# 关键：设置超时和捕获 stderr
subprocess.run(cmd, capture_output=True, text=True, timeout=300)
```

#### 视频处理 (FFmpeg)
```bash
# 压缩：使用预设平衡速度和质量
ffmpeg -i input.mp4 -b:v 2000k -preset medium output.mp4

# 缩放：使用 scale filter
ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4

# 格式转换：选择合适的编码器
# MP4: libx264 + aac
# WebM: libvpx + libvorbis
# AVI: mpeg4 + libmp3lame
```

### 数据库设计

```sql
CREATE TABLE tasks (
    id TEXT PRIMARY KEY,          -- UUID
    filename TEXT NOT NULL,       -- 原始文件名
    file_type TEXT NOT NULL,      -- image/audio/video
    operation TEXT NOT NULL,      -- 操作类型
    status TEXT NOT NULL,         -- pending/processing/completed/failed
    progress INTEGER DEFAULT 0,   -- 进度百分比
    created_at TEXT NOT NULL,    -- ISO 格式时间戳
    updated_at TEXT NOT NULL,
    error_message TEXT            -- 错误信息
)
```

### API 设计模式

```python
# 标准响应格式
{
    'success': True/False,
    'task_id': 'uuid',
    'result_filename': 'file.ext',
    'size': 12345,
    'error': 'error message'  # 仅在失败时
}

# 任务状态流
pending -> processing -> completed (success=true) or failed (success=false)
```

### 前端最佳实践

#### 文件上传处理
```javascript
// 1. 验证文件类型
const allowedTypes = ['image/jpeg', 'image/png']
if (!allowedTypes.includes(file.type)) {
    // 拒绝
}

// 2. 使用 FormData 上传二进制
const formData = new FormData()
formData.append('file', file)
await fetch('/api/upload', { method: 'POST', body: formData })

// 3. 正确处理错误
if (!response.ok) {
    const error = await response.json()
    // 显示 error.error
}
```

#### 异步流程
```javascript
// 三步流程：上传 -> 处理 -> 下载
const { filename } = await uploadFile(file)
const { result_filename } = await processFile(filename, params)
const blob = await downloadFile(result_filename)
```

### 常见问题和解决方案

| 问题 | 原因 | 解决方案 |
|------|------|--------|
| CORS 错误 | 后端未启用 CORS | `app = Flask(__name__); CORS(app)` |
| FFmpeg 超时 | 大文件处理时间长 | 增加 `timeout` 参数 |
| 图片转换失败 | 色彩空间不兼容 | 使用 `convert('RGB')` 规范化 |
| 数据库锁定 | 多个连接冲突 | 每次操作后 `conn.close()` |
| 文件名冲突 | 多个用户同时处理 | 使用 UUID 作为前缀 |

### 性能优化建议

1. **文件大小限制**：设置 `MAX_FILE_SIZE = 500MB`
2. **FFmpeg 预设**：
   - 快速处理：`preset=ultrafast`（文件大）
   - 平衡：`preset=medium`（推荐）
   - 最优压缩：`preset=slow`（处理慢）
3. **内存优化**：使用流式处理而非全量加载
4. **并发处理**：添加任务队列 (Celery) 支持

### 项目结构建议

```
backend/
├── app.py              # 主应用 + 全局配置
├── config.py           # 配置常量（可选）
├── routes/
│   ├── __init__.py
│   ├── image_routes.py
│   ├── audio_routes.py
│   ├── video_routes.py
├── services/           # 业务逻辑
├── models/             # 数据模型（可选）
└── uploads/            # 临时文件存储
```

### 跨对话保存

本项目的所有代码、文档、配置都已保存到 GitHub，包括：
- 完整的前后端代码
- 依赖配置文件
- API 和部署文档
- 使用示例

下次恢复时只需 clone 项目即可继续开发。

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

## 相关技术参考

- Flask 官方文档：https://flask.palletsprojects.com/
- Vue 3 文档：https://vuejs.org/
- FFmpeg 文档：https://ffmpeg.org/documentation.html
- Pillow 文档：https://pillow.readthedocs.io/
