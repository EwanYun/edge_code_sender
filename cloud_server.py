from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Track received tasks
received_tasks = []


@app.route('/cloud/process', methods=['POST'])
def process_task():
    """Simple endpoint to receive tasks"""
    task = request.json
    received_tasks.append({
        "task_id": task["id"],
        "received_at": time.time(),
        "task_data": task
    })
    print(f"Cloud received task: {task['id']} (Total: {len(received_tasks)})")
    return jsonify({"status": "success", "location": "cloud"})


@app.route('/cloud/stats', methods=['GET'])
def get_stats():
    """Return count of received tasks"""
    return jsonify({"task_count": len(received_tasks)})


if __name__ == '__main__':
    print("Starting cloud server on port 8001...")
    app.run(host='0.0.0.0', port=8001)