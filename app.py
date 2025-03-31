from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up Faelith's unique identifier
AUTHORIZED_USER = "TrueFaelith0"  # Your unique identifier
openai.api_key = 'your-openai-api-key-here'  # Your OpenAI API key

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    user_id = request.json.get('user_id')  # Assume each platform sends a user ID with the message
    
    # Check if the message is from you
    if user_id != AUTHORIZED_USER:
        return jsonify({'response': "You are not authorized to interact with Faelith."}), 403
    
    # Process the message with OpenAI (can replace with more advanced AI model logic)
    response = openai.Completion.create(
        engine="text-davinci-003",  # Example OpenAI model
        prompt=user_input,
        max_tokens=150
    )
    
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
