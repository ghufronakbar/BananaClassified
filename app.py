import random
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()  # Load file .env

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "defaultsecret")

# Ensure upload folder exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/scan', methods=['GET','POST'])
def scan():
    if request.method == 'GET':
        return render_template('scan.html')
    if 'image' not in request.files:
        return {'status': 400, 'message': "No file part", 'data': None}, 400
    file = request.files['image']
    if file.filename == '':
        return {'status': 400, 'message': "No selected file", 'data': None}, 400
    if file:
        # Simulate a random algorithm to determine freshness        
        is_fresh = random.choice([True, False])
        random_acc = random.uniform(0, 1)
        return {'status': 200, 'message': "File uploaded successfully", 'data': {'isFresh': is_fresh , 'accuracy': random_acc}}, 200

@app.route('/result')
def result():
    return render_template('result.html')
    # print(request.args)
    # filename = request.args.get('filename')
    # if filename:
    #     return render_template('result.html', filename=filename)
    # return "No file uploaded", 400
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug, port=port)
