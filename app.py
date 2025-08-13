from flask import Flask, render_template, request, send_file
import google.generativeai as genai
from dotenv import load_dotenv
import os
from io import BytesIO

load_dotenv()
genai.configure(api_key=os.getenv("keys"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")