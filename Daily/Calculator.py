def add(x, y):
    answer = (y + x)
    return print(f"Answer is {answer}")
    
def sub(x, y):
    answer = (x - y)
    return print(f"Answer is {answer}")

def div(x, y):
    answer = (x / y)
    return print(f"Answer is {answer}")
    
def mul(x, y):
    answer = (x * y)
    return print(f"Answer is {answer}")
    
    
def main():
    try:
        while True:
            x = int(input("enter num for x: "))
            y = int(input("enter num for y: "))
            op = input("Enter the opertator: (+, /, *, -): ")
            if op == "+":
                add(x, y)
                
            elif op == "-":
                sub(x, y)
            elif op == "/":
                div(x, y)
            elif op == "*":
                mul(x, y)
            else:
                print("what")
                continue
    except ValueError:
        print("enter a number plz")
        main()
        
    
    
    
if __name__ == "__main__":
    main()
