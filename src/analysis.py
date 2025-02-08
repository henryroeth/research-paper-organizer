import fitz  # PyMuPDF module
import os
import pandas as pd
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Small & efficient embedding model

# Function to extract text from PDFs
def extract_text_from_pdfs(pdf_folder):
    pdf_texts = []
    file_names = []
    
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, file)
            doc = fitz.open(file_path)
            text = " ".join([page.get_text("text") for page in doc])  # Extract text from all pages
            pdf_texts.append(text)
            file_names.append(file)
    
    return pdf_texts, file_names

# Specify folder containing PDFs
pdf_folder = "C:/Users/henry/research-paper-organizer/data/"
pdf_texts, file_names = extract_text_from_pdfs(pdf_folder)

# Generate embeddings for each document abstract
embeddings = model.encode(pdf_texts)

# Perform K-Means clustering
num_clusters = 3  # May be adjusted
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
labels = kmeans.fit_predict(embeddings)

# Reduce dimensionality for visualization
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings)

# Create DataFrame for analysis
df = pd.DataFrame({'File Name': file_names, 'Cluster': labels})
print(df)

# Plot clusters
plt.figure(figsize=(8,6))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=labels, cmap='viridis', alpha=0.7)
for i, txt in enumerate(file_names):
    plt.annotate(txt, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]), fontsize=8, alpha=0.6)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Document Clustering Visualization")
plt.show()
