# Organizing Research Papers Using Text Embeddings and Clustering
### In this project, I integrate research into my course on artificial intelligence at Hiram College. The goal is simple—organize research papers using text embeddings and clustering.

# Documentation

1. **Extracting text** from PDFs using PyMuPDF
2. **Creating embeddings** from abstracts using the `sentence-transformers` library
3. **Clustering** papers using the KMeans algorithm
4. **Visualizing** the clusters with **PCA** and **Matplotlib**

## Dependencies

- **[PyMuPDF](https://pypi.org/project/PyMuPDF/)** - To extract text from PDF files.
- **[sentence-transformers](https://huggingface.co/sentence-transformers)** - For generating text embeddings.
- **[scikit-learn](https://scikit-learn.org/stable/)** - For clustering and dimensionality reduction.
- **[Matplotlib](https://matplotlib.org/stable/)** - For visualizing the clustered data.

## Modules

### 1. **Data Fetching Script (`fetch_arxiv_dataset.py`)**

This script uses the arXiv API to fetch a set of research papers and download them as PDFs into a designated `data` folder

#### Key References:
- **[arXiv API Documentation](https://arxiv.org/help/api/index)**: For fetching papers from arXiv.
- **[requests library](https://docs.python-requests.org/en/latest/)**: For making HTTP requests to download the PDFs.
- **[tqdm library](https://tqdm.github.io/)**: For displaying a progress bar during the download process.

### 2. **Text Embedding & Clustering Script (`analysis.py`)**

This script reads the PDFs, extracts the abstract text, generates embeddings using the `sentence-transformers` library, and then clusters the papers using the KMeans algorithm.

#### Key Steps
1. **Text Extraction**:
    - Extracts abstracts from the downloaded PDFs using a custom text extraction function (likely based on PyMuPDF or another library).

2. **Text Embedding**:
    - Uses a pre-trained **[SentenceTransformer](https://huggingface.co/sentence-transformers)** model to convert abstracts into high-dimensional vector embeddings

3. **Clustering**:
    - Applies the **[KMeans algorithm](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)** to group papers into clusters based on their content
    
4. **Dimensionality Reduction (PCA)**:
    - Reduces the dimensionality of the embeddings to 2D using **[PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)** for visualization
    
5. **Visualization**:
    - Plots the clusters in 2D using **[Matplotlib](https://matplotlib.org/stable/contents.html)**

## Workflow

1. **Fetch the Data**
2. **Generate Embeddings**
3. **Cluster Papers**
4. **Visualize Results**

## Understanding the Code

### 1. **Data Fetching (`fetch_arxiv_dataset.py`)**

This script makes use of the **[arXiv API](https://arxiv.org/help/api/index)** and **[requests](https://docs.python-requests.org/en/latest/)** to download research papers.

#### Explanation of Key Code:
- **`arxiv.Client()`**: Used to interact with the arXiv API and search for papers
- **`random.sample()`**: Selects a random sample of papers to download from the total available set
- **`requests.get()`**: Downloads each PDF file from the provided URL

### 2. **Text Embedding and Clustering (`analysis.py`)**

This script handles the clustering of research papers. It uses **[sentence-transformers](https://huggingface.co/sentence-transformers)** for embedding generation and **[scikit-learn](https://scikit-learn.org/stable/)** for clustering.

#### Explanation of Key Code:
- **`SentenceTransformer()`**: Loads a pre-trained transformer model to convert text (abstracts) into embeddings
- **`KMeans(n_clusters=5)`**: Performs clustering on the text embeddings using KMeans
- **`PCA(n_components=2)`**: Reduces the embeddings to 2D space for visualization

### 3. **Visualization (`matplotlib.pyplot`)**

The final clustering results are visualized using **[Matplotlib](https://matplotlib.org/stable/contents.html)**. This enables you to observe how papers are grouped based on the clustering.

---

## Resources for Further Learning

### Text Embedding and NLP
- **[Hugging Face Transformers](https://huggingface.co/transformers/)**: A powerful library for NLP models, including sentence transformers
- **[Sentence-Transformers Documentation](https://huggingface.co/sentence-transformers)**: Learn how to use transformer models for text embeddings

### Clustering and Dimensionality Reduction
- **[KMeans Clustering in Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)**: Documentation on KMeans clustering
- **[PCA in Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)**: A detailed guide on PCA for dimensionality reduction

### File Handling and Downloads
- **[Requests Library Documentation](https://docs.python-requests.org/en/latest/)**: A comprehensive guide to making HTTP requests in Python, including handling file downloads
- **[PyMuPDF Documentation](https://pypi.org/project/PyMuPDF/)**: For extracting text from PDFs
