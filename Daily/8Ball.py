import random
import time
import os

def get_answer():
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    return random.choice(answers)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    print("Welcome to the Magic 8-Ball!")
    time.sleep(1)

    while True:
        question = input("\nAsk a question (or type 'exit' to quit): ").strip()
        
        if question.lower() == "exit":
            print("\nThanks for playing! Bai bai!")
            break
        elif not question:
            print("try again")
            continue
        
        print("\nThinking..")
        time.sleep(2)
        print(f"8Ball says: {get_answer()}")

if __name__ == "__main__":
    main()
