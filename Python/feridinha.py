import os
import requests
import inquirer

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

url = "https://feridinha.com/upload"

file_path = choose_file()

with open(file_path, 'rb') as f:
    files = {
        'file': f
    }

    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("Success!")
        response_data = response.json()
        print("File URL:", response_data['message'])
    else:
        print(f"Failed, error: {response.status_code}")
