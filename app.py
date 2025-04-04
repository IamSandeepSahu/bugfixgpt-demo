from flask import Flask, jsonify, request
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Bug: Division by zero error
@app.route('/api/divide')
@app.route('/api/divide')
def divide():
    try:
        a = int(request.args.get('a', 10))
        b = int(request.args.get('b', 2))  # Changed default to 2 instead of 0
        result = a / b
        return jsonify({"result": result})
    except Exception as e:
        error_msg = f'{{"error": "{str(e)}", "route": "/api/divide", "params": {json.dumps(request.args.to_dict())}}}'
        logger.error(error_msg)
        return jsonify({"error": str(e)}), 500
@app.route('/')
def home():
    return jsonify({
        "message": "BugFixGPT Demo - AI-Powered Automated Debugging", 
        "endpoints": ["/api/divide?b=0"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 