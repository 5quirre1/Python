toDo = []
from datetime import datetime
class ToDo:
    def __init__(self, title, body, time):
        self.title = title
        self.body = body
        self.time = time

    def __str__(self):
        return f"{self.title} - {self.body} ({self.time})"


def add():
    title = input("Enter title: ")
    body = input("Enter description: ")
    time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    new_task = ToDo(title, body, time)
    toDo.append(new_task)
    print("Task added!")


def delete():
    if not toDo:
        print("no tasks.")
        return

    view()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(toDo):
            removed = toDo.pop(index)
            print(f"Deleted: {removed.title}")
        else:
            print("what")
    except ValueError:
        print("Do a number.")


def view():
    if not toDo:
        print("No tasks")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(toDo, start=1):
        print(f"{i}. {task}")


def main():
    while True:
        print("\nTodo Program")
        print("1: Add Task\n2: Delete Task\n3: View Tasks\n4: Exit")
        option = input(">>> ")

        match option:
            case "1":
                add()
            case "2":
                delete()
            case "3":
                view()
            case "4":
                print("bai")
                break
            case _:
                print("no")


if __name__ == "__main__":
    main()
