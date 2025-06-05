# PDF Document Processing Agent 🚀

An automated Python tool that scrapes websites for PDF documents, downloads them, processes their content, and saves the analyzed results. Perfect for research, data collection, and document analysis tasks.

## 🌟 Features

- 🌐 Scrapes websites to find PDF documents
- ⬇️ Downloads PDFs with progress tracking
- 📄 Processes PDF content (text extraction, metadata analysis)
- 💾 Saves processed results in JSON format
- ✅ Handles both direct PDF links and webpage scraping
- 🔒 Basic validation and error handling for corrupt/protected PDFs

## 🛠️ Installation

1. Clone the repository:
```powershell
git clone <repository-url>
cd DocumentHandling
```

2. Create and activate a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Set up environment variables:
```powershell
Copy-Item .env.example .env
```

## 🚀 Usage

1. Configure the target website in `main.py`:
```python
website_url = "https://example.com/pdfs/"  # Replace with your target URL
```

2. Run the script:
```powershell
python main.py
```

## 📁 Project Structure

```
├── config.py           # Configuration settings
├── main.py            # Main script with DocumentAgent class
├── pdf_scraper.py     # PDF scraping and downloading
├── pdf_processor.py   # PDF content processing
├── storage_handler.py # Result storage handling
├── downloads/         # Downloaded PDF storage
└── output/           # Processed results in JSON
```

## 📦 Output

The agent creates two main directories:
- `downloads/`: Stores downloaded PDF files
- `output/`: Contains processed content in JSON format with:
  - Text content
  - Metadata
  - Page information
  - Processing timestamps

## 📝 Requirements

- Python 3.8+
- Required packages (see requirements.txt)
- Internet connection
- Sufficient disk space for downloads

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
