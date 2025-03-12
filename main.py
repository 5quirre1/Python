import os

def count_files_in_folder(folder_path):
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)
    return file_count

def update_readme(readme_path, folder_info):
    with open(readme_path, 'r') as file:
        readme_content = file.read()

    updated_content = readme_content + "\n## Python programs total\n"
    
    for folder, count in folder_info.items():
        updated_content += f"- {folder}: {count} files\n"
    
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
