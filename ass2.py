import tkinter as tk
from tkinter import messagebox

# Functions for arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        messagebox.showerror("Error", "Division by zero is not allowed")
        return None

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        if result is not None:
            result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and set variables
operation_var = tk.StringVar(value="Add")
result_var = tk.StringVar()

# Create GUI components
label1 = tk.Label(root, text="Enter first number:")
label2 = tk.Label(root, text="Enter second number:")
label_result = tk.Label(root, text="Result:")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry_result = tk.Entry(root, textvariable=result_var, state="readonly")

radio_add = tk.Radiobutton(root, text="Add", variable=operation_var, value="Add")
radio_subtract = tk.Radiobutton(root, text="Subtract", variable=operation_var, value="Subtract")
radio_multiply = tk.Radiobutton(root, text="Multiply", variable=operation_var, value="Multiply")
radio_divide = tk.Radiobutton(root, text="Divide", variable=operation_var, value="Divide")

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_exit = tk.Button(root, text="Exit", command=root.quit)

# Place GUI components using grid layout
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

radio_add.grid(row=2, column=0, padx=10, pady=5)
radio_subtract.grid(row=2, column=1, padx=10, pady=5)
radio_multiply.grid(row=3, column=0, padx=10, pady=5)
radio_divide.grid(row=3, column=1, padx=10, pady=5)

button_calculate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
label_result.grid(row=5, column=0, padx=10, pady=10)
entry_result.grid(row=5, column=1, padx=10, pady=10)

button_exit.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
