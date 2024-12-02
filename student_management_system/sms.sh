#!/bin/bash

# Function to create a teacher record
create_teacher() {
    echo "Enter Teacher ID:"
    read id
    echo "Enter Teacher Name:"
    read name
    echo "Enter Teacher Subject:"
    read subject
    echo "$id,$name,$subject" >> teachers.csv
    echo "Teacher added successfully!"
}

# Function to view all teachers
view_teachers() {
    echo "Teachers List:"
    cat teachers.csv
}

# Function to delete a teacher record
delete_teacher() {
    echo "Enter Teacher ID to delete:"
    read id
    sed -i "/$id/d" teachers.csv
    echo "Teacher deleted successfully!"
}

# Function to create a student record
create_student() {
    echo "Enter Student ID:"
    read id
    echo "Enter Student Name:"
    read name
    echo "Enter Student Age:"
    read age
    echo "Enter Student Class:"
    read class
    echo "$id,$name,$age,$class" >> students.csv
    echo "Student added successfully!"
}

# Function to view all students
view_students() {
    echo "Students List:"
    cat students.csv
}

# Function to search for a student by ID
search_student() {
    echo "Enter Student ID to search:"
    read id
    grep "$id" students.csv
}

# Function to create a semester record
create_semester() {
    echo "Enter Semester ID:"
    read id
    echo "Enter Semester Name:"
    read name
    echo "Enter Semester Start Date (YYYY-MM-DD):"
    read start_date
    echo "Enter Semester End Date (YYYY-MM-DD):"
    read end_date
    echo "$id,$name,$start_date,$end_date" >> semesters.csv
    echo "Semester added successfully!"
}

# Function to view all semesters
view_semesters() {
    echo "Semesters List:"
    cat semesters.csv
}

# Function to create a course record
create_course() {
    echo "Enter Course ID:"
    read id
    echo "Enter Course Name:"
    read name
    echo "Enter Teacher ID for this course:"
    read teacher_id
    echo "$id,$name,$teacher_id" >> courses.csv
    echo "Course added successfully!"
}

# Function to view all courses
view_courses() {
    echo "Courses List:"
    cat courses.csv
}

# Function to delete a student record
delete_student() {
    echo "Enter Student ID to delete:"
    read id
    sed -i "/$id/d" students.csv
    echo "Student deleted successfully!"
}

# Main menu function to display options
show_menu() {
    echo "----------------------------"
    echo "Student Management System"
    echo "----------------------------"
    echo "1. Create Teacher"
    echo "2. View Teachers"
    echo "3. Delete Teacher"
    echo "4. Create Student"
    echo "5. View Students"
    echo "6. Search Student Info"
    echo "7. Create Semester"
    echo "8. View Semesters"
    echo "9. Create Course"
    echo "10. View Courses"
    echo "11. Delete Student"
    echo "12. Exit"
    echo "Enter your choice:"
    read choice
    case $choice in
        1) create_teacher ;;
        2) view_teachers ;;
        3) delete_teacher ;;
        4) create_student ;;
        5) view_students ;;
        6) search_student ;;
        7) create_semester ;;
        8) view_semesters ;;
        9) create_course ;;
        10) view_courses ;;
        11) delete_student ;;
        12) exit ;;
        *) echo "Invalid choice. Try again." ;;
    esac
}

# Loop to keep the menu running until the user chooses to exit
while true
do
    show_menu
done

