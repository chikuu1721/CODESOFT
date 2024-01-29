import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Mark Task as Completed button
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        # Populate tasks from file
        self.load_tasks_from_file()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, False))
            self.task_listbox.insert(tk.END, task)
            self.save_tasks_to_file()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("ERROR", "Please enter a task.")

    def save_tasks_to_file(self):
        with open("tasks.txt", "w") as file:
            for task, is_completed in self.tasks:
                file.write(f"{task},{is_completed}\n")
                
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
            self.save_tasks_to_file()
        except IndexError:
            messagebox.showwarning("ERROR", "Please select a task to delete.")

    def mark_as_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task, is_completed = self.tasks[selected_index]
            self.tasks[selected_index] = (task, True)
            self.task_listbox.itemconfig(selected_index, bg="light green")
            self.save_tasks_to_file()
        except IndexError:
            messagebox.showwarning("ERROR", "Please select a task to mark as completed.")

    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file.readlines():
                    task, is_completed = line.strip().split(',')
                    self.tasks.append((task, is_completed == "True"))
                    self.task_listbox.insert(tk.END, task)
                    if is_completed == "True":
                        index = len(self.tasks) - 1
                        self.task_listbox.itemconfig(index, bg="light green")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()
