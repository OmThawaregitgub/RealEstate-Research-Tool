import sys
from flask import Flask, request, jsonify, render_template

# Fix for ChromaDB sqlite3 issue on some systems
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from rag import process_urls, generate_answer

app = Flask(__name__)

# New route to serve the frontend HTML file
@app.route('/')
def serve_index():
    return render_template('index.html')

# Route to handle URL processing
@app.route('/process-urls', methods=['POST'])
def process_data():
    data = request.get_json()
    urls = data.get('urls', [])

    if not urls:
        return jsonify({"status": "error", "message": "No URLs provided."}), 400

    try:
        status_message = process_urls(urls)
        return jsonify({"status": "success", "message": status_message}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to handle question answering
@app.route('/generate-answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"status": "error", "message": "No query provided."}), 400

    try:
        answer, sources = generate_answer(query)
        return jsonify({"status": "success", "answer": answer, "sources": sources}), 200
    except RuntimeError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # You can change the host and port if needed
    app.run(host='0.0.0.0', port=5000, debug=True)
