from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Testing Flask App!"

# Define a route that returns some data
@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hey There"})

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True, port=8080)
