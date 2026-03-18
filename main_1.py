import customtkinter as ctk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FILE = "tasks.json"

class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("800x600")
        self.minsize(400, 500)

        self.tasks = []
        self.load_tasks()

        self.container = ctk.CTkFrame(self, corner_radius=15)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.container.grid_rowconfigure(2, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkLabel(
            self.container,
            text="My Tasks",
            font=("Segoe UI", 28, "bold")
        )
        self.header.grid(row=0, column=0, pady=(15, 10))

        self.input_frame = ctk.CTkFrame(self.container)
        self.input_frame.grid(row=1, column=0, padx=15, pady=10, sticky="ew")

        self.input_frame.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter a new task..."
        )
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.add_btn = ctk.CTkButton(
            self.input_frame,
            text="Add",
            width=80,
            command=self.add_task
        )
        self.add_btn.grid(row=0, column=1, padx=10)

        self.list_frame = ctk.CTkScrollableFrame(self.container)
        self.list_frame.grid(row=2, column=0, padx=15, pady=10, sticky="nsew")

        self.actions = ctk.CTkFrame(self.container)
        self.actions.grid(row=3, column=0, padx=15, pady=10, sticky="ew")

        self.actions.grid_columnconfigure((0,1), weight=1)

        self.delete_btn = ctk.CTkButton(
            self.actions,
            text="X",
            fg_color="#d9534f",
            hover_color="#c9302c",
            command=self.delete_task
        )
        self.delete_btn.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

        self.done_btn = ctk.CTkButton(
            self.actions,
            text="okay",
            fg_color="#5cb85c",
            hover_color="#449d44",
            command=self.mark_done
        )
        self.done_btn.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        self.selected_index = None

        self.refresh_list()

    def add_task(self):
        #text = self.entry.get().strip()
        #if text:
        text = self.entry.get()
        self.tasks.append({"text": text, "done": False})
        self.entry.delete(0, "end")
        self.save_tasks()
        self.refresh_list()


    # def delete_task(self):
    #     if self.selected_index is not None:
    #         confirm = messagebox.askyesno(
    #             "Confirm delete",
    #             "Are you sure you want to delete this task?"
    #         )

    #         if confirm:
    #             self.tasks.pop(self.selected_index)
    #             self.selected_index = None
    #             self.save_tasks()
    #             self.refresh_list()

    def delete_task(self):
        # if self.selected_index is not None:
        #     self.tasks.pop(self.selected_index)
        #     self.selected_index = None
        #     self.save_tasks()
        #     self.refresh_list()
        if self.tasks:
            self.tasks.pop()  
            self.save_tasks()
            self.refresh_list()

    def mark_done(self):
        if self.selected_index is not None:
            self.tasks[self.selected_index]["done"] = True
            self.save_tasks()
            self.refresh_list()

    def select_task(self, index):
        self.selected_index = index
        self.refresh_list()

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = ctk.CTkFrame(self.list_frame, corner_radius=10)
            frame.pack(fill="x", pady=5, padx=5)

            #color = "#2a2d2e" if i != self.selected_index else "#3a7ebf"
            color = "#2a2d2e"
            frame.configure(fg_color=color)

            text = ("✔ " if task["done"] else "") + task["text"]

            label = ctk.CTkLabel(
                frame,
                text=text,
                anchor="w"
            )
            label.pack(side="left", padx=10, pady=10, fill="x", expand=True)

            frame.bind("<Button-1>", lambda e, idx=i: self.select_task(idx))
            label.bind("<Button-1>", lambda e, idx=i: self.select_task(idx))

    def save_tasks(self):
        with open(FILE, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                self.tasks = json.load(f)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()