import tkinter as tk
from tkinter import messagebox, font, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password-Protected To-Do List App")
        self.root.geometry("450x550")  # Set window size

        # Store tasks with statuses (whether completed or not)
        self.tasks = []

        # Common password for the "Track" button
        self.password = "karthi@2004"

        # Gradient background effect (using canvas)
        self.canvas = tk.Canvas(self.root, width=450, height=550)
        self.canvas.pack(fill="both", expand=True)

        # Create gradient background
        self.canvas.create_rectangle(0, 0, 450, 550, fill="#000000", outline="")

        # Frame for task widgets
        self.frame = tk.Frame(self.canvas, bg="#E6E6FA", relief="raised", borderwidth=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)

        # Heading
        self.heading_label = tk.Label(self.frame, text="To-Do List", font=("Helvetica", 18, "bold"), bg="light grey", fg="#34495E")
        self.heading_label.pack(pady=10)

        # Task entry widget with placeholder text
        self.task_entry = tk.Entry(self.frame, width=30, font=("Helvetica", 14), borderwidth=5, relief="sunken")
        self.task_entry.pack(pady=10)

        # Create buttons with rounded corners
        self.add_button = tk.Button(self.frame, text="Add Task", font=("Helvetica", 12), bg="#5DADE2", fg="white", relief="flat", command=self.add_task)
        self.add_button.pack(pady=5, ipadx=20)

        # Task Listbox with scrollbar
        self.listbox_frame = tk.Frame(self.frame)
        self.listbox_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(self.listbox_frame, width=50, height=10, font=("Helvetica", 12), yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE, relief="flat")
        self.task_listbox.pack(side=tk.LEFT)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Create control buttons
        self.control_frame = tk.Frame(self.frame, bg="white")
        self.control_frame.pack(pady=10)

        self.delete_button = tk.Button(self.control_frame, text="Delete", font=("Helvetica", 12), bg="#E74C3C", fg="white", relief="flat", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5, ipadx=20)

        self.track_button = tk.Button(self.control_frame, text="Track", font=("Helvetica", 12), bg="#F39C12", fg="white", relief="flat", command=self.track_task)
        self.track_button.pack(side=tk.LEFT, padx=5, ipadx=20)

        self.update_button = tk.Button(self.control_frame, text="Update", font=("Helvetica", 12), bg="#3498DB", fg="white", relief="flat", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5, ipadx=20)

        # Font for completed tasks
        self.completed_font = font.Font(self.task_listbox, self.task_listbox.cget("font"))
        self.completed_font.configure(slant="italic", overstrike=True)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False, 'visible': False})  # Hide task after adding
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def track_task(self):
        # Ask for the password first
        entered_password = simpledialog.askstring("Password", "Enter the password to track the tasks:", show='*')
        if entered_password == self.password:
            task_name = simpledialog.askstring("Track Task", "Enter the task name to track:")
            if task_name:
                found = False
                self.task_listbox.delete(0, tk.END)  # Clear the listbox before displaying
                for task in self.tasks:
                    if task['task'] == task_name:
                        found = True
                        task['visible'] = True  # Make task visible when tracked
                        self.task_listbox.insert(tk.END, task['task'])
                        messagebox.showinfo("Track Task", f"Task '{task_name}' found and revealed in the list.")
                        break
                if not found:
                    messagebox.showinfo("Track Task", f"Task '{task_name}' not found.")
        else:
            messagebox.showwarning("Incorrect Password", "The password you entered is incorrect.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index]['task'] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task name.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
