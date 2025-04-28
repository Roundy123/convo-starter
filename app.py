from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ice_breaker import ice_break_with
import os

app = Flask(__name__)

@app.route('/')
def index():
    initial_name = request.args.get('name', '')
    return render_template('index.html', initial_name=initial_name)

@app.route('/process')
def process():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    
    try:
        summary, profile_pic_url, ice_breakers = ice_break_with(name)
        return jsonify({
            'summary': summary.summary,
            'interesting_facts': summary.facts,
            'ice_breakers': ice_breakers,
            'profile_pic_url': profile_pic_url
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    load_dotenv()
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)