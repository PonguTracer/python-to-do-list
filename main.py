from colorama import Fore, Style

def print_colored(text, color='white'):
    colors = {
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'purple': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'reset': Style.RESET_ALL
    }
    print(f'{colors[color]}{text}{colors["reset"]}')

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print_colored(f'Task "{task}" added successfully.', color='green')

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print_colored(f'Task "{task}" deleted successfully.', color='red')
        else:
            print(f'Task "{task}" not found.', color='yellow')

    def view_tasks(self):
        if self.tasks:
            print_colored("Your To-Do List:", color='cyan')
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")
    def print_colored(text, color='white'):
        colors = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'purple': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'reset': '\033[0m'
        }
        print(f'{colors[color]}{text}{colors["reset"]}')

def main():
    to_do_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Delete Task\n3. View Tasks\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)

        elif choice == "2":
            task = input("Enter the task to delete: ")
            to_do_list.delete_task(task)

        elif choice == "3":
            to_do_list.view_tasks()

        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
