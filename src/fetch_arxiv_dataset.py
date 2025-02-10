import arxiv
import os
import random
import requests
from tqdm import tqdm  # progress bar for download process

# Specify download location
DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

# Make sure the 'data' folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Initialize arXiv client
client = arxiv.Client()

# Define search criteria: Searching across Physics, Biology, and Literature categories
search = arxiv.Search(
    query="cat:physics OR cat:q-bio OR cat:cs.CL",  # physics, biology, and literature
    max_results=1000,  # get a large set of papers
    sort_by=arxiv.SortCriterion.SubmittedDate  # sort by submission date
)

# Fetch papers from arXiv
papers = list(client.results(search))

# Handle case where fewer than 500 papers are available
num_papers_to_download = min(len(papers), 500)  # download up to 500 papers, or all if fewer

# Randomly select papers for downloading
selected_papers = random.sample(papers, num_papers_to_download)

# Download PDFs and save them to the "data" folder
for paper in tqdm(selected_papers, desc="Downloading PDFs"):
    paper_id = paper.entry_id.split("/")[-1]  # extract paper ID from the URL
    pdf_url = paper.pdf_url  # get the PDF URL
    pdf_path = os.path.join(DATA_FOLDER, f"{paper_id}.pdf")  # save the file with paper ID as filename

    try:
        response = requests.get(pdf_url, stream=True)  # download in streaming mode
        if response.status_code == 200:  # check for successful response
            with open(pdf_path, "wb") as f:  # open file for writing
                for chunk in response.iter_content(1024):  # write content in chunks
                    f.write(chunk)
        else:
            print(f"Failed to download: {pdf_url}")
    except Exception as e:
        print(f"Error downloading {pdf_url}: {e}")
