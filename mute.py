def main():
    isMuted = False
    greg = "mute a person or smth idfk\n"
    while True:
        
        print(greg)
        mute = input().lower()
        if (mute == "mute"):
            if (isMuted == True):
                print("Already muted")
            else:
                isMuted = True
        elif (mute == "unmute"):
            if (isMuted == False):
                print("Already not muted\n")
            else:
                isMuted = False
            
        if (isMuted):
            greg = "\nmuted"
        else:
            greg = "no mute\n"
if __name__ == "__main__":
    main()
