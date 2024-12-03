#!/bin/bash

# Function to display a welcome message
show_welcome_image() {
    clear
    echo "Welcome to Student Management System!"
    sleep 2
}

# Function for user registration
register_user() {
    echo "Select Role to Register:"
    echo "1. Admin"
    echo "2. Teacher"
    echo "3. Student"
    read role_option

    case $role_option in
        1) role="admin" ;;
        2) role="teacher" ;;
        3) role="student" ;;
        *) echo "Invalid choice." ; return ;;
    esac

    echo "Enter Name:"
    read name
    echo "Enter ID:"
    read id
    echo "Enter Email:"
    read email
    echo "Enter Password:"
    read -s password

    # Store user data in users.csv
    echo "$id,$name,$password,$role" >> users.csv

    # Store role-specific data
    case $role in
        admin) echo "$id,$name,$email" >> admins.csv ;;
        teacher) echo "$id,$name,Subject,$email" >> teachers.csv ;;
        student)
            echo "Enter Semester:"
            read semester
            echo "$id,$name,$email,$semester" >> students.csv
            ;;
    esac

    echo "Registration successful!"
}

# Function for user login
login() {
    echo "Enter ID:"
    read id
    echo "Enter Password:"
    read -s password

    # Loop through users.csv to find the user with matching ID and password
    user_found=false
    while IFS=',' read -r csv_id csv_name csv_password csv_role; do
        # Trim spaces from csv_password and input password for comparison
        csv_password=$(echo "$csv_password" | xargs)  # Trim spaces
        password=$(echo "$password" | xargs)  # Trim spaces

        # Compare the ID and Password
        if [[ "$csv_id" == "$id" && "$csv_password" == "$password" ]]; then
            user_found=true
            role=$csv_role
            name=$csv_name
            break
        fi
    done < users.csv

    # If user is found, proceed with login
    if $user_found; then
        echo "Login successful as $role! Welcome, $name."
        
        # Navigate to role-specific menu
        case $role in
            admin) admin_menu ;;
            teacher) teacher_menu ;;
            student) student_menu ;;
            *) echo "Invalid role." ;;
        esac
    else
        echo "Invalid credentials, please try again."
    fi
}

# Admin Menu
admin_menu() {
    while true; do
        echo "Admin Menu"
        echo "1. Create Teacher"
        echo "2. View Teachers"
        echo "3. Create Semester"
        echo "4. Create Course"
        echo "5. View Students"
        echo "6. Delete Teacher"
        echo "7. Delete Student"
        echo "8. Logout"
        echo "Enter your choice:"
        read choice

        case $choice in
            1) create_teacher ;;
            2) view_teachers ;;
            3) create_semester ;;
            4) create_course ;;
            5) view_students ;;
            6) delete_teacher ;;
            7) delete_student ;;
            8) break ;;
            *) echo "Invalid choice, try again." ;;
        esac
    done
}

# Teacher Menu
teacher_menu() {
    while true; do
        echo "Teacher Menu"
        echo "1. View Students"
        echo "2. View Courses"
        echo "3. Logout"
        echo "Enter your choice:"
        read choice

        case $choice in
            1) view_students ;;
            2) view_courses ;;
            3) break ;;
            *) echo "Invalid choice, try again." ;;
        esac
    done
}

# Student Menu
student_menu() {
    while true; do
        echo "Student Menu"
        echo "1. View Info"
        echo "2. Logout"
        echo "Enter your choice:"
        read choice

        case $choice in
            1) search_student ;;
            2) break ;;
            *) echo "Invalid choice, try again." ;;
        esac
    done
}

# Functions for CRUD operations

# Create a new teacher
create_teacher() {
    echo "Enter Teacher ID:"
    read id
    echo "Enter Name:"
    read name
    echo "Enter Subject:"
    read subject
    echo "Enter Email:"
    read email
    echo "$id,$name,$subject,$email" >> teachers.csv
    echo "Teacher added successfully!"
}

# View all teachers
view_teachers() {
    cat teachers.csv
}

# Create a new semester
create_semester() {
    echo "Enter Semester ID:"
    read id
    echo "Enter Name:"
    read name
    echo "Enter Start Date (YYYY-MM-DD):"
    read start_date
    echo "Enter End Date (YYYY-MM-DD):"
    read end_date
    echo "$id,$name,$start_date,$end_date" >> semesters.csv
    echo "Semester added successfully!"
}

# Create a new course
create_course() {
    echo "Enter Course ID:"
    read id
    echo "Enter Course Name:"
    read course_name
    echo "Enter Teacher ID:"
    read teacher_id
    echo "$id,$course_name,$teacher_id" >> courses.csv
    echo "Course added successfully!"
}

# View all students
view_students() {
    cat students.csv
}

# View all courses
view_courses() {
    cat courses.csv
}

# Search for a student
search_student() {
    echo "Enter Student ID:"
    read student_id
    student_info=$(grep "$student_id" students.csv)

    if [ -n "$student_info" ]; then
        echo "Student Info: $student_info"
    else
        echo "Student not found."
    fi
}

# Delete a teacher from teachers.csv
delete_teacher() {
    echo "Enter Teacher ID to delete:"
    read teacher_id
    temp_file=$(mktemp)

    # Remove teacher from teachers.csv
    grep -v "^$teacher_id," teachers.csv > "$temp_file" && mv "$temp_file" teachers.csv
    echo "Teacher deleted successfully!"
}

# Delete a student from students.csv
delete_student() {
    echo "Enter Student ID to delete:"
    read student_id
    temp_file=$(mktemp)

    # Remove student from students.csv
    grep -v "^$student_id," students.csv > "$temp_file" && mv "$temp_file" students.csv
    echo "Student deleted successfully!"
}

# Show the main menu and allow the user to choose actions
show_menu() {
    echo "Main Menu"
    echo "1. Register"
    echo "2. Login"
    echo "3. Exit"
    read choice

    case $choice in
        1) register_user ;;
        2) login ;;
        3) exit 0 ;;
        *) echo "Invalid choice, try again." ;;
    esac
}

# Loop to keep the menu running until the user chooses to exit
while true; do
    show_menu
done
