# main.py
import os
from src.generator import build_from_markdown

def init_folders():
    """Creates necessary folders if they don't exist."""
    folders = ['assets', 'output']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

if __name__ == "__main__":
    init_folders()
    
    print("🚀 Starting Document Generation...")
    output_file = "output/Maximo_9_Training_Guide.docx"
    
    try:
        build_from_markdown('docs', output_file)
        print(f"✅ Success! File saved at: {output_file}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")