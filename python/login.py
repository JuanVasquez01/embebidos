# login.py
import tkinter as tk
from tkinter import messagebox
from Interfaz import Interfaz

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        # Username label and entry
        self.username_label = tk.Label(root, text="Username")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        # Password label and entry
        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simple validation (replace with actual validation logic)
        if username == "admin" and password == "123":
            messagebox.showinfo("Login", "Login successful!")
            self.root.destroy()
            self.open_main_interface()
        else:
            messagebox.showerror("Login", "Invalid username or password")

    def open_main_interface(self):
        root = tk.Tk()
        interfaz = Interfaz(root)
        interfaz.mostrar_mensaje('Hola desde la interfaz')
        interfaz.iniciar()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
