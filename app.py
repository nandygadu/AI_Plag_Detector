from flask import Flask, request, jsonify, render_template,send_file
import os
from bert_hmm import Plagarism_check
import numpy as np
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import joblib


hmm_model = joblib.load(r'hmm_model.pkl')
tokenizer = BertTokenizer.from_pretrained(r'bert')
model = BertForSequenceClassification.from_pretrained(r'bert')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')  # Your HTML file containing the form

@app.route('/upload_file', methods=['POST'])
def upload_file():
    # Check if the 'document' key is in the request
    if 'document' not in request.files:
        return "No file part in the request", 400

    file = request.files['document']  # Use 'document' as in your form
    if file.filename == '':
        return "No file selected", 400

    if file:
        # Save the uploaded file to the configured UPLOAD_FOLDER
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        Plag = Plagarism_check(file_path,hmm_model=hmm_model,tokenizer=tokenizer,model=model)
        
        # Call your backend model's file-checking function here
        # Replace this with the actual function call to your model
        return render_template('index.html',ai_percent = Plag)
    

@app.route('/text_area',methods = ['POST'])
def text_area():
        if request.method == 'POST':
        # Get the input text from the form
            input_text = request.form['input_text']

            # Save the input text to sample.txt
            with open('sample.txt', 'w',encoding='utf-8') as f:
                f.write(input_text)

            # Call the bert_hmm code to process the text and generate result.pdf
            plag = Plagarism_check(r'sample.txt',hmm_model=hmm_model,tokenizer=tokenizer,model=model)
            return render_template('index.html',ai_percent = plag)


@app.route('/result')
def display_result():
    # Check if the result.pdf exists
    if os.path.exists('result.pdf'):
        # Send the file to the user for download/view
        return send_file('result.pdf', as_attachment=False)
    else:
        return "No PDF available. Please submit text first."

if __name__ == '__main__':
    app.run(debug=True)
