<template>
  <div class="page">
    <div class="card">
      <h2>📜 处理历史</h2>
      
      <button class="refresh-btn" @click="loadTasks">刷新</button>
      
      <div v-if="loading" class="loading">加载中...</div>
      
      <div v-else-if="tasks.length === 0" class="empty">
        暂无处理历史
      </div>
      
      <div v-else class="tasks-list">
        <div v-for="task in tasks" :key="task.id" class="task-item">
          <div class="task-header">
            <span class="task-filename">{{ task.filename }}</span>
            <span :class="['task-status', task.status]">{{ task.status }}</span>
          </div>
          <div class="task-details">
            <p><strong>类型:</strong> {{ task.file_type }}</p>
            <p><strong>操作:</strong> {{ task.operation }}</p>
            <p><strong>创建时间:</strong> {{ formatDate(task.created_at) }}</p>
            <p v-if="task.error_message"><strong>错误:</strong> {{ task.error_message }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { listTasks } from '../services/api'

export default {
  name: 'HistoryPage',
  data() {
    return {
      tasks: [],
      loading: false
    }
  },
  mounted() {
    this.loadTasks()
    // Auto-refresh every 5 seconds
    this.interval = setInterval(() => this.loadTasks(), 5000)
  },
  beforeUnmount() {
    if (this.interval) clearInterval(this.interval)
  },
  methods: {
    async loadTasks() {
      this.loading = true
      try {
        const res = await listTasks()
        this.tasks = res.data
      } catch (error) {
        console.error('加载任务列表失败:', error)
      } finally {
        this.loading = false
      }
    },
    formatDate(dateString) {
      const date = new Date(dateString)
      return date.toLocaleString('zh-CN')
    }
  }
}
</script>

<style scoped>
.page {
  display: flex;
  justify-content: center;
  padding: 2rem 0;
}

.card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  max-width: 800px;
  width: 100%;
}

.card h2 {
  color: #333;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.refresh-btn {
  background: #667eea;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  margin-bottom: 1rem;
  transition: background 0.3s;
}

.refresh-btn:hover {
  background: #764ba2;
}

.loading {
  text-align: center;
  color: #667eea;
  padding: 2rem;
}

.empty {
  text-align: center;
  color: #999;
  padding: 2rem;
}

.tasks-list {
  display: grid;
  gap: 1rem;
}

.task-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  background: #fafafa;
  transition: all 0.3s;
}

.task-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.task-filename {
  font-weight: bold;
  color: #333;
  word-break: break-all;
}

.task-status {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
}

.task-status.pending {
  background: #fff3cd;
  color: #856404;
}

.task-status.processing {
  background: #cce5ff;
  color: #004085;
}

.task-status.completed {
  background: #d4edda;
  color: #155724;
}

.task-status.failed {
  background: #f8d7da;
  color: #721c24;
}

.task-details {
  font-size: 0.9rem;
  color: #666;
}

.task-details p {
  margin: 0.25rem 0;
}
</style>
