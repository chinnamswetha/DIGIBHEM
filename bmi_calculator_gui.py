import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def calculate_and_display_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_label.config(text=f"Your BMI is: {bmi:.2f}\nBMI Category: {category}")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place the widgets
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)

weight_entry = tk.Entry(root)
height_entry = tk.Entry(root)

weight_entry.grid(row=0, column=1, padx=10, pady=5)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_display_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
