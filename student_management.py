import sqlite3

con = sqlite3.connect("students_data.db")

cursor = con.cursor()

cursor.execute('''
    create table if not exists students(
               Roll integer primary key,
               Name text not null,
               course char not null,
               contact number not null)

''')


def list_all_data():
    print("\n")
    print("*" * 70)
    cursor.execute("select * from students")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*" * 70)

def add_data(Roll,Name,course,contact):
   cursor.execute("insert into students (Roll,Name,course,contact) values (?,?,?,?)",(Roll,Name,course,contact))
   con.commit()

def update_data(Roll,new_name,new_course,new_contact):
    cursor.execute("Update students set Name = ?, course = ?, contact = ? where Roll = ?",(new_name,new_course,new_contact,Roll))
    con.commit()

def search_data(Roll):
    cursor.execute("select * from students where Roll =?",(Roll,))
    for row in cursor.fetchone():
        print(row)
    con.commit()

def delete_data(Roll):
    cursor.execute("Delete from students where Roll = ?",(Roll,))
    con.commit()


def main():
    while True:
        print("""
            ***** Student Management System *****
            Hello, how would you like to proceed?
            1. List all Student name
            2. Add Student data
            3. Update a Student data
            4. Search a student data
            5. Delete a student data
            6. Exit the App
            """)
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_data()
        elif choice =='2':
            Roll = int(input("Enter your Roll number: "))
            Name = input("Enter your name: ")
            course = input("Enter your course: ")
            contact = input("Enter your contact: ")
            add_data(Roll,Name,course,contact)
            print("\n")
            print("Your data has been added succesfully!")

        elif choice == "3":
            Roll = int(input("Enter your Roll number to update: "))
            new_name = input("Enter your name: ")
            new_course = input("Enter your course: ")
            new_contact = input("Enter your contact: ")
            update_data(Roll,new_name,new_course,new_contact)
            print("\n")
            print("Your data is updated succesfully!")

        elif choice == "4":
            Roll = int(input("Enter your Roll number to search: "))
            print("\n")
            print("*"* 70)
            search_data(Roll)
            print("\n")
            print("*"* 70)
        elif choice =="5":
            Roll = int(input("Enter your Roll number to delete: "))
            delete_data(Roll)
            print("\n")
            print("Your data is deleted!!")

        elif choice =="6":
            break
        else:
            print("Invalid Choice Selected!!")

    con.close()

if __name__ == "__main__":
    main()        