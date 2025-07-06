from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user database
USER_DB = {
    "admin": "secret123",
    "user1": "welcome"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400

    if username in USER_DB and USER_DB[username] == password:
        return jsonify({"message": "Login successful", "token": "fake-jwt-token"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
