# File: index.py
from flask import Flask, request, jsonify
from flask_cors import CORS # You might need to pip install flask-cors
import bunker_mod as bk

app = Flask(__name__)
CORS(app) # Allows your new Interface to talk to this API

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "API is running. Send POST request to / with roll_no and password."})

@app.route("/", methods=["POST"])
def get_attendance():
    # 1. Get credentials from JSON or Form Data
    if request.is_json:
        data = request.json
        roll_no = data.get('roll_no')
        password = data.get('password')
    else:
        roll_no = request.form.get('roll_no')
        password = request.form.get('password')

    if not roll_no or not password:
        return jsonify({"error": "Missing roll_no or password"}), 400

    try:
        # 2. Use the original scraper module
        # Note: Ensure bunker_mod.py returns a list/dict, not rendered HTML.
        # If bunker_mod returns a dict directly, this works perfectly.
        attendance_data = bk.return_attendance(roll_no, password)
        
        # 3. Return pure JSON
        return jsonify(attendance_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
