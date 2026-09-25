import tkinter as tk
import ctypes
from ctypes import wintypes
root = tk.Tk()
root.title("Price Calculator")
root.geometry("450x500")
root.overrideredirect(True)
root.configure(bg="#F5F5F5")
title_bar = tk.Frame(root, bg="#2C3E50", height=35)
title_bar.pack(fill="x")
title_text = tk.Label(
    title_bar,
    text="Price Calculator",
    bg="#2C3E50",
    fg="white",
    font=("Arial", 10, "bold")
)
title_text.pack(side="left", padx=12)
def minimize_window():
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    ctypes.windll.user32.ShowWindow(hwnd, 6)
minimize_button = tk.Button(
    title_bar,
    text="—",
    command=minimize_window,
    bg="#2C3E50",
    fg="white",
    bd=0,
    font=("Arial", 11, "bold")
)
minimize_button.pack(side="right", padx=(8, 25))
minimize_button.bind("<Enter>", lambda e: minimize_button.config(bg="#3D566E"))
minimize_button.bind("<Leave>", lambda e: minimize_button.config(bg="#2C3E50"))
close_button = tk.Button(
    title_bar,
    text="✕",
    command=root.destroy,
    bg="#2C3E50",
    fg="white",
    bd=0,
    font=("Arial", 11, "bold")
)
close_button.pack(side="right", padx=8)
close_button.bind("<Enter>", lambda e: close_button.config(bg="#E81123"))
close_button.bind("<Leave>", lambda e: close_button.config(bg="#2C3E50"))
def start_move(event):
    root.x = event.x
    root.y = event.y
def do_move(event):
    x = root.winfo_x() + event.x - root.x
    y = root.winfo_y() + event.y - root.y
    root.geometry(f"+{x}+{y}")


title_bar.bind("<Button-1>", start_move)
title_bar.bind("<B1-Motion>", do_move)
     
# Title
title_label = tk.Label(
    root,
    text="PRICE CALCULATOR",
    font=("Arial", 18, "bold"),
    bg="#F5F5F5",fg="#222222",
)
title_label.pack(pady=15)

# Price

price_label = tk.Label(root, text="Enter Price:", font=("Arial", 11, "bold"), bg="#F5F5F5")
price_label.pack()
def validate_price(value):
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

vcmd = (root.register(validate_price), "%P")

price_entry = tk.Entry()
price_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=20,
    justify="center",
    relief="solid",
    bd=1,
    validate="key",
    validatecommand=vcmd
)
price_entry.pack()

# Tax Rate
tax_rate_label = tk.Label(root, text="Tax Rate (%):", font=("Arial", 11, "bold"), bg="#F5F5F5")
tax_rate_label.pack(pady=(10, 0))

tax_rate_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=20,
    justify="center",
    relief="solid",
    bd=1,
    validate="key",
    validatecommand=vcmd
)
tax_rate_entry.insert(0, "13")
tax_rate_entry.pack()
def validate_price(value):
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

# Calculate
def calculate():
    try:
        price = float(price_entry.get())
        tax = float(tax_rate_entry.get()) / 100
    except ValueError:
        subtotal_label.config(text="")
        
        result_label.config(
            text="Please enter a valid price and tax rate",
            font=("Arial", 10, "normal")
        )
        return

    tax_amount = price * tax
    total = price + tax_amount

    subtotal_label.config(text=f"Subtotal: ${price:.2f}")
    tax_label.config(text=f"Tax: ${tax_amount:.2f}")
    result_label.config(
        text=f"Total: ${total:.2f}",
        font=("Arial", 14, "bold")
    )
price_entry.bind("<Return>", lambda event: calculate())

# Clear
def clear():
    price_entry.delete(0, tk.END)

    tax_rate_entry.delete(0, tk.END)
    tax_rate_entry.insert(0, "13")

    subtotal_label.config(text="")
    tax_label.config(text="")
    result_label.config(text="")
    price_entry.focus_set()

# Three buttons side by side
buttons_frame = tk.Frame(root, bg="#F5F5F5")
buttons_frame.pack(pady=20)
calculate_button = tk.Button(
    buttons_frame,
    text="Calculate",
    command=calculate,
    font=("Arial", 11, "bold"),
    width=10,
    height=2,
    bg="#2E7D32",
    fg="white",
    relief="raised",
    bd=4,
    activebackground="#1B5E20",
    activeforeground="white"
)
calculate_button.pack(side="left", padx=8)
clear_button = tk.Button(
    buttons_frame,
    text="Clear",
    command=clear,
    font=("Arial", 11, "bold"),
    width=10,
    height=2,
    bg="#1976D2",
    fg="white",
        relief="raised",
    bd=4,
    activebackground="#0D47A1",
    activeforeground="white"
    
    
)
clear_button.pack(side="left", padx=8)
exit_button = tk.Button(
    buttons_frame,
    text="Exit",
    command=lambda: root.after(10, root.destroy),
    font=("Arial", 11, "bold"),
    width=10,
    height=2,
    bg="#D32F2F",
    fg="white",
        relief="raised",
    bd=4,
    activebackground="#0D47A1",
    activeforeground="white"
    
)
exit_button.pack(side="left", padx=8)
subtotal_label = tk.Label(root, text="", font=("Arial", 12), bg="#F5F5F5")
subtotal_label.pack(pady=2)
tax_label = tk.Label(root, text="", font=("Arial", 12), bg="#F5F5F5")
tax_label.pack(pady=2)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#F5F5F5")
result_label.pack(pady=5)
root.update_idletasks()
hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
DWMWA_WINDOW_CORNER_PREFERENCE = 33
DWMWCP_ROUND = ctypes.c_int(2)
ctypes.windll.dwmapi.DwmSetWindowAttribute(
    hwnd,
    DWMWA_WINDOW_CORNER_PREFERENCE,
    ctypes.byref(DWMWCP_ROUND),
    ctypes.sizeof(DWMWCP_ROUND)
)

width = root.winfo_width()
height = root.winfo_height()
region = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, width, height, 40, 40)
ctypes.windll.user32.SetWindowRgn(hwnd, region, True)
price_entry.focus_set()
root.mainloop()
