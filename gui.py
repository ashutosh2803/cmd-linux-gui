import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modules import calModule, dateModule, initModule, installModule, pwdModule, mkdirModule

root = tk.Tk()
root.title("Option Selection")

# Create a styled frame
frame = ttk.Frame(root, padding=20)
frame.pack()

# Create a styled label
label = ttk.Label(frame, text="Select an Option:", font=("Helvetica", 14))
label.pack()

option1 = ttk.Button(frame, text="Calender", command=calModule)
option2 = ttk.Button(frame, text="Date", command=dateModule)
option3 = ttk.Button(frame, text="init Package", command=initModule)
option4 = ttk.Button(frame, text="Package Installation", command=installModule)
option5 = ttk.Button(frame, text="Print Working Directory", command=pwdModule)
option6 = ttk.Button(frame, text="Create a New Folder", command=mkdirModule)

# Add some styling to the buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

# Pack the widgets into the window
option1.pack(pady=5)
option2.pack(pady=5)
option3.pack(pady=5)
option4.pack(pady=5)
option5.pack(pady=5)
option6.pack(pady=5)

root.mainloop()
