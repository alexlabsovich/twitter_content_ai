from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_content', methods=['POST'])
def generate_content():
    try:
        data = request.json
        topic = data.get('topic', '')
        tone = data.get('tone', 'professional')
        content_type = data.get('contentType', 'thread')
        language = data.get('language', 'en')

        # Set system message based on language
        system_message = (
            "You are a content creation expert who specializes in both Twitter threads and long-form articles. "
            f"Create content in {'Russian' if language == 'ru' else 'English'}. "
            "Adapt your writing style based on the requested format while maintaining engaging and informative content."
        )
        
        if content_type == 'thread':
            prompt = f"""Create a Twitter thread about {topic}. 
            Language: {'Russian' if language == 'ru' else 'English'}
            Tone: {tone}
            Rules:
            - Make it engaging and informative
            - Break it into 280-character chunks
            - Use emojis appropriately
            - Include a hook in the first tweet
            - End with a call to action
            - Write in {'Russian' if language == 'ru' else 'English'} language
            """
        else:
            prompt = f"""Write a well-structured article about {topic}.
            Language: {'Russian' if language == 'ru' else 'English'}
            Tone: {tone}
            Rules:
            - Create a compelling headline
            - Include an engaging introduction
            - Break into clear sections with subheadings
            - Use relevant examples and data points
            - Write in a clear, {tone} tone in {'Russian' if language == 'ru' else 'English'} language
            - Include a strong conclusion
            - Length: 800-1200 words
            """
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "http://localhost:5000",  # Your website URL
            "X-Title": "Twitter Thread Generator",    # Your app name
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "mistralai/mistral-7b-instruct",  # You can change the model
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        }
        
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for bad status codes
        
        response_data = response.json()
        
        content = response_data['choices'][0]['message']['content']
        
        if content_type == 'thread':
            # Process the response into tweet-sized chunks
            content_parts = content.split('\n')
            # Filter out empty strings and clean up tweets
            content_parts = [tweet.strip() for tweet in content_parts if tweet.strip()]
        else:
            # Process article content
            content_parts = [content]
        
        return jsonify({
            "success": True, 
            "content": content_parts,
            "contentType": content_type
        })
    
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "error": f"API Error: {str(e)}"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
