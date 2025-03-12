import requests
import inquirer
import base64


def get_github_repo_contents(repo_url):
    repo_parts = repo_url.rstrip('/').split('/')
    owner = repo_parts[-2]
    repo = repo_parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("failed.. check link..")
        return None


def get_file_content(file_url):
    response = requests.get(file_url)
    
    if response.status_code == 200:
        content = response.json()
        file_content = base64.b64decode(content['content']).decode('utf-8')
        return file_content
    else:
        print("failed to get content")
        return None


def list_files_and_folders(files):
    choices = []
    for file in files:
        choices.append({
            'name': f"{file['name']}/" if file['type'] == 'dir' else file['name'],
            'value': file
        })

    questions = [
        inquirer.List('file',
                      message="Select a file or folder",
                      choices=choices,
                      ),
    ]
    answer = inquirer.prompt(questions)
    return answer['file']


def navigate_back(previous_dirs):
    if previous_dirs:
        return previous_dirs.pop()
    else:
        print("no previous folder to go back to..")
        return None


def main():
    repo_url = input("Enter the GitHub repository URL: ")

    repo_contents = get_github_repo_contents(repo_url)

    previous_dirs = []

    if repo_contents:
        while True:
            selected = list_files_and_folders(repo_contents)

            if selected['type'] == 'dir':
                previous_dirs.append(repo_contents)
                print(f"Listing contents of folder: {selected['name']}")
                repo_contents = get_github_repo_contents(selected['url'])
            else:
                print(f"You selected file: {selected['name']}")
                file_content = get_file_content(selected['url'])
                if file_content:
                    print(f"--- Contents of {selected['name']} ---\n")
                    print(file_content[:500])
                    view_more = inquirer.confirm("Would you like to see more of the file?", default=True)
                    if view_more:
                        print(file_content[500:])
                    break
                else:
                    print(f"error retrieving content for {selected['name']}.")
                    break
            
            go_back = inquirer.confirm("Do you want to go back to the previous folder?", default=False)
            if go_back:
                repo_contents = navigate_back(previous_dirs)
                if not repo_contents:
                    break
    else:
        print("repo contents failed load..")


if __name__ == "__main__":
    main()
