# =========================================
# Project Name : NOVA - Python Assistant
# Developed By : Divay
# =========================================

import random
import datetime
import string

print("Hello Divay 👋")
print("I am Nova 🤖 - Your Python Assistant")
print("Type 'menu' to see available commands")

def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+ - * /): ")
        if op == "+": print("Result:", a+b)
        elif op == "-": print("Result:", a-b)
        elif op == "*": print("Result:", a*b)
        elif op == "/": print("Result:", a/b)
        else: print("Invalid operator")
    except:
        print("Invalid input")

def even_odd():
    n = int(input("Enter a number: "))
    print("Even" if n%2==0 else "Odd")

def table():
    n = int(input("Enter number: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def joke():
    print(random.choice(["Why do programmers love Python? Because it is easy!","Why was the computer cold? It left Windows open!"]))

def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits
    print("Password:", "".join(random.choice(chars) for _ in range(length)))

def show_date():
    print("Date:", datetime.datetime.now().strftime("%d-%m-%Y"))

def show_time():
    print("Time:", datetime.datetime.now().strftime("%H:%M:%S"))

def menu():
    print("calculator\nevenodd\ntable\njoke\npassword\ndate\ntime\nexit")

while True:
    cmd = input("Divay > ").lower()
    if cmd == "calculator": calculator()
    elif cmd == "evenodd": even_odd()
    elif cmd == "table": table()
    elif cmd == "joke": joke()
    elif cmd == "password": password_generator()
    elif cmd == "date": show_date()
    elif cmd == "time": show_time()
    elif cmd == "menu": menu()
    elif cmd == "exit": break
    else: print("Invalid command")
