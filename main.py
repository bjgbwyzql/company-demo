from todo import add_task, list_tasks, complete_task


def show_menu():
    print("\n=== Todo App ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            text = input("Task: ").strip()
            add_task(text)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            index = int(input("Task number: "))
            complete_task(index)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

