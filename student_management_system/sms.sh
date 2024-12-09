#!/bin/bash

# Ensure required files exist
initialize_files() {
    touch users.csv admins.csv teachers.csv students.csv courses.csv semesters.csv
}

# Show Welcome Message
show_welcome_image() {
    zenity --info --text="Welcome to the Student Management System!" --title="Welcome" --width=400
}

# User Registration
register_user() {
    role=$(zenity --list --radiolist --title="Select Role" --text="Choose a role to register:" \
        --column="Select" --column="Role" \
        TRUE "Admin" FALSE "Teacher" FALSE "Student" --width=400 --height=300)

    if [ -z "$role" ]; then
        zenity --error --text="Role not selected." --width=300
        return
    fi

    name=$(zenity --entry --title="Enter Name" --text="Enter your name:")
    id=$(zenity --entry --title="Enter ID" --text="Enter your ID:")
    email=$(zenity --entry --title="Enter Email" --text="Enter your email:")
    password=$(zenity --password --title="Enter Password" --text="Enter a password:")

    # Store user data
    echo "$id,$name,$password,$role" >> users.csv

    case $role in
        "Admin") echo "$id,$name,$email" >> admins.csv ;;
        "Teacher") 
            subject=$(zenity --entry --title="Enter Subject" --text="Enter subject specialization:")
            echo "$id,$name,$subject,$email" >> teachers.csv ;;
        "Student")
            semester=$(zenity --entry --title="Enter Semester" --text="Enter your semester:")
            echo "$id,$name,$email,$semester" >> students.csv ;;
    esac

    zenity --info --text="Registration successful!" --width=300
}

# User Login
login() {
    id=$(zenity --entry --title="Enter ID" --text="Enter your ID:")
    password=$(zenity --password --title="Enter Password" --text="Enter your password:")

    user_found=false
    while IFS=',' read -r csv_id csv_name csv_password csv_role; do
        if [[ "$csv_id" == "$id" && "$csv_password" == "$password" ]]; then
            user_found=true
            role=$csv_role
            name=$csv_name
            break
        fi
    done < users.csv

    if $user_found; then
        zenity --info --text="Login successful as $role! Welcome, $name." --width=400
        case $role in
            "Admin") admin_menu ;;
            "Teacher") teacher_menu ;;
            "Student") student_menu ;;
        esac
    else
        zenity --error --text="Invalid credentials. Please try again." --width=300
    fi
}

# Admin Menu
admin_menu() {
    while true; do
        choice=$(zenity --list --radiolist --title="Admin Menu" --text="Choose an action:" \
            --column="Select" --column="Action" \
            TRUE "Create Teacher" FALSE "View Teachers" \
            FALSE "Create Semester" FALSE "Create Course" \
            FALSE "View Students" FALSE "Logout" --width=400 --height=300)

        case $choice in
            "Create Teacher") create_teacher ;;
            "View Teachers") view_teachers ;;
            "Create Semester") create_semester ;;
            "Create Course") create_course ;;
            "View Students") view_students ;;
            "Logout") break ;;
        esac
    done
}

# Teacher Menu
teacher_menu() {
    while true; do
        choice=$(zenity --list --radiolist --title="Teacher Menu" --text="Choose an action:" \
            --column="Select" --column="Action" \
            TRUE "View Students" FALSE "View Courses" FALSE "Logout" --width=400 --height=300)

        case $choice in
            "View Students") view_students ;;
            "View Courses") view_courses ;;
            "Logout") break ;;
        esac
    done
}

# Student Menu
student_menu() {
    while true; do
        choice=$(zenity --list --radiolist --title="Student Menu" --text="Choose an action:" \
            --column="Select" --column="Action" \
            TRUE "View Info" FALSE "Logout" --width=400 --height=300)

        case $choice in
            "View Info") search_student ;;
            "Logout") break ;;
        esac
    done
}

# CRUD Operations
create_teacher() {
    id=$(zenity --entry --title="Enter Teacher ID" --text="Enter Teacher ID:")
    name=$(zenity --entry --title="Enter Name" --text="Enter Teacher Name:")
    subject=$(zenity --entry --title="Enter Subject" --text="Enter Subject Specialization:")
    email=$(zenity --entry --title="Enter Email" --text="Enter Email:")
    echo "$id,$name,$subject,$email" >> teachers.csv
    zenity --info --text="Teacher added successfully!" --width=300
}

view_teachers() {
    zenity --text-info --title="Teachers List" --filename=teachers.csv --width=600 --height=400
}

create_semester() {
    id=$(zenity --entry --title="Enter Semester ID" --text="Enter Semester ID:")
    name=$(zenity --entry --title="Enter Semester Name" --text="Enter Semester Name:")
    start_date=$(zenity --entry --title="Enter Start Date" --text="Enter Start Date (YYYY-MM-DD):")
    end_date=$(zenity --entry --title="Enter End Date" --text="Enter End Date (YYYY-MM-DD):")
    echo "$id,$name,$start_date,$end_date" >> semesters.csv
    zenity --info --text="Semester added successfully!" --width=300
}

create_course() {
    id=$(zenity --entry --title="Enter Course ID" --text="Enter Course ID:")
    name=$(zenity --entry --title="Enter Course Name" --text="Enter Course Name:")
    teacher_id=$(zenity --entry --title="Enter Teacher ID" --text="Enter Teacher ID:")
    echo "$id,$name,$teacher_id" >> courses.csv
    zenity --info --text="Course added successfully!" --width=300
}

view_students() {
    zenity --text-info --title="Students List" --filename=students.csv --width=600 --height=400
}

view_courses() {
    zenity --text-info --title="Courses List" --filename=courses.csv --width=600 --height=400
}

search_student() {
    student_id=$(zenity --entry --title="Search Student" --text="Enter Student ID:")
    student_info=$(grep "$student_id" students.csv)
    if [ -n "$student_info" ]; then
        zenity --info --title="Student Info" --text="Student Details:\n$student_info" --width=400
    else
        zenity --error --text="Student not found!" --width=300
    fi
}

# Main Menu
main_menu() {
    choice=$(zenity --list --radiolist --title="Main Menu" --text="Choose an option:" \
        --column="Select" --column="Action" \
        TRUE "Register" FALSE "Login" FALSE "Exit" --width=400 --height=300)

    case $choice in
        "Register") register_user ;;
        "Login") login ;;
        "Exit") exit 0 ;;
    esac
}

# Initialize required files
initialize_files

# Main Loop
show_welcome_image
while true; do
    main_menu
done
