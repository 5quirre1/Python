import requests

def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io/json')
        response.raise_for_status()
        ip_info = response.json()
        return ip_info
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    ip_info = get_ip_info()
    if isinstance(ip_info, dict):
        print(f"IP Address: {ip_info.get('ip', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
    else:
        print(ip_info)
