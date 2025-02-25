import requests

def fetch(apiKey, username):
    url = f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={apiKey}&format=json&limit=1"
    response = requests.get(url)
    

    if response.status_code != 200:
        print(f"error: didn't fetch, the code or smth: {response.status_code}")
        print(f"Response: {response.text}")
        return

    data = response.json()


    if 'recenttracks' in data:
        print("=" * 40)
        print(f"{username}'s latest scrobble was:\n")
        track = data['recenttracks']['track'][0]
        print(f"Track: {track['name']}")
        print(f"Artist: {track['artist']['#text']}")
        print(f"Album: {track['album']['#text']}")
        print("=" * 40)
    else:
        print("error: recent tracks not found...")

def main(): 
    username = input("Username: ")
    apiKey = input("ApiKey: ")
    
    fetch(apiKey, username)

if __name__ == "__main__":
    main()
