"""
This very shitty ass code was made by 5quirre1 lmfao
"""

import requests
import json

def get_username(token):
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["login"]
    else:
        print(f"Error: {response.status_code}, unable to fetch username.")
        return None

def get_repositories(username, token, visibility='all', sort='full_name'):
    url = f"https://api.github.com/users/{username}/repos?visibility={visibility}&sort={sort}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        if repos:
            print(f"\nRepositories for {username} ({visibility} visibility, sorted by {sort}):")
            for repo in repos:
                print(f"- {repo['name']} ({repo['visibility']}): {repo['html_url']}")
        else:
            print(f"No repositories found for {username} with {visibility} visibility.")
    else:
        print(f"Error: {response.status_code}, unable to fetch repositories.")

def create_issue(token, repo_name, title, body=""):
    username = get_username(token)
    if not username:
        return

    url = f"https://api.github.com/repos/{username}/{repo_name}/issues"
    headers = {"Authorization": f"token {token}"}
    data = {"title": title, "body": body}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        issue = response.json()
        print(f"Issue created: {issue['html_url']}")
    else:
        print(f"Error: {response.status_code}, unable to create issue.")

def fork_repository(token, repo_name):
    """Fork a repository."""
    username = get_username(token)
    if not username:
        return

    url = f"https://api.github.com/repos/{username}/{repo_name}/forks"
    headers = {"Authorization": f"token {token}"}
    response = requests.post(url, headers=headers)

    if response.status_code == 202:
        print(f"Repository {repo_name} successfully forked!")
    else:
        print(f"Error: {response.status_code}, unable to fork repository.")

def settings(token, repo_name, description="Updated repository description"):
    username = get_username(token)
    if not username:
        return

    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {"Authorization": f"token {token}"}
    data = {
        "description": description
    }
    response = requests.patch(url, json=data, headers=headers)

    if response.status_code == 200:
        repo = response.json()
        print(f"Repository settings updated: {repo['html_url']}")
    else:
        print(f"Error: {response.status_code}, Unable to update repository settings.")

def main():
    print("Welcome to the GitHub CLI!\n")
    token = input("Enter your GitHub personal access token: ")

    username = get_username(token)
    if not username:
        print("Failed to retrieve username.")
        return

    while True:
        print("\nChoose an action:")
        print("1. List repositories")
        print("2. Create an issue")
        print("3. Fork a repository")
        print("4. Update repository settings")
        print("5. Exit")

        choice = input(f"{username} >> ")

        if choice == "1":
            visibility = input("Enter visibility (all, public, private): ") or "all"
            sort = input("Enter sort order (created, updated, pushed, full_name): ") or "full_name"
            get_repositories(username, token, visibility, sort)

        elif choice == "2":
            repo_name = input("Enter the repository name: ")
            title = input("Enter the issue title: ")
            body = input("Enter the issue body (or leave empty): ")
            create_issue(token, repo_name, title, body)

        elif choice == "3":
            repo_name = input("Enter the repository name to fork: ")
            fork_repository(token, repo_name)

        elif choice == "4":
            repo_name = input("Enter the repository name to update: ")
            description = input("Enter new description (or leave empty): ") or "Updated repository description"
            settings(token, repo_name, description)

        elif choice == "5":
            print("Bai bai")
            break

        else:
            print("error: invalid")

if __name__ == "__main__":
    main()
