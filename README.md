# Twitter Thread AI Generator

An AI-powered tool that helps you generate engaging Twitter threads using OpenRouter AI. Simply input your topic and preferred tone, and get a well-structured thread optimized for Twitter.

## Features

- 🤖 AI-powered thread generation using OpenRouter
- 📝 Multiple tone options (Professional, Casual, Humorous, Educational, Inspirational)
- 🎯 Automatically formats content into tweet-sized chunks
- 💫 Adds appropriate emojis and hooks
- 🎨 Clean, modern web interface

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your API key:
   - Go to [OpenRouter](https://openrouter.ai/keys)
   - Create an account and generate an API key
   - Copy your API key

4. Set up environment variables:
   - Create '.env' file in twitter_thread_ai
   - Add in '.env' file - OPENROUTER_API_KEY=YOUR_API_KEY
   - Save it

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and go to:
   ```
   http://localhost:5000
   ```

## Usage

1. Enter your topic in the text area
2. Select your preferred tone
3. Click "Generate Thread 🚀"
4. Wait for the AI to generate your thread
5. Copy and use the generated tweets

## Models

The application uses the Mistral-7B-Instruct model by default, but you can modify the model in `app.py` to use other models available through OpenRouter.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements!
