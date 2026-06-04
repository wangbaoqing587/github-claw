# 使用示例

## 图片处理

### 压缩 JPEG 图片

1. 在首页点击"选择图片或拖放"
2. 选择或拖放一个 JPG 图片
3. 在"压缩图片"部分设置质量（例如 75）
4. 点击"压缩"按钮
5. 等待处理完成，查看文件大小变化

### 将 PNG 转换为 WebP

1. 选择一个 PNG 图片
2. 在"格式转换"部分选择"WebP"作为目标格式
3. 点击"转换"按钮
4. 处理完成后可以下载 WebP 格式的文件

## 音频处理

### 压缩 MP3 音频

1. 切换到"🎵 音频处理"页面
2. 选择一个 MP3 文件
3. 在"压缩音频"部分选择比特率（例如 128 kbps）
4. 点击"压缩"按钮
5. 处理完成

### 将 WAV 转换为 MP3

1. 选择一个 WAV 文件
2. 在"格式转换"部分选择"MP3"作为目标格式
3. 点击"转换"按钮
4. 获得 MP3 格式的文件

## 视频处理

### 压缩 MP4 视频

1. 切换到"🎥 视频处理"页面
2. 选择一个 MP4 视频文件
3. 在"压缩视频"部分：
   - 选择比特率（例如 2000 kbps）
   - 选择质量预设（例如 medium）
4. 点击"压缩"按钮
5. 等待处理完成（可能需要较长时间）

### 调整视频分辨率

1. 选择一个视频文件
2. 在"分辨率调整"部分：
   - 设置宽度（例如 640）
   - 设置高度（例如 480）
3. 点击"调整"按钮
4. 处理完成后下载

### 转换视频格式

1. 选择一个视频文件
2. 在"格式转换"部分选择目标格式（例如 WebM）
3. 点击"转换"按钮
4. 获得转换后的视频文件

## 查看处理历史

1. 切换到"📜 处理历史"页面
2. 查看所有已处理的任务：
   - 文件名
   - 处理类型
   - 操作类型
   - 状态（pending/processing/completed/failed）
   - 创建时间
3. 页面会每 5 秒自动刷新

## API 使用示例

### 使用 cURL 上传文件

```bash
curl -F "file=@/path/to/image.jpg" http://localhost:5000/api/upload
```

### 使用 Python 调用 API

```python
import requests

# 上传文件
with open('image.jpg', 'rb') as f:
    response = requests.post('http://localhost:5000/api/upload', 
                            files={'file': f})
    filename = response.json()['filename']

# 压缩图片
response = requests.post('http://localhost:5000/api/image/process',
                        json={
                            'filename': filename,
                            'operation': 'compress',
                            'params': {'quality': 80}
                        })
print(response.json())
```

### 使用 JavaScript 调用 API

```javascript
// 上传文件
const formData = new FormData()
formData.append('file', fileInput.files[0])

const uploadRes = await fetch('http://localhost:5000/api/upload', {
  method: 'POST',
  body: formData
})

const { filename } = await uploadRes.json()

// 处理图片
const processRes = await fetch('http://localhost:5000/api/image/process', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    filename,
    operation: 'convert',
    params: { target_format: 'webp' }
  })
})

const result = await processRes.json()
console.log(result)
```

## 批量处理

虽然 UI 支持一个一个文件处理，但可以通过 API 进行批量处理：

```python
import os
import requests

# 遍历目录中的所有图片
upload_dir = './images'
for filename in os.listdir(upload_dir):
    if filename.endswith('.jpg'):
        filepath = os.path.join(upload_dir, filename)
        
        # 上传
        with open(filepath, 'rb') as f:
            upload_res = requests.post(
                'http://localhost:5000/api/upload',
                files={'file': f}
            )
        
        uploaded_filename = upload_res.json()['filename']
        
        # 压缩
        process_res = requests.post(
            'http://localhost:5000/api/image/process',
            json={
                'filename': uploaded_filename,
                'operation': 'compress',
                'params': {'quality': 70}
            }
        )
        
        print(f"处理完成: {filename}")
```

## 性能优化建议

1. **图片压缩**：高质量应用设置 85-90，低质量应用设置 70-75
2. **音频压缩**：
   - 音乐：192 kbps
   - 播客：128 kbps
   - 电话：64 kbps
3. **视频压缩**：
   - 超快预设：快速处理，较大文件
   - 中等预设：平衡速度和文件大小
   - 慢速预设：最高压缩率，处理时间长

## 支持的文件格式

### 图片
- JPEG (.jpg, .jpeg)
- PNG (.png)
- WebP (.webp)
- GIF (.gif)

### 音频
- MP3 (.mp3)
- WAV (.wav)
- AAC (.aac)
- FLAC (.flac)

### 视频
- MP4 (.mp4)
- WebM (.webm)
- AVI (.avi)
- MOV (.mov)

## 故障排除

如果处理失败，请：
1. 查看历史记录中的错误消息
2. 确保文件格式受支持
3. 确保有足够的磁盘空间
4. 检查后端日志输出
5. 尝试用更小的文件测试
