import time


def code():
    print("You can start coding now (type 'END' to finish)")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    code_string = "\n".join(lines)

    try:
        exec(code_string)
        time.sleep(2)
        print("Wanna do it again? (yes or no)")
        g = input().lower()
        if g == "yes":
            code()
        elif g == "no":
            print("bai bai!")
            exit()
        else:
            print("prob not then lmfao bai bai")
            exit()
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("Python in Python real")
    time.sleep(1)
    code()


if __name__ == "__main__":
    main()
