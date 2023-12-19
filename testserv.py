from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/receive-string', methods=['POST'])
def receive_string():
    data = request.get_json()
    if 'input_string' in data:
        input_string = data['input_string']
        print(f"{input_string} hat verstanden wie REST APIs funktionieren!")
        return jsonify({'message': 'String received successfully'}), 200
    else:
        return jsonify({'error': 'No input string provided'}), 400

if __name__ == '__main__':
    app.run()
