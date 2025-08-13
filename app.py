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

@app.route("/generate", methods=["POST"])
def generate():
    description = request.form.get("description", "")
    

    prompt = f"""Generate a professional, well-formatted README.md in English.
    The project description is:
    {description}

    
    """

    model = genai.GenerativeModel("gemini-1.5")
    response = model.generate_content(prompt)

    readme_content = response.text or "Error generating README."

    # Save to in-memory file
    file_stream = BytesIO()
    file_stream.write(readme_content.encode('utf-8'))
    file_stream.seek(0)

    return send_file(
        file_stream,
        as_attachment=True,
        download_name="README.md",
        mimetype="text/markdown"
    )

if __name__ == "__main__":
    app.run(debug=True)
