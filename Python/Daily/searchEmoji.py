emoji = {
    ":sob:": "😭",
    ":smile:": "😃",
    ":heart:": "❤️",
    ":broken_heart:": "💔",
    ":thumbsup:": "👍",
    ":fire:": "🔥",
    ":laughing:": "😆",
    ":confused:": "😕",
    ":cry:": "😢",
    ":sweat:": "😅",
    ":sweat_smile:": "😅",
    ":joy:": "😂",
    ":sunglasses:": "😎",
    ":star_struck:": "🤩",
    ":thinking:": "🤔",
    ":sleeping:": "😴",
    ":pensive:": "😔",
    ":grin:": "😁",
}

def search(searchInput):
    if (searchInput in emoji):
        print(emoji[searchInput])
    else:
        print("Not found..")
        main()
def main():
    print("put want you want to search")
    searchInput = input().lower()
    search(searchInput)

if __name__ == "__main__":
    main()
