import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename



# OpenAI API Key
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# Flask setup
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



def transcribe_audio(audio_path):
    """Transcribes audio using OpenAI's Whisper model."""
    with open(audio_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
    return response["text"]

def generate_image(prompt):
    """Generates an image using OpenAI's DALL·E model."""
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    return response["data"][0]["url"]

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded", 400
        
        file = request.files["file"]
        if file.filename == "":
            return "No selected file", 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Transcribe audio
        transcription = transcribe_audio('static/Recording.m4a')

        # Generate image
        image_url = generate_image(transcription)

        return render_template("result.html", transcription=transcription, image_url=image_url)

    return render_template("index.html")

# Route to serve uploaded files
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
