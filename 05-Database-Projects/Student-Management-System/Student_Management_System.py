import mysql.connector

# Connect to MySQL Server (Initial Connection without DB)
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

# Initialize Advanced Dictionary Cursor
mycursor = mydb.cursor(dictionary=True)

# Create Database and Switch to it
mycursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
mycursor.execute("USE student_db")

# Create 'students' Table with Constraints
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INT PRIMARY KEY AUTO_INCREMENT, 
        roll_no INT UNIQUE NOT NULL, 
        name VARCHAR(50) NOT NULL, 
        course VARCHAR(50) NOT NULL, 
        city VARCHAR(50)
    )
""")

# Function to Insert a New Student Record
def insert():
    print('\n\t\tInsert Student Records\n')
    try:
        # Taking inputs from user
        rollNum = int(input('Enter student Roll Number : '))
        name = input('Enter student name : ')
        course = input('Enter student course :')
        city = input('Enter student city : ')
        
        # Safe query block using parameterized inputs
        sql = "INSERT INTO students(roll_no, name, course, city) VALUES(%s, %s, %s, %s)"
        val = (rollNum, name, course, city)
        mycursor.execute(sql, val)
        
        # FIX: Added commit immediately to save data permanently on disk
        mydb.commit()
        print(f'\n\t\tInsert Record(s) {mycursor.rowcount} Successfully!')
        
    except ValueError:
        print('\n\t\tError : Enter valid student roll number (Digit) ')
    except Exception as e:
        print(f" Error : {e}")

# Function to Dynamically Update Specific Fields of a Student Record
def update():
    print('\n\t\tUpdate Student Records\n')
    try:
        rollNum = int(input('Enter student roll number which you want to update: '))
        
        # Check if student exists before updating
        mycursor.execute("SELECT * FROM students WHERE roll_no = %s", (rollNum,))
        student = mycursor.fetchone()
        
        if not student:
            print('\n\t\tError : Student roll number not found!')
            return
        
        # Display current data
        print(f"Current Data -> Name: {student['name']} | Course: {student['course']} | City: {student['city']}")
        print("\nWhat do you want to update?")
        print("1. Update Name")
        print("2. Update Course")
        print("3. Update City")
        sub_choice = input("Enter choice (1/2/3): ")
        
        # Dynamic Query Selection based on user choice
        if sub_choice == '1':
            new_name = input("Enter new name: ")
            sql = "UPDATE students SET name = %s WHERE roll_no = %s"
            val = (new_name, rollNum)
        elif sub_choice == '2':
            new_course = input("Enter new course: ")
            sql = "UPDATE students SET course = %s WHERE roll_no = %s"
            val = (new_course, rollNum)
        elif sub_choice == '3':
            new_city = input("Enter new city: ")
            sql = "UPDATE students SET city = %s WHERE roll_no = %s"
            val = (new_city, rollNum)
        else:
            print("\n\t\tInvalid choice! Update cancelled.")
            return

        # Execute dynamic update and save changes
        mycursor.execute(sql, val)
        mydb.commit()
        print(f'\n\t\tUpdate Record(s) {mycursor.rowcount} Successfully!')

    except ValueError:
        print('\n\t\tError : Enter valid student roll number (Digit) ')
    except Exception as e:
        print(f" Error : {e}")

# Function to Read and Display All Student Records
def show():
    print('\n\t\tDisplaying All Student Records\n')
    mycursor.execute("SELECT * FROM students")
    studentDetails = mycursor.fetchall()
    
    # Check if table is empty
    if not studentDetails:
        print('\n\t\tNo records found in the database!')
        return
        
    # Loop through list of dictionaries and print using keys
    for student in studentDetails:
        print(f"\t\t{student['id']}\t{student['roll_no']}\t{student['name']}\t{student['course']}\t{student['city']}")
    print(f'\n\t\tSelect Record(s) {mycursor.rowcount}')

# Function to Delete a Student Record Permanently (Hard Delete)
def delete():
    print('\n\t\tDelete Student Records\n')
    try:
        rollNum = int(input('Which you want to delete records.., Enter student roll number : '))
        
        # Check if student exists before deleting
        mycursor.execute("SELECT * FROM students WHERE roll_no = %s", (rollNum,))
        student = mycursor.fetchone()
        
        if not student:
            print('\n\t\tError : Student roll number not found!')
            return
        
        print(f"Current Data -> Name: {student['name']} | Course: {student['course']} | City: {student['city']}")

        # Execute Delete Query
        mycursor.execute("DELETE FROM students WHERE roll_no = %s", (rollNum,))
        
        # FIX: Added commit immediately to free disk block and save deletion
        mydb.commit()
        print(f'\n\t\tDelete Record(s) {mycursor.rowcount} Successfully!')
        
    except ValueError:
         print('\n\t\tError : Enter valid student roll number (Digit) ')
    except Exception as e:
        print(f" Error : {e}")    
        
# Main Application Loop Interface
while True:
    print("\n========================= MAIN MENU =========================")
    menuChoice = input("1. Insert Record\n2. Update Record\n3. Show Record\n4. Delete Record\n5. Exit\nEnter your choice -----> ")
    
    if menuChoice == '1':
        insert()
    elif menuChoice == '2':
        update()
    elif menuChoice == '3':
        show()
    elif menuChoice == '4':
        delete()
    elif menuChoice == '5':
        print("\nThank you for using Student Management System. Goodbye!")
        break # Cleaner than exit() for terminating a while loop safely
    else:
        print('\n\t\tError: Enter a valid menu choice (1-5)\n')