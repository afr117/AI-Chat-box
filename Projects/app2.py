from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import traceback

app = Flask(__name__)

# OpenAI API key (replace with your actual key)
api_key = "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"
client = OpenAI(api_key=api_key)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        user_input = request.form['user_input']

        # Send input to OpenAI GPT-3.5 Turbo model
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chat assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        response_message = completion['choices'][0]['message']['content']

        return jsonify({'response_message': response_message})

    except Exception as e:
        print(f"Error: {str(e)}")
        traceback.print_exc()
        return jsonify({'response_message': 'Error processing request'})

if __name__ == '__main__':
    app.run(debug=True)
