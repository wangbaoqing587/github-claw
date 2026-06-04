"""Image processing routes"""
import os
from flask import Blueprint, request, jsonify, send_file
from services.image_processor import ImageProcessor
import uuid
from datetime import datetime
import sqlite3

bp = Blueprint('image', __name__, url_prefix='/api/image')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'tasks.db')

image_processor = ImageProcessor(UPLOAD_FOLDER)

def save_task(task_id, filename, file_type, operation, status, error_message=None):
    """Save task to database"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.utcnow().isoformat()
    c.execute('''
        INSERT OR REPLACE INTO tasks 
        (id, filename, file_type, operation, status, created_at, updated_at, error_message)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (task_id, filename, file_type, operation, status, now, now, error_message))
    conn.commit()
    conn.close()

@bp.route('/process', methods=['POST'])
def process():
    """Process image"""
    data = request.json
    filename = data.get('filename')
    operation = data.get('operation')
    params = data.get('params', {})
    
    if not filename or not operation:
        return jsonify({'error': 'Missing filename or operation'}), 400
    
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(input_path):
        return jsonify({'error': 'File not found'}), 404
    
    task_id = str(uuid.uuid4())
    
    try:
        save_task(task_id, filename, 'image', operation, 'processing')
        
        if operation == 'compress':
            quality = params.get('quality', 85)
            result_path = image_processor.compress(input_path, quality=quality)
        elif operation == 'convert':
            target_format = params.get('target_format', 'jpeg')
            result_path = image_processor.convert_format(input_path, target_format)
        else:
            raise ValueError(f'Unknown operation: {operation}')
        
        result_filename = os.path.basename(result_path)
        result_size = os.path.getsize(result_path)
        
        save_task(task_id, filename, 'image', operation, 'completed')
        
        return jsonify({
            'success': True,
            'task_id': task_id,
            'result_filename': result_filename,
            'size': result_size
        })
    except Exception as e:
        save_task(task_id, filename, 'image', operation, 'failed', str(e))
        return jsonify({'error': str(e)}), 500

@bp.route('/download/<filename>', methods=['GET'])
def download(filename):
    """Download processed file"""
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    
    return send_file(filepath, as_attachment=True, download_name=filename)
