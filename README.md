# Audio Transcription and Image Generation App

This Flask application allows users to upload audio files, transcribe them using OpenAI's Whisper model, and generate images based on the transcription using OpenAI's DALL-E model.

## Features

- Audio file upload functionality
- Automatic transcription of audio using OpenAI's Whisper API
- Image generation based on transcribed text using OpenAI's DALL-E API
- Simple web interface to interact with the application

## Project Structure

```
audio-transcription-image-app/
├── app.py                  # Main Flask application
├── .env                    # Environment variables (OpenAI API key)
├── static/                 # Static files
│   └── Recording.m4a       # Sample audio file referenced in code
├── templates/              # HTML templates
│   ├── index.html          # Upload page
│   └── result.html         # Results display page
├── uploads/                # Directory for uploaded files
└── README.md               # This file
```

## Prerequisites

- Python 3.6+
- OpenAI API key

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mynameisabhi2k/Image-Generator-Web-Application.git
cd Image-Generator-Web-Application
```

2. Install the required dependencies:

```bash
pip install flask openai python-dotenv werkzeug
```

3. Create a `.env` file in the project root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Start the Flask application:

```bash
python app.py
```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Upload an audio file using the web interface

4. The application will transcribe the audio and generate an image based on the transcription

5. View the transcription and generated image on the results page

## Code Explanation

The application uses:
- Flask for the web server and routing
- OpenAI's Whisper API for audio transcription
- OpenAI's DALL-E API for image generation
- Werkzeug for secure file handling

