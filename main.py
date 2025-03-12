"""
Made by Squirrel (5quirre1) Gay Acorns

This updates the README with the current count of the programs in the Daily folder and Python folder.
"""

import os
import re

def count_files_in_folder(folder_path):
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)
    return file_count

def update_readme(readme_path, folder_info):
    with open(readme_path, 'r') as file:
        readme_content = file.read()

    updated_content = re.sub(
        r"## Python programs total\n(.*?)(?=\n##|\Z)",
        lambda match: "## Python programs total\n" + "\n".join(
            [f"- {folder}: {count} files" for folder, count in folder_info.items()]
        ),
        readme_content,
        flags=re.DOTALL
    )

    if updated_content == readme_content:
        updated_content += "\n## Python programs total\n"
        updated_content += "\n".join([f"- {folder}: {count} files" for folder, count in folder_info.items()])

    with open(readme_path, 'w') as file:
        file.write(updated_content)

def main():
    folders = ['Daily', 'Python']

    folder_info = {}
    for folder in folders:
        file_count = count_files_in_folder(folder)
        folder_info[folder] = file_count

    readme_path = 'README.md'
    update_readme(readme_path, folder_info)

if __name__ == "__main__":
    main()
