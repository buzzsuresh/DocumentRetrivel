# PDF Document Processing Agent

This project implements a document processing agent that:
1. Scrapes websites for PDF links
2. Downloads PDF documents
3. Processes the content using LangChain
4. Saves the results to a shared drive

## Setup

1. Create a virtual environment and activate it:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install langchain requests beautifulsoup4 PyPDF2 python-dotenv unstructured
```

3. Copy the `.env.example` file to `.env` and update the variables:
```powershell
Copy-Item .env.example .env
```

## Usage

1. Update the `website_url` in `main.py` with the target website URL.

2. Run the script:
```powershell
python main.py
```

## Project Structure

- `main.py`: Main script with the DocumentAgent class
- `pdf_scraper.py`: Functions for scraping and downloading PDFs
- `pdf_processor.py`: PDF processing using LangChain
- `storage_handler.py`: Functions for saving processed content
- `config.py`: Configuration settings

## Output

Processed documents are saved in:
- `downloads/`: Downloaded PDF files
- `output/`: Processed content in JSON format
