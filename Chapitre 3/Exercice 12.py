from tkinter import*

def fermer(event):
    root.destroy()

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{str(width)}x{str(height)}')
root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(bg="blue")

root.bind('<Escape>', fermer)

label = Label(root, text="""HEEEEEEIN ???""", bg='blue', fg='white', font=('', 75))
label.pack(expand=YES)

root.mainloop()