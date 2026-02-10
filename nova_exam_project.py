import random
import datetime
import string

print("Hello Divay 👋")
print("I am Nova, your Python Assistant")
print("Type 'menu' to see all commands")



def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+ - * /): ")

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            print("Result:", a / b)
        else:
            print("Invalid operator")
    except:
        print("Error: Invalid input")

def even_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def table():
    n = int(input("Enter number for table: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def joke():
    jokes = [
        "Why do programmers love Python? Because it is simple!",
        "Why was the computer cold? It left Windows open!",
        "Why did the computer go to school? To improve its memory!"
    ]
    print(random.choice(jokes))

def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(chars)
    print("Generated Password:", password)

def show_date():
    print("Date:", datetime.datetime.now().strftime("%d-%m-%Y"))

def show_time():
    print("Time:", datetime.datetime.now().strftime("%H:%M:%S"))

def student_dictionary():
    student = {}
    student["name"] = input("Enter student name: ")
    student["roll"] = input("Enter roll number: ")
    student["course"] = input("Enter course: ")
    print("Student Details:", student)

def file_write():
    data = input("Enter text to save in file: ")
    with open("nova_data.txt", "w") as f:
        f.write(data)
    print("Data written to file successfully")

def file_read():
    try:
        with open("nova_data.txt", "r") as f:
            print("File Content:", f.read())
    except:
        print("File not found")

def menu():
    print("""
Commands:
calculator   - Calculator
evenodd      - Even or Odd
table        - Table Generator
joke         - Joke Teller
password     - Password Generator
date         - Show Date
time         - Show Time
student      - Dictionary Example
writefile    - File Write
readfile     - File Read
exit         - Exit Nova
""")



while True:
    cmd = input("\nDivay, enter command: ").lower()

    if cmd == "calculator":
        calculator()
    elif cmd == "evenodd":
        even_odd()
    elif cmd == "table":
        table()
    elif cmd == "joke":
        joke()
    elif cmd == "password":
        password_generator()
    elif cmd == "date":
        show_date()
    elif cmd == "time":
        show_time()
    elif cmd == "student":
        student_dictionary()
    elif cmd == "writefile":
        file_write()
    elif cmd == "readfile":
        file_read()
    elif cmd == "menu":
        menu()
    elif cmd == "exit":
        print("Goodbye Divay 👋 Nova closed.")
        break
    else:
        print("Invalid command. Type 'menu'.")
