import PyPDF2
from typing import Dict, Any
import os

def process_pdf(pdf_path: str) -> Dict[str, Any]:
    """
    Process a PDF file using PyPDF2 and extract its content.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        Dict[str, Any]: Dictionary containing processed content and metadata
    """
    try:
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            reader = PyPDF2.PdfReader(file)
            
            # Extract text from each page
            pages_content = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    pages_content.append(text)
            
            # Extract document info
            info = reader.metadata if reader.metadata else {}
            
            # Create content dictionary
            content = {
                'title': os.path.basename(pdf_path),
                'pages': len(reader.pages),
                'content': pages_content,
                'metadata': {
                    'author': info.get('/Author', ''),
                    'creator': info.get('/Creator', ''),
                    'producer': info.get('/Producer', ''),
                    'subject': info.get('/Subject', ''),
                    'title': info.get('/Title', '')
                }
            }
            
            return content
    
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return {}
