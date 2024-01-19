import tkinter as tk
from tkinter import ttk
# credit card validation 
def calculate_card_checksum(card_number):
    total_sum = 0
    for i in range(len(card_number)-1, -1, -1):
        digit = int(card_number[i])
        if (len(card_number) - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
    return total_sum % 10

def luhn_algorithm(card_number):
    return calculate_card_checksum(card_number) == 0

def calculate_isbn_checksum(isbn):
    total_sum = 0
    for i in range(len(isbn)):
        digit = int(isbn[i])
        total_sum += digit if i % 2 == 0 else digit * 3
    return total_sum % 10

def authenticate_isbn(isbn):
    return calculate_isbn_checksum(isbn) == 0

def calculate_upc_checksum(upc):
    total_sum = 0
    for i in range(len(upc)):
        digit = int(upc[i])
        total_sum += digit * 3 if i % 2 == 0 else digit
    return (10 - total_sum % 10) % 10

def authenticate_upc(upc):
    return calculate_upc_checksum(upc) == 0

def authenticate():
    card_number = card_entry.get()
    isbn = isbn_entry.get()
    upc = upc_entry.get()

    card_result.set("Valid Visa/MasterCard" if luhn_algorithm(card_number) else "Invalid Visa/MasterCard")
    isbn_result.set("Valid ISBN" if authenticate_isbn(isbn) else "Invalid ISBN")
    upc_result.set("Valid UPC" if authenticate_upc(upc) else "Invalid UPC")

# GUI setup
root = tk.Tk()
root.title("Authentication System")

# Styles
style = ttk.Style()
style.theme_use("clam")  # Change the theme to "clam" (or another theme of your choice)

# Set a background color for the entire application
root.configure(bg="#f0f0f0")

# Card
card_label = ttk.Label(root, text="Enter Card Number:", font=("Helvetica", 12))
card_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
card_entry = ttk.Entry(root, font=("Helvetica", 12))
card_entry.grid(row=0, column=1, padx=10, pady=10)

# ISBN
isbn_label = ttk.Label(root, text="Enter ISBN:", font=("Helvetica", 12))
isbn_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
isbn_entry = ttk.Entry(root, font=("Helvetica", 12))
isbn_entry.grid(row=1, column=1, padx=10, pady=10)

# UPC
upc_label = ttk.Label(root, text="Enter UPC:", font=("Helvetica", 12))
upc_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
upc_entry = ttk.Entry(root, font=("Helvetica", 12))
upc_entry.grid(row=2, column=1, padx=10, pady=10)

# Authenticate Button
authenticate_button = ttk.Button(root, text="Authenticate", command=authenticate, style="TButton")
authenticate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Results
card_result = tk.StringVar()
isbn_result = tk.StringVar()
upc_result = tk.StringVar()

card_result_label = ttk.Label(root, textvariable=card_result, foreground="green", font=("Helvetica", 10, "bold"))
card_result_label.grid(row=4, column=0, columnspan=2, pady=5)

isbn_result_label = ttk.Label(root, textvariable=isbn_result, foreground="green", font=("Helvetica", 10, "bold"))
isbn_result_label.grid(row=5, column=0, columnspan=2, pady=5)

upc_result_label = ttk.Label(root, textvariable=upc_result, foreground="green", font=("Helvetica", 10, "bold"))
upc_result_label.grid(row=6, column=0, columnspan=2, pady=5)

# Add padding to all widgets
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()