import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os
from dotenv import load_dotenv

load_dotenv() # Load environmePATHnt variables from the .env file

PATH = os.getenv('APP_PATH')

SMTP_SERVER = os.getenv('APP_SMTP_SERVER')
SMTP_PORT = os.getenv('APP_SMTP_PORT')

# Configure logging
logging.basicConfig(filename=PATH+'application.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def invia_email(destinatario, mittente, soggetto, corpo, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = mittente
    msg['To'] = destinatario
    msg['Subject'] = soggetto
    msg.attach(MIMEText(corpo, 'plain'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)			
            server.send_message(msg)
							
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def leggi_file_e_invia_email(file_path, destinatario, mittente, soggetto, smtp_username, smtp_password, url):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            righe = file.readlines()
        
        if righe:            
            righe.append('\n------------------------------\nURL Website: \n' + url)
            corpo = ''.join(righe)
            invia_email(destinatario, mittente, soggetto, corpo, smtp_username, smtp_password)
        else:
            logging.info("The file is empty, no email sent.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 6:
        logging.error("Usage: python notification_program.py <email_from> <email_to> <email_subject> <file_path> <url>")
        sys.exit(1)

    email_from = sys.argv[1]
    email_to = sys.argv[2]
    email_subject = sys.argv[3]
    file_path = sys.argv[4]					 
    url = sys.argv[5]
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    smtp_username = os.getenv('APP_SMTP_USERNAME')
    smtp_password = os.getenv('APP_SMTP_PASSWORD')

    leggi_file_e_invia_email(file_path, email_to, email_from, email_subject, smtp_username, smtp_password, url)

if __name__ == "__main__":
    main()
