from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ice_breaker import ice_break_with
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    try:
        summary, profile_pic_url = ice_break_with(name)
        print(f"Profile picture URL: {profile_pic_url}")  # Debug log
        return jsonify({
            "summary": summary.summary,
            "interesting_facts": summary.facts,
            "profile_pic_url": profile_pic_url
        })
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug log
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    load_dotenv()
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)