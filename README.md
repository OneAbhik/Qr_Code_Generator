# QR Code Generator

Desktop app to generate QR codes from any URL. No ad-heavy websites. Built with Python, tkinter, qrcode, pillow.

![App Screenshot](image.png)

## Features
- Generate QR code from any URL or text
- Instant preview inside app
- Auto-save as `qrcode.png`
- Empty input validation with error popup
- Styled GUI with hover effect on button

## Tech Stack
- Python 3
- tkinter / ttk (GUI)
- qrcode (QR matrix generation)
- Pillow (image handling)

## Installation
```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
```

## Usage
```bash
python qr_generator.py
```
1. Enter URL in text box
2. Click **Generate QR Code**
3. Scan from screen with phone, or grab `qrcode.png` from project folder

## How It Works
- `qrcode.QRCode()` builds data matrix from input
- `make_image()` renders it to PIL image, saved as PNG
- `ImageTk.PhotoImage` converts it for tkinter label
- Image reference stored on label to avoid garbage collection

## Future Improvements
- Save As dialog
- Custom colors
- Logo in QR center
- Batch generation from file

## Author
**Aman** - Network Engineer | Python Automation
[GitHub](https://github.com/<username>)
