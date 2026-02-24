# AI Text-to-Image Generator using Flask and Stable Diffusion

This project is a web-based AI application that generates images from text prompts using Stable Diffusion via Hugging Face Inference API.

---

## 🌐 Live Demo

🔗 https://ai-text-to-image-generator-ew0m.onrender.com

## Features

• Generate AI images from text  
• Flask backend integration  
• Stable Diffusion AI model  
• Interactive web interface  
• Free and open-source AI model  

---

## Technologies Used

Python  
Flask  
Stable Diffusion  
Hugging Face API  
HTML  
CSS  
JavaScript  

---

## How to Run Locally

### Step 1: Install dependencies

```bash
pip install -r requirements.txt

### Step 2: Add Hugging Face API Key in .env

Add Hugging Face API Key in .env

### Step 3:Run the application

python app.py

### Step 4:Open browser

http://127.0.0.1:5000

How It Works

• User enters text prompt
• Flask sends request to Stable Diffusion model via Hugging Face API
• Model generates image
• Image displayed on website



## Project Structure

AI-Text-to-Image-Generator/
│
├── app.py # Main Flask backend application
├── requirements.txt # Project dependencies
├── .env # API key (not shared publicly)
├── .gitignore # Files ignored by Git
├── README.md # Project documentation
│
├── templates/
│ └── index.html # Frontend HTML file
│
└── static/
├── css/
│ └── style.css # Styling file
│
└── js/
└── script.js # Frontend JavaScript logic
