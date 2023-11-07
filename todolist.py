import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
        else:
            raise ValueError("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 0 < task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority
        else:
            raise ValueError("Invalid task index.")

    def remove_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            return removed_task.description
        else:
            raise ValueError("Invalid task index.")

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.todo_list = ToDoList()

        self.create_gui()

    def create_gui(self):
        self.description_label = tk.Label(self.root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()

        self.due_date_label = tk.Label(self.root, text="Due Date (optional):")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.pack()

        self.priority_label = tk.Label(self.root, text="Priority (optional):")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(self.root)
        self.priority_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.display_button = tk.Button(self.root, text="Display Tasks", command=self.display_tasks)
        self.display_button.pack()

        self.mark_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_task)
        self.mark_button.pack()

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        try:
            self.todo_list.add_task(description, due_date, priority)
            self.output_text.insert(tk.END, "Task added successfully.\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_tasks(self):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "To-Do List:\n")
        for index, task in enumerate(self.todo_list.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            self.output_text.insert(tk.END, f"{index}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Status: {status}\n")

    def mark_task(self):
        task_index = self.get_task_index()
        if task_index is not None:
            try:
                self.todo_list.mark_completed(task_index)
                self.output_text.insert(tk.END, f"Task {task_index} marked as completed.\n")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def update_task(self):
        task_index = self.get_task_index()
        if task_index is not None:
            new_description = self.description_entry.get()
            new_due_date = self.due_date_entry.get()
            new_priority = self.priority_entry.get()
            try:
                self.todo_list.update_task(task_index, new_description, new_due_date, new_priority)
                self.output_text.insert(tk.END, f"Task {task_index} updated successfully.\n")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def remove_task(self):
        task_index = self.get_task_index()
        if task_index is not None:
            try:
                removed_description = self.todo_list.remove_task(task_index)
                self.output_text.insert(tk.END, f"Task '{removed_description}' removed from the list.\n")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def get_task_index(self):
        try:
            task_index = int(self.description_entry.get())
            if task_index < 1 or task_index > len(self.todo_list.tasks):
                raise ValueError("Invalid task index.")
            return task_index
        except ValueError:
            messagebox.showerror("Error", "Invalid task index.")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
