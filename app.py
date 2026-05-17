import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        user_topic = data.get('topic', '')
        content_type = data.get('type', 'منشور سوشيال ميديا')
        
        prompt = f"""أنت كاتب محترف. المطلوب: كتابة {content_type} حول موضوع: {user_topic}
اكتب بالعربية الفصحى بشكل طبيعي، لا تذكر أنك ذكاء اصطناعي."""
        
        response = model.generate_content(prompt)
        return jsonify({'status': 'success', 'content': response.text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
