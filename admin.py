import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymongo as pym

def admin_panel(name):
    window = tk.Tk()
    window.title("Password Manager Admin")
    window.geometry("1300x750")
    window.configure(bg = "#45aaf2")
    
    photo = tk.PhotoImage(file="Logo_PassManager.png")
    label_photo = tk.Label(image=photo ,bg="#45aaf2",).grid(row=0, column=1, padx=10)

    def logout():
        ans = tk.messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if ans:
            window.destroy()
            import main

    def openAdd():
        from add import add_credentials
        add_credentials(name)
    def openUpdate():
        from update import update_credentials
        update_credentials(name)
    def openDelete():
        from delete import del_credentials
        del_credentials(name)

    btnAdd = tk.Button(window, text = "Add",command=openAdd, width=10, font=("Poppins", 16)).grid(row=10,column = 0,padx=10,pady=10)
    btnUpdate = tk.Button(window, text = "Update",command=openUpdate, width=10, font=("Poppins", 16)).grid(row=10,column = 1, padx=(0, 40), pady=10, ipadx=20)
    btnDelete = tk.Button(window, text = "Delete",command=openDelete, width=10, font=("Poppins", 16)).grid(row=10,column = 2,padx=(
        0,120), pady=10)
    btnLogout = tk.Button(window, text = "Logout", command = logout, width=10, font=("Poppins", 16)).grid(row=10,column = 3, padx=10,pady=10)


    window.mainloop()
