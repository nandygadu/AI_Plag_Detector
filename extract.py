import re
import os
from PyPDF2 import PdfReader

def extract_sentences_in_chunks(text, sentence_limit=5):
    # Split the text into sentences using regex
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    
    # Yield chunks of sentences
    for i in range(0, len(sentences), sentence_limit):
        chunk = " ".join(sentences[i:i + sentence_limit])
        yield chunk

def extract_text(file_name):
    text = ""

    # Check the file extension
    _, file_extension = os.path.splitext(file_name)

    if file_extension.lower() == '.pdf':
        # Read from PDF file
        with open(file_name, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"  # Add a newline after each page
    elif file_extension.lower() == '.txt':
        # Read from text file
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        raise ValueError("Unsupported file format. Please use a .txt or .pdf file.")

    # Process the extracted text in chunks
    extracted_chunks = []
    for chunk in extract_sentences_in_chunks(text):
        extracted_chunks.append(chunk)

    return extracted_chunks
