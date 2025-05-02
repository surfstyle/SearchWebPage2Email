import sys
import requests
from bs4 import BeautifulSoup
import logging
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from the .env file

PATH = os.getenv('APP_PATH')

# Configure logging
logging.basicConfig(filename=PATH+'application.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_webpage(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching the webpage: {e}")
        return None

def search_keywords(content, keywords):
    lines = content.splitlines()
    keywords = [keyword.lower() for keyword in keywords]
    results = []

    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in keywords):
            start_index = max(0, i - 2)
            end_index = min(len(lines), i + 4)
            context_lines = lines[start_index:end_index]
            results.append('\n'.join(context_lines))
    
    return results

def save_results_to_file(results, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for result in results:
                file.write(result + '\n\n')
        logging.info(f"Results successfully saved to {file_path}")
    except IOError as e:
        logging.error(f"Error saving the results to file: {e}")

def main():
    if len(sys.argv) != 4:
        logging.error("Usage: python search.py <url> <keywords> <output_file>")
        sys.exit(1)

    url = sys.argv[1]
    keywords = sys.argv[2].split(',')
    output_file = sys.argv[3]

    content = fetch_webpage(url)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        text_content = soup.get_text()
        results = search_keywords(text_content, keywords)
        save_results_to_file(results, output_file)

if __name__ == "__main__":
    main()
