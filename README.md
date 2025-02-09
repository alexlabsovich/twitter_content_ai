# Twitter Thread&Article AI Generator

An AI-powered tool that helps you generate engaging Twitter threads using OpenRouter AI. Simply input your topic and preferred tone, and get a well-structured thread optimized for Twitter.

## Features

- 🤖 AI-powered thread generation using OpenRouter
- 📝 Multiple tone options (Professional, Casual, Humorous, Educational, Inspirational)
- 🎯 Automatically formats content into tweet-sized chunks
- 💫 Adds appropriate emojis and hooks
- 🎨 Clean, modern web interface
- 2 language support (RU;ENG)

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

## Example
1. Sent text:
Mad Lads, please welcome the King of Monad – loui69 !:alarm_purple: 
He just joined our Nad Lads dedicated channel today. 
So, what is Nad Lads all about?
Nad Lads was one of the first - if not the first - faction inside the Monad ecosystem. The Monad community has shown massive respect for Mad Lads, creating content, memes, video edits, and amplifying our posts with full support.
With Monad Testnet launching this month, we’re ramping up our support game! This channel is dedicated to organizing strategies and co-events with our friends at Monad so we can grow together. 💜
Nad Lads is a front-row seat for active Mad Lads who want to support the Monad ecosystem…
…and who knows? Maybe King Loui and Monad will bless the most wild Lads with WL spots for their most coveted blue-chip projects.
Nad Lads ON TOP!

2. Result:
Title: Introducing the King of Monad: Loui69 and the Rise of Nad Lads in the Monad Ecosystem
Welcome to the launch of our exclusive Nad Lads channel, an extraordinary faction within the dynamic Monad ecosystem. In the realm of blockchain technology and decentralized finance, the Monad community has shown a profound respect for Nad Lads, culminating in an outpouring of content, memes, video edits, and resounding support for our initiatives.
**- The Origins of Nad Lads: Pioneers in the Monad Ecosystem**
Nad Lads, one of the first - if not the very first - faction inside the Monad community, has established a reputation for their unwavering commitment and groundbreaking contributions. The Monad Testnet, due to launch this month, offers an exciting opportunity for Nad Lads to demonstrate the full power of their strategic planning and cohesion within the ever-evolving Monad ecosystem.
**- A Channel for Active Mad Lads: Collaborating for Growth**
This dedicated channel serves as a front-row seat for active Mad Lads who seek to support the Monad ecosystem. Our collective goal is to foster an environment that encourages collaboration, growth, and the nurturing of future opportunities within Monad.
In a potential clue hinting at an exciting future, King Loui and the Monad team may even bestow exclusive Whitelist (WL) spots for their most coveted blue-chip projects upon the wildest and most passionate Lads.
**- The Rise of King Loui: Leading the Nad Lads Charge**
King Loui's joining our ranks signifies a new chapter for Nad Lads. As a globally recognized figure within the Monad community, King Loui's dedication and expertise will undoubtedly serve as a driving force, galvanizing Nad Lads towards even greater heights.
With him at the helm, we eagerly await the upcoming Monad Testnet launch and the potential opportunities it will bring for our faction, as we anticipate a future filled with exciting collaborations and mutual growth.
**- The Nad Lads Legacy: A Testament to the Power of Community**
Nad Lads stands as a testament to the power of community within the decentralized finance space. Through the hard work and dedication of our members, Nad Lads has managed to carve out a unique niche within the Monad ecosystem.
By organizing strategies, collaborating with the Monad team on co-events, and leading by example, Nad Lads continues to solidify its position as a driving force within the Monad community. Our commitment to growth, excellence, and collaboration sets us apart and provides us with a strong foundation upon which to grow and thrive in the burgeoning world of Monad.
Join the Nad Lads family today and be a part of the exciting journey as we navigate the Monad Testnet launch and beyond, keeping one foot always on the Nad Lads gas pedal.
Nad Lads ON TOP!

