import json
import subprocess
import logging
import sys
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from the .env file

#Parameter in command line
#CONFIG_FILE = 'config_xyz.json'

PATH = os.getenv('APP_PATH')

# Configure logging
logging.basicConfig(filename=PATH+'application.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def read_config(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except IOError as e:
        logging.error(f"Error reading the config file: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        logging.error("Usage: python start.py <config_xyz>")
        sys.exit(1)

    config_file = sys.argv[1]
    config = read_config(PATH+config_file)
    #print("...."+PATH+config_file)
    if config:
        url = config.get('URL')
        keywords = config.get('KEYWORDS')
        output_file = config.get('OUTPUT_FILE')
        email_from = config.get('EMAIL-FROM')
        email_to = config.get('EMAIL-TO')
        email_subject = config.get('EMAIL-SUBJECT')

        if url and keywords and output_file and email_from and email_to and email_subject:
            subprocess.run(['python3', PATH+'search.py', url, ','.join(keywords), output_file])
            subprocess.run(['python3', PATH+'notify.py', email_from, email_to, email_subject, output_file, url])
        else:
            logging.error("Configuration file is missing required fields.")
    else:
        logging.error("Failed to load configuration.")

if __name__ == "__main__":
    main()
