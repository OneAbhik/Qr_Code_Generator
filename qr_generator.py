import tkinter as tk
from tkinter import ttk, messagebox

import qrcode
from PIL import Image, ImageTk

BG = "#D6EAF8"
BTN = "#2E86C1"
BTN_ACTIVE = "#1B4F72"


def generate_qr_code():
    url = entry_url.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    qr_image = Image.open("qrcode.png")
    qr_image_tk = ImageTk.PhotoImage(qr_image)

    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk  # keep reference, else garbage collected


root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background=BG, font=("Segoe UI", 11))
style.configure(
    "TButton",
    background=BTN,
    foreground="white",
    font=("Segoe UI", 11, "bold"),
    padding=8,
)
style.map(
    "TButton",
    background=[("active", BTN_ACTIVE), ("!active", BTN)],
)

ttk.Label(root, text="Enter URL to generate QR code:").pack(pady=(20, 8))

entry_url = ttk.Entry(root, width=35)
entry_url.pack(pady=5)
entry_url.focus()
entry_url.bind("<Return>", lambda e: generate_qr_code())

ttk.Button(root, text="Generate QR Code", command=generate_qr_code).pack(pady=15)

qr_label = ttk.Label(root)
qr_label.pack(pady=10)

root.mainloop()