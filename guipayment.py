import tkinter as tk
from tkinter import messagebox

def process_payment():
    payment_amount = amount_entry.get()
    payment_method = method_var.get()

    if payment_method == "Credit Card":
        messagebox.showinfo("Payment Confirmation", f"Paid ${payment_amount} via Credit Card")
    elif payment_method == "Mobile Wallet":
        messagebox.showinfo("Payment Confirmation", f"Paid ${payment_amount} via Mobile Wallet")
    else:
        messagebox.showerror("Error", "Please select a payment method.")

app = tk.Tk()
app.title("Payment System")

# Create and place widgets
amount_label = tk.Label(app, text="Enter Payment Amount ($):")
amount_label.pack()
amount_entry = tk.Entry(app)
amount_entry.pack()

method_label = tk.Label(app, text="Select Payment Method:")
method_label.pack()

method_var = tk.StringVar()
credit_card_radio = tk.Radiobutton(app, text="Credit Card", variable=method_var, value="Credit Card")
mobile_wallet_radio = tk.Radiobutton(app, text="Mobile Wallet", variable=method_var, value="Mobile Wallet")

credit_card_radio.pack()
mobile_wallet_radio.pack()

process_button = tk.Button(app, text="Process Payment", command=process_payment)
process_button.pack()

app.mainloop()
