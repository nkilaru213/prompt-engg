import os
import textract

# pip install textract
# sudo apt install antiword unrtf poppler-utils tesseract-ocr

def extract_text_from_files(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.pdf', '.docx', '.txt', '.pptx')):
            file_path = os.path.join(folder_path, filename)
            try:
                text = textract.process(file_path).decode('utf-8')
                documents.append({"filename": filename, "text": text})
            except Exception as e:
                print(f"Error extracting from {filename}: {e}")
    return documents

#Chunk and generate embeddings

from sentence_transformers import SentenceTransformer

def chunk_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def generate_embeddings(chunks, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    vectors = model.encode(chunks)
    return vectors

#store in Vector DB

import faiss
import numpy as np
import pickle

def store_embeddings(vectors, chunks, index_file='index.faiss', map_file='text_map.pkl'):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    # Save FAISS index
    faiss.write_index(index, index_file)

    # Save text mapping
    text_map = {i: chunks[i] for i in range(len(chunks))}
    with open(map_file, 'wb') as f:
        pickle.dump(text_map, f)

    print(f"Stored {len(chunks)} chunks.")

def execute(folder_path):
    all_chunks = []
    for doc in extract_text_from_files(folder_path):
        chunks = chunk_text(doc["text"])
        all_chunks.extend(chunks)

    vectors = generate_embeddings(all_chunks)
    store_embeddings(np.array(vectors), all_chunks)


