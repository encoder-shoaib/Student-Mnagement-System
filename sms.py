import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to check if a user exists
def user_exists(user_id, password):
    try:
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_id and row[2] == password:
                    return row[3]  # return role if found
    except FileNotFoundError:
        return None
    return None

# Function to register a new user
def register_user(role, user_id, name, email, password, semester=None):
    try:
        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([user_id, name, password, role])

        # Store role-specific data
        if role == "admin":
            with open("admins.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([user_id, name, email])
        elif role == "teacher":
            with open("teachers.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([user_id, name, "Subject", email])
        elif role == "student":
            with open("students.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([user_id, name, email, semester])
        
        messagebox.showinfo("Registration", f"{role.capitalize()} registered successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while registering: {e}")

# Login Screen
def login_screen():
    login_window = tk.Tk()
    login_window.title("Login - Student Management System")

    def handle_login():
        user_id = entry_id.get()
        password = entry_password.get()
        role = user_exists(user_id, password)
        
        if role:
            messagebox.showinfo("Login Successful", f"Welcome {role}!")
            login_window.destroy()
            if role == "admin":
                admin_menu()
            elif role == "teacher":
                teacher_menu()
            elif role == "student":
                student_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid ID or Password")
    
    tk.Label(login_window, text="User ID:").pack(pady=5)
    entry_id = tk.Entry(login_window)
    entry_id.pack(pady=5)
    
    tk.Label(login_window, text="Password:").pack(pady=5)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack(pady=5)

    tk.Button(login_window, text="Login", command=handle_login).pack(pady=10)
    tk.Button(login_window, text="Register", command=lambda: registration_screen()).pack(pady=5)
    login_window.mainloop()

# Registration Screen
def registration_screen():
    reg_window = tk.Tk()
    reg_window.title("Register - Student Management System")

    def register_action():
        role = role_var.get()
        user_id = entry_id.get()
        name = entry_name.get()
        email = entry_email.get()
        password = entry_password.get()
        semester = entry_semester.get() if role == "student" else None
        
        register_user(role, user_id, name, email, password, semester)
        reg_window.destroy()
        login_screen()

    tk.Label(reg_window, text="User ID:").pack(pady=5)
    entry_id = tk.Entry(reg_window)
    entry_id.pack(pady=5)
    
    tk.Label(reg_window, text="Name:").pack(pady=5)
    entry_name = tk.Entry(reg_window)
    entry_name.pack(pady=5)
    
    tk.Label(reg_window, text="Email:").pack(pady=5)
    entry_email = tk.Entry(reg_window)
    entry_email.pack(pady=5)
    
    tk.Label(reg_window, text="Password:").pack(pady=5)
    entry_password = tk.Entry(reg_window, show="*")
    entry_password.pack(pady=5)
    
    tk.Label(reg_window, text="Semester (if student):").pack(pady=5)
    entry_semester = tk.Entry(reg_window)
    entry_semester.pack(pady=5)

    role_var = tk.StringVar(value="admin")
    tk.Label(reg_window, text="Role:").pack(pady=5)
    tk.Radiobutton(reg_window, text="Admin", variable=role_var, value="admin").pack(pady=5)
    tk.Radiobutton(reg_window, text="Teacher", variable=role_var, value="teacher").pack(pady=5)
    tk.Radiobutton(reg_window, text="Student", variable=role_var, value="student").pack(pady=5)

    tk.Button(reg_window, text="Register", command=register_action).pack(pady=10)
    reg_window.mainloop()

# Admin Menu
def admin_menu():
    admin_window = tk.Tk()
    admin_window.title("Admin Menu - Student Management System")
    
    def create_teacher():
        pass  # Implement teacher creation logic here
    
    tk.Label(admin_window, text="Admin Menu").pack(pady=10)
    tk.Button(admin_window, text="Create Teacher", command=create_teacher).pack(pady=5)
    tk.Button(admin_window, text="View Teachers", command=lambda: view_teachers()).pack(pady=5)
    tk.Button(admin_window, text="Logout", command=admin_window.quit).pack(pady=5)
    admin_window.mainloop()

# Teacher Menu
def teacher_menu():
    teacher_window = tk.Tk()
    teacher_window.title("Teacher Menu - Student Management System")
    
    def view_students():
        pass  # Implement viewing students logic here

    tk.Label(teacher_window, text="Teacher Menu").pack(pady=10)
    tk.Button(teacher_window, text="View Students", command=view_students).pack(pady=5)
    tk.Button(teacher_window, text="Logout", command=teacher_window.quit).pack(pady=5)
    teacher_window.mainloop()

# Student Menu
def student_menu():
    student_window = tk.Tk()
    student_window.title("Student Menu - Student Management System")

    def view_info():
        pass  # Implement student info viewing logic here

    tk.Label(student_window, text="Student Menu").pack(pady=10)
    tk.Button(student_window, text="View Info", command=view_info).pack(pady=5)
    tk.Button(student_window, text="Logout", command=student_window.quit).pack(pady=5)
    student_window.mainloop()

# Main Entry Point
def main():
    if not os.path.exists("users.csv"):
        with open("users.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["user_id", "name", "password", "role"])

    login_screen()

# Run the main function
if __name__ == "__main__":
    main()
