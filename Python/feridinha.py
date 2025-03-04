import os
import requests
try:
    import inquirer
except ImportError:
    os.system("pip install inquirer")
    import inquirer
import sys
import time
import threading

def choose_file():
    media_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mp3', '.wav', '.ogg', '.flv', '.mkv']

    file_choices = [f for f in os.listdir('.') if os.path.isfile(f) and any(f.lower().endswith(ext) for ext in media_extensions)]

    if not file_choices:
        print("No media files found...")
        exit(1)

    questions = [
        inquirer.List('file',
                      message="Select a media file to upload",
                      choices=file_choices,
                      ),
    ]

    answers = inquirer.prompt(questions)
    if answers is None:
        print("Cancelled.")
        exit(1)
    return answers['file']


def loading_spinner():
    spinner = ['|', '/', '-', '\\']
    while True:
        for symbol in spinner:
            sys.stdout.write(f'\rUploading {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)

url = "https://feridinha.com/upload"

file_path = choose_file()


spinner_thread = threading.Thread(target=loading_spinner)
spinner_thread.daemon = True
spinner_thread.start()

with open(file_path, 'rb') as f:
    files = {
        'file': f
    }

    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("\rSuccess!                 ")
        response_data = response.json()
        print("File URL:", response_data['message'])
    else:
        print(f"\rFailed, error: {response.status_code}             ") 
