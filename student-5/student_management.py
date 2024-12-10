import tkinter as tk
from tkinter import messagebox
import csv
import os

# Ensure required files exist
# Ensure required files exist
def initialize_files():
    files = ['users.csv', 'admins.csv', 'teachers.csv', 'students.csv', 'courses.csv', 'semesters.csv', 'results.csv']
    for file in files:
        if not os.path.exists(file):
            with open(file, 'w', newline='') as f:
                writer = csv.writer(f)
                if file == 'users.csv':
                    writer.writerow(["ID", "Name", "Password", "Role"])
                elif file == 'admins.csv':
                    writer.writerow(["ID", "Name", "Email"])
                elif file == 'teachers.csv':
                    writer.writerow(["ID", "Name", "Subject", "Email"])
                elif file == 'students.csv':
                    writer.writerow(["ID", "Name", "Email", "Semester"])
                elif file == 'courses.csv':
                    writer.writerow(["Course ID", "Course Name", "Teacher ID"])
                elif file == 'semesters.csv':
                    writer.writerow(["Semester ID", "Semester Name", "Start Date", "End Date"])
                elif file == 'results.csv':
                    writer.writerow(["Student ID", "Course ID", "Grade"])

# Fetch courses based on student's semester

def view_courses(student_id):
    courses = []
    
    # Fetch the student's semester
    student_semester = None
    with open('students.csv', 'r') as students_file:
        reader = csv.reader(students_file)
        next(reader)  # Skip header row
        for student in reader:
            if student[0] == student_id:
                student_semester = student[3]
                break

    if not student_semester:
        messagebox.showinfo("No Semester", "Student's semester not found.")
        return

    # Now fetch courses for this semester
    with open('courses.csv', 'r') as courses_file:
        reader = csv.reader(courses_file)
        next(reader)  # Skip header row
        for row in reader:
            course_id, course_name, teacher_id, course_semester = row
            if course_semester == student_semester:
                courses.append(f"{course_id}: {course_name}")
    
    if courses:
        messagebox.showinfo("Courses", "\n".join(courses))
    else:
        messagebox.showinfo("No Courses", "No courses found for this student in the current semester.")


# View Result
def view_result(student_id):
    results = []
    with open('results.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[0] == student_id:
                course_id = row[1]
                grade = row[2]
                # Fetch course name from courses.csv
                with open('courses.csv', 'r') as courses_file:
                    courses_reader = csv.reader(courses_file)
                    next(courses_reader)  # Skip header row
                    for course in courses_reader:
                        if course[0] == course_id:
                            course_name = course[1]
                            results.append(f"{course_name}: {grade}")
    if results:
        messagebox.showinfo("Results", "\n".join(results))
    else:
        messagebox.showinfo("No Results", "No results found for this student.")

# View Semester
def view_semester(student_id):
    semester_info = None
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[0] == student_id:
                semester_id = row[3]
                # Fetch semester details from semesters.csv
                with open('semesters.csv', 'r') as semester_file:
                    semester_reader = csv.reader(semester_file)
                    next(semester_reader)  # Skip header row
                    for semester_row in semester_reader:
                        if semester_row[0] == semester_id:
                            semester_info = f"Semester: {semester_row[1]}\nStart Date: {semester_row[2]}\nEnd Date: {semester_row[3]}"
                            break
    if semester_info:
        messagebox.showinfo("Semester Info", semester_info)
    else:
        messagebox.showinfo("No Semester", "No semester info found for this student.")

# Student Menu
def student_menu(student_id):
    student_window = tk.Toplevel()
    student_window.title("Student Menu")
    
    # View Courses Button
    view_courses_button = tk.Button(student_window, text="View Courses", command=lambda: view_courses(student_id))
    view_courses_button.pack(pady=10)
    
    # View Results Button
    view_results_button = tk.Button(student_window, text="View Results", command=lambda: view_result(student_id))
    view_results_button.pack(pady=10)
    
    # View Semester Button
    view_semester_button = tk.Button(student_window, text="View Semester", command=lambda: view_semester(student_id))
    view_semester_button.pack(pady=10)
    
    # Logout Button
    logout_button = tk.Button(student_window, text="Logout", command=student_window.destroy)
    logout_button.pack(pady=10)


# User Registration
def register_user():
    role = role_var.get()
    name = name_entry.get()
    id = id_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not name or not id or not email or not password:
        messagebox.showerror("Error", "All fields are required")
        return
    
    # Save user data to users.csv
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, password, role])
    
    if role == "Admin":
        with open('admins.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, email])
    elif role == "Teacher":
        subject = subject_entry.get()  # Display subject field only for teachers
        if not subject:
            messagebox.showerror("Error", "Subject is required for Teacher registration")
            return
        with open('teachers.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, subject, email])
    elif role == "Student":
        semester = semester_var.get()  # Get selected semester from dropdown
        if not semester:
            messagebox.showerror("Error", "Semester is required for Student registration")
            return
        with open('students.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, email, semester])
    
    messagebox.showinfo("Success", f"{role} registration successful!")


# Login
def login():
    id = login_id_entry.get()
    password = login_password_entry.get()
    
    user_found = False
    student_id = None
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[0] == id and row[2] == password:
                user_found = True
                role = row[3]
                if role == "Student":
                    student_id = row[0]  # The student's ID
                break
    
    if user_found:
        messagebox.showinfo("Login Successful", f"Welcome {role}!")
        # Open respective role menu
        if role == "Admin":
            admin_menu()
        elif role == "Teacher":
            teacher_menu()
        elif role == "Student":
            student_menu(student_id)  # Pass the student ID to the student menu
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")


# Admin Menu
def admin_menu():
    admin_window = tk.Toplevel()
    admin_window.title("Admin Menu")
    
    # Create Teacher Function
    def create_teacher():
        teacher_id = teacher_id_entry.get()
        teacher_name = teacher_name_entry.get()
        subject = subject_entry.get()
        teacher_email = teacher_email_entry.get()

        if not teacher_id or not teacher_name or not subject or not teacher_email:
            messagebox.showerror("Error", "All fields are required")
            return
        
        with open('teachers.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([teacher_id, teacher_name, subject, teacher_email])
        
        messagebox.showinfo("Success", "Teacher created successfully!")
        teacher_id_entry.delete(0, tk.END)
        teacher_name_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
        teacher_email_entry.delete(0, tk.END)

    # View Teachers Function
    def view_teachers():
        teachers_list = []
        with open('teachers.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                teachers_list.append(f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}, Email: {row[3]}")
        
        if teachers_list:
            messagebox.showinfo("Teachers List", "\n".join(teachers_list))
        else:
            messagebox.showinfo("No Teachers", "No teachers found.")

    # Delete Teacher Function
    def delete_teacher():
        teacher_id = teacher_id_entry.get()
        
        if not teacher_id:
            messagebox.showerror("Error", "Teacher ID is required to delete")
            return
        
        teachers = []
        with open('teachers.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] != teacher_id:  # Keep all teachers except the one to be deleted
                    teachers.append(row)
        
        with open('teachers.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Subject", "Email"])  # Write header again
            writer.writerows(teachers)
        
        messagebox.showinfo("Success", f"Teacher with ID {teacher_id} has been deleted.")
        teacher_id_entry.delete(0, tk.END)
    
    # Create Student Function
    def create_student():
        student_id = student_id_entry.get()
        student_name = student_name_entry.get()
        student_email = student_email_entry.get()
        student_semester = student_semester_entry.get()

        if not student_id or not student_name or not student_email or not student_semester:
            messagebox.showerror("Error", "All fields are required")
            return
        
        with open('students.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, student_name, student_email, student_semester])
        
        messagebox.showinfo("Success", "Student created successfully!")
        student_id_entry.delete(0, tk.END)
        student_name_entry.delete(0, tk.END)
        student_email_entry.delete(0, tk.END)
        student_semester_entry.delete(0, tk.END)

    # View Students Function
    def view_students():
        students_list = []
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                students_list.append(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Semester: {row[3]}")
        
        if students_list:
            messagebox.showinfo("Students List", "\n".join(students_list))
        else:
            messagebox.showinfo("No Students", "No students found.")

    # Delete Student Function
    def delete_student():
        student_id = student_id_entry.get()

        if not student_id:
            messagebox.showerror("Error", "Student ID is required to delete")
            return

        students = []
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] != student_id:  # Keep all students except the one to be deleted
                    students.append(row)

        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Semester"])  # Write header again
            writer.writerows(students)

        messagebox.showinfo("Success", f"Student with ID {student_id} has been deleted.")
        student_id_entry.delete(0, tk.END)

    # Teacher Creation Fields
    teacher_id_label = tk.Label(admin_window, text="Teacher ID:")
    teacher_id_label.pack()
    teacher_id_entry = tk.Entry(admin_window)
    teacher_id_entry.pack()

    teacher_name_label = tk.Label(admin_window, text="Teacher Name:")
    teacher_name_label.pack()
    teacher_name_entry = tk.Entry(admin_window)
    teacher_name_entry.pack()

    teacher_email_label = tk.Label(admin_window, text="Teacher Email:")
    teacher_email_label.pack()
    teacher_email_entry = tk.Entry(admin_window)
    teacher_email_entry.pack()

    subject_label = tk.Label(admin_window, text="Subject:")
    subject_label.pack()
    subject_entry = tk.Entry(admin_window)
    subject_entry.pack()

    create_teacher_button = tk.Button(admin_window, text="Create Teacher", command=create_teacher)
    create_teacher_button.pack()

    view_teachers_button = tk.Button(admin_window, text="View Teachers", command=view_teachers)
    view_teachers_button.pack()

    delete_teacher_button = tk.Button(admin_window, text="Delete Teacher", command=delete_teacher)
    delete_teacher_button.pack()

    # Student Creation Fields
    student_id_label = tk.Label(admin_window, text="Student ID:")
    student_id_label.pack()
    student_id_entry = tk.Entry(admin_window)
    student_id_entry.pack()

    student_name_label = tk.Label(admin_window, text="Student Name:")
    student_name_label.pack()
    student_name_entry = tk.Entry(admin_window)
    student_name_entry.pack()

    student_email_label = tk.Label(admin_window, text="Student Email:")
    student_email_label.pack()
    student_email_entry = tk.Entry(admin_window)
    student_email_entry.pack()

    student_semester_label = tk.Label(admin_window, text="Student Semester:")
    student_semester_label.pack()
    student_semester_entry = tk.Entry(admin_window)
    student_semester_entry.pack()

    create_student_button = tk.Button(admin_window, text="Create Student", command=create_student)
    create_student_button.pack()

    view_students_button = tk.Button(admin_window, text="View Students", command=view_students)
    view_students_button.pack()

    delete_student_button = tk.Button(admin_window, text="Delete Student", command=delete_student)
    delete_student_button.pack()

    # Logout Button
    logout_button = tk.Button(admin_window, text="Logout", command=admin_window.destroy)
    logout_button.pack(pady=10)


# Teacher Menu
def teacher_menu():
    teacher_window = tk.Toplevel()
    teacher_window.title("Teacher Menu")
    
    # Actions for Teacher (view students, etc.)
    pass

# Student Menu
def student_menu(student_id):
    student_window = tk.Toplevel()
    student_window.title("Student Menu")
    
    # View Courses Button
    view_courses_button = tk.Button(student_window, text="View Courses", command=lambda: view_courses(student_id))
    view_courses_button.pack(pady=10)
    
    # View Results Button
    view_results_button = tk.Button(student_window, text="View Results", command=lambda: view_result(student_id))
    view_results_button.pack(pady=10)
    
    # View Semester Button
    view_semester_button = tk.Button(student_window, text="View Semester", command=lambda: view_semester(student_id))
    view_semester_button.pack(pady=10)
    
    # Logout Button
    logout_button = tk.Button(student_window, text="Logout", command=student_window.destroy)
    logout_button.pack(pady=10)

# Main Registration and Login Window
# Main Registration and Login Window
# Main Registration and Login Window
def main_window():
    global role_var, name_entry, id_entry, email_entry, password_entry, subject_entry, semester_entry
    global login_id_entry, login_password_entry, semester_dropdown, semester_var
    
    window = tk.Tk()
    window.title("Student-Teacher Management System")
    
    initialize_files()

    # Registration Frame
    register_frame = tk.Frame(window)
    register_frame.pack(pady=20)

    role_var = tk.StringVar(value="Student")  # Default role is Student
    
    tk.Label(register_frame, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(register_frame)
    name_entry.grid(row=0, column=1)

    tk.Label(register_frame, text="ID:").grid(row=1, column=0)
    id_entry = tk.Entry(register_frame)
    id_entry.grid(row=1, column=1)

    tk.Label(register_frame, text="Email:").grid(row=2, column=0)
    email_entry = tk.Entry(register_frame)
    email_entry.grid(row=2, column=1)

    tk.Label(register_frame, text="Password:").grid(row=3, column=0)
    password_entry = tk.Entry(register_frame, show="*")
    password_entry.grid(row=3, column=1)

    tk.Label(register_frame, text="Role:").grid(row=4, column=0)
    roles = ["Admin", "Teacher", "Student"]
    for i, role in enumerate(roles):
        tk.Radiobutton(register_frame, text=role, variable=role_var, value=role, command=update_role_fields).grid(row=4, column=i + 1)

    # Conditional fields for subject (Teacher) and semester (Student)
    subject_label = tk.Label(register_frame, text="Subject:")
    subject_entry = tk.Entry(register_frame)
    semester_label = tk.Label(register_frame, text="Semester:")
    
    # Predefined semesters (this could be dynamic, fetching from a file)
    semester_list = ["Spring 2024", "Fall 2024", "Spring 2025"]  # Example semesters
    semester_var = tk.StringVar()
    semester_var.set(semester_list[0])  # Default semester

    # Dropdown for semester selection
    semester_dropdown = tk.OptionMenu(register_frame, semester_var, *semester_list)

    # Initially hide these fields
    subject_label.grid_forget()
    subject_entry.grid_forget()
    semester_label.grid_forget()
    semester_dropdown.grid_forget()

    # Register button
    register_button = tk.Button(register_frame, text="Register", command=register_user)
    register_button.grid(row=6, column=0, columnspan=2)
    
    # Login Frame
    login_frame = tk.Frame(window)
    login_frame.pack(pady=20)

    tk.Label(login_frame, text="ID:").grid(row=0, column=0)
    login_id_entry = tk.Entry(login_frame)
    login_id_entry.grid(row=0, column=1)

    tk.Label(login_frame, text="Password:").grid(row=1, column=0)
    login_password_entry = tk.Entry(login_frame, show="*")
    login_password_entry.grid(row=1, column=1)

    login_button = tk.Button(login_frame, text="Login", command=login)
    login_button.grid(row=2, column=0, columnspan=2)

    window.mainloop()

def update_role_fields():
    # Hide both subject and semester fields by default
    subject_label.grid_forget()
    subject_entry.grid_forget()
    semester_label.grid_forget()
    semester_entry.grid_forget()

    # Show the subject field if Teacher is selected
    if role_var.get() == "Teacher":
        subject_label.grid(row=5, column=0)
        subject_entry.grid(row=5, column=1)
    # Show the semester dropdown if Student is selected
    elif role_var.get() == "Student":
        semester_label.grid(row=5, column=0)
        semester_dropdown.grid(row=5, column=1)  # Use dropdown for semester selection




# Run the program
main_window()
