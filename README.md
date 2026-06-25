# Advanced AI Plagiarism Checker

## Overview
This repository contains a Flask web application for detecting AI-generated text and plagiarism-like patterns in uploaded documents or pasted text. The system combines:
- a pretrained BERT classifier for text classification
- an HMM-based segmentation model for text chunking and context-aware prediction
- PDF extraction and report generation

The app accepts `.pdf` and `.txt` files, or direct pasted text, and provides:
- an AI-generated text likelihood score
- a downloadable PDF report summarizing the result

## Features
- Upload PDF or TXT documents for analysis
- Paste text directly into the web interface
- Detect likely AI-generated content in text segments
- Create a styled PDF report with classification results
- Simple Flask frontend with responsive UI


## Models Used
### BERT Classifier
- The project uses a `BertForSequenceClassification` model loaded from the `bert/` directory.
- It is used to classify chunks of text into categories such as human-written or AI-generated.

### HMM Segmentation
- The hidden Markov model (`hmm_model.pkl`) segments text based on sentence lengths.
- These segments are passed to the BERT classifier to improve contextual analysis.

### Text Extraction and Chunking
- `extract.py` extracts text from `.pdf` and `.txt` files.
- Text is subdivided into chunks of up to 5 sentences for processing.

## Requirements
- Python 3.8+ recommended
- Flask
- transformers
- torch
- numpy
- pandas
- joblib
- PyPDF2
- reportlab

## Installation
1. Open a terminal in the project root folder.
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install flask transformers torch numpy pandas joblib PyPDF2 reportlab
   ```

4. Ensure the following files and directories exist in the project root:
   - `bert/` with `config.json`, `model.safetensors`, `tokenizer_config.json`, `vocab.txt`, and `special_tokens_map.json`
   - `hmm_model.pkl`
   - `templates/index.html`

## How to Run
1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open your browser and visit:

   ```text
   http://127.0.0.1:5000
   ```

3. Use one of the two available options:
   - Upload a `.pdf` or `.txt` file and click **Upload and Check**
   - Paste text into the textarea and click **Check Now**

4. View the AI likelihood percentage on the page.
5. Download the generated PDF report by clicking **Download Report**.

## Notes
- Uploaded files are saved in the `uploads/` folder.
- The report is written to `result.pdf` in the project root.
- The current UI uses the `index.html` template under `templates/`.
- `sample.txt` is used as temporary storage for pasted text input.

## Troubleshooting
- If the app fails to start, confirm that the `bert/` model directory is present and `hmm_model.pkl` exists.
- For PDF extraction issues, verify that the input PDF is readable and not password-protected.
- If the BERT model load fails, ensure the `transformers` and `torch` versions are compatible with the model files.

## License
This project is provided as-is. Adapt the code and models as needed for research or personal projects.
