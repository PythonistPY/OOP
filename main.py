class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not completed"
        return f"Task: {self.description}, Due date: {self.due_date}, Status: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.mark_as_completed()
                return True
        return False

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Finish homework", "2024-08-21")
    manager.add_task("Buy groceries", "2024-08-22")

    # Вывод текущих задач
    print("Current tasks:")
    for task in manager.get_current_tasks():
        print(task)

    # Отметка задачи как выполненной
    manager.mark_task_as_completed("Finish homework")

    # Вывод задач после выполнения
    print("\nTasks after marking 'Finish homework' as completed:")
    for task in manager.get_current_tasks():
        print(task)



