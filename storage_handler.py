import os
import json
from datetime import datetime

def save_to_drive(content: dict, output_dir: str, filename: str = None) -> str:
    """
    Save processed content to a shared drive location.
    
    Args:
        content (dict): The processed content to save
        output_dir (str): Directory to save the content
        filename (str, optional): Custom filename. Defaults to None.
        
    Returns:
        str: Path to the saved file
    """
    try:
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"processed_{timestamp}.json"
        
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
        
        return filepath
    
    except Exception as e:
        print(f"Error saving content: {e}")
        return ""
