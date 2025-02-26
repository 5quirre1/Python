# made by squirel

import requests
import time


settings_flags = {
    "nsfw": False,
    "religious": False,
    "political": False,
    "racist": False,
    "sexist": False,
    "explicit": False
}

def get_api_url():
    blacklist = [key for key, value in settings_flags.items() if value]
    blacklist_query = ",".join(blacklist)
    url = "https://v2.jokeapi.dev/joke/Any"
    if blacklist:
        url += f"?blacklistFlags={blacklist_query}"
    return url

def fetch_joke():
    url = get_api_url()
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        joke_data = response.json()
        
        if joke_data.get("error"):
            print("error: Could not fetch a joke.")
            return

        
        print(f"Category: {joke_data.get('category', 'Unknown')}\n")
        
        print("=" * 50)
        if joke_data.get("type") == "twopart":
            print(joke_data.get("setup", "No setup found"))
            time.sleep(2)
            print(joke_data.get("delivery", "No delivery found"))
        elif joke_data.get("type") == "single":
            print(joke_data.get("joke", "No joke found."))

        print("=" * 50)
        print("\n\n")
    except requests.RequestException as e:
        print(f"error fetching joke: {e}")
    
    time.sleep(2)

def settings():
    while True:
        print("\nSettings:")
        print("=" * 50)
        for key, value in settings_flags.items():
            print(f"{key.capitalize()}: {'ON' if value else 'OFF'}")
        print("=" * 50)
        print("Type the category to toggle it, or type 'back' to return.")

        option = input(">> ").strip().lower()
        if option == "back":
            break
        elif option in settings_flags:
            settings_flags[option] = not settings_flags[option]
            print(f"{option.capitalize()} is now {'ON' if settings_flags[option] else 'OFF'}.")
        else:
            print("uhh no option.")

def main():
    while True:
        print(":" *45)
        print("\t\tWelcome to joke           ")
        print(":" * 45)
        print("1. Get a Joke")
        print("2. Settings")
        print("3. Exit")
        option = input(">> ").strip().lower()

        match option:
            case "1":
                fetch_joke()
            case "2":
                settings()
            case "3":
                print("bai bai!")
                break
            case _:
                print("uhh no option.")

if __name__ == "__main__":
    main()
