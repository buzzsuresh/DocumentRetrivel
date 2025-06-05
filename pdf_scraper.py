from bs4 import BeautifulSoup, Tag
import requests
import os
from typing import List, Dict
from urllib.parse import urljoin

def scrape_pdf_links(url: str) -> List[Dict[str, str]]:
    """
    Scrape PDF links from a given webpage or handle direct PDF URLs.
    
    Args:
        url (str): The URL of the webpage to scrape or direct PDF URL
        
    Returns:
        List[Dict[str, str]]: List of dictionaries containing PDF info (url and filename)
    """
    try:
        # Check if the URL is a direct PDF link
        if url.lower().endswith('.pdf'):
            return [{
                'url': url,
                'filename': os.path.basename(url)
            }]

        # If not a direct PDF, scrape the webpage for PDF links
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        pdf_links = []
        for link in soup.find_all('a'):
            if isinstance(link, Tag):
                href = link.get('href', '')
                if href and isinstance(href, str) and href.lower().endswith('.pdf'):
                    absolute_url = urljoin(url, href)
                    filename = os.path.basename(absolute_url)
                    pdf_links.append({
                        'url': absolute_url,
                        'filename': filename
                    })
        
        return pdf_links
    
    except requests.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []

def download_pdf(pdf_info: Dict[str, str], download_dir: str) -> str:
    """
    Download a PDF file from the given URL with progress tracking and validation.
    
    Args:
        pdf_info (Dict[str, str]): Dictionary containing PDF info
        download_dir (str): Directory to save the downloaded PDF
        
    Returns:
        str: Path to the downloaded file or empty string if download fails
    """
    try:
        # Setup headers for better compatibility
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/pdf,*/*'
        }
        
        # Make the request with headers and stream enabled
        response = requests.get(pdf_info['url'], stream=True, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Get the content length if available
        total_size = int(response.headers.get('content-length', 0))
        
        filepath = os.path.join(download_dir, pdf_info['filename'])
        
        # Create directory if it doesn't exist
        os.makedirs(download_dir, exist_ok=True)
        
        # Download with progress tracking
        downloaded_size = 0
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    if total_size > 0:
                        progress = (downloaded_size / total_size) * 100
                        print(f"\rDownloading {pdf_info['filename']}: {progress:.1f}%", end='')
        
        print()  # New line after progress
        
        # Validate the downloaded file
        if os.path.getsize(filepath) < 100:  # Basic size check
            print(f"Warning: Downloaded file {pdf_info['filename']} seems too small")
            return ""
            
        # Check if it's a valid PDF
        try:
            with open(filepath, 'rb') as f:
                if not f.read(4).startswith(b'%PDF'):
                    print(f"Warning: {pdf_info['filename']} does not appear to be a valid PDF")
                    os.remove(filepath)
                    return ""
        except Exception:
            print(f"Error validating PDF file {pdf_info['filename']}")
            return ""
        
        return filepath
    
    except requests.RequestException as e:
        print(f"Error downloading {pdf_info['url']}: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error downloading {pdf_info['filename']}: {e}")
        return ""
