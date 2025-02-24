import requests

def downloader(url, filename, show_progress=True):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                downloaded_size += len(chunk)
                if show_progress and total_size > 0:
                    print(f"Downloaded {downloaded_size / total_size * 100:.2f}%", end='\r')
        
        print(f"\nDownload complete: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

def main():
    url = input("Enter the URL of the file to download: ")
    filename = input("Enter the filename to save as: ")
    
    downloader(url, filename)
    
if __name__ == "__main__":
    main()
