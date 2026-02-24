from flask import Flask, render_template, request, jsonify
import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
    "Content-Type": "application/json",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():

    prompt = request.json['prompt']

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    if response.status_code != 200:
        return jsonify({"error": response.text})

    image_base64 = base64.b64encode(response.content).decode()

    image_url = f"data:image/png;base64,{image_base64}"

    return jsonify({"image_url": image_url})


if __name__ == "__main__":
    app.run(debug=True)