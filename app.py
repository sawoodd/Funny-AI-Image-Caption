from flask import Flask, render_template, request
import os, random, time
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config["DEBUG"] = True
# Demo realistic captions
demo_captions = [
    "A dog running across a grassy field.",
    "A person riding a bike on a busy street.",
    "A group of people standing near a car.",
    "A cup of coffee on a wooden table.",
    "A cat sitting near a window looking outside.",
    "A laptop placed beside a notepad on a desk.",
    "A mountain range covered with snow under a clear sky."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    filename = secure_filename(file.filename)
    upload_folder = 'static/uploads'
    os.makedirs(upload_folder, exist_ok=True)  # ✅ make sure folder exists
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    time.sleep(2.5)  # Simulate AI processing delay
    caption = random.choice(demo_captions)
    return render_template('result.html', caption=caption, img_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)
