from config import OUTPUT_DIR, DOWNLOAD_DIR
from pdf_scraper import scrape_pdf_links, download_pdf
from pdf_processor import process_pdf
from storage_handler import save_to_drive
from typing import List
import os

class DocumentAgent:
    def __init__(self):
        """Initialize the Document Agent"""
        self.processed_files = []
    
    def process_website(self, url: str) -> List[str]:
        """
        Process a website to extract and handle PDF documents.
        
        Args:
            url (str): The URL of the website to process
            
        Returns:
            List[str]: List of paths to the processed output files
        """
        # Scrape PDF links
        pdf_links = scrape_pdf_links(url)
        if not pdf_links:
            print(f"No PDF links found at {url}")
            return []
        
        output_files = []
        
        # Process each PDF
        for pdf_info in pdf_links:
            # Download PDF
            pdf_path = download_pdf(pdf_info, DOWNLOAD_DIR)
            if not pdf_path:
                continue
            
            # Process PDF content
            content = process_pdf(pdf_path)
            if not content:
                continue
            
            # Save processed content
            output_path = save_to_drive(content, OUTPUT_DIR)
            if output_path:
                output_files.append(output_path)
                self.processed_files.append({
                    'source_url': pdf_info['url'],
                    'local_path': pdf_path,
                    'output_path': output_path
                })
        
        return output_files

def main():
    """Main function to demonstrate usage"""
    agent = DocumentAgent()    # Example usage - Using arxiv.org as it's reliable and contains PDFs
    website_url = "https://sample-files.com/documents/pdf/"  # LangChain paper as an example
    print(f"\nProcessing website: {website_url}")
    processed_files = agent.process_website(website_url)
    
    print(f"\nProcessed {len(processed_files)} files:")
    for file in processed_files:
        print(f"- {file}")
    
    if not processed_files:
        print("\nTip: Make sure the website is accessible and contains PDF files.")

if __name__ == "__main__":
    main()
