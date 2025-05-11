from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Debugging: Print incoming request
        print("Received request:", request.get_data())
        
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data received. Please send valid JSON."}), 400
        
        text = data.get("text", "").strip()  # Ensure there’s no leading/trailing whitespace
        if not text:
            return jsonify({"error": "Text input is empty. Please provide valid text."}), 400

        print("Received text:", text)  # Debugging: Print the text received
        
        # Limit the input text length to avoid overflow
        if len(text.split()) > 1000:
            text = " ".join(text.split()[:1000])
        
        # Generate summary
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        
        # Return summary
        return jsonify({"summary": summary[0]["summary_text"]})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    app.run(debug=True)
