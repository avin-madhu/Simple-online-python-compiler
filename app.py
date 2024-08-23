from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Test cases
test_cases = [
    {"input": "3 5", "output": "8"},
    {"input": "7 8", "output": "15"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_code():
    code = request.form['code']
    passed_tests = 0

    for case in test_cases:
        result = run_code(code, case['input'])
        # stripping last 2 charcaters (maybe it's spaces)
        result = result[:len(result)-2]
        if str(result) == case['output']:
            passed_tests += 1

    score = (passed_tests / len(test_cases)) * 100
    return jsonify({"score": score, "passed_tests": passed_tests, "total_tests": len(test_cases)})


def run_code(code, input_data):
    try:
        proc = subprocess.run(
            ["python", "-c", code],
            input=input_data.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=2
        )
        output = proc.stdout.decode('utf-8')
        error = proc.stderr.decode('utf-8')
        
        if error:
            return f"Error: {error}"
        
        return output if output else "No Output"
        
    except subprocess.TimeoutExpired:
        return "Timeout"

if __name__ == '__main__':
    app.run(debug=True)
