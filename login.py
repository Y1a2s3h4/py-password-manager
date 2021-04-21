import tkinter as tk
from tkinter import messagebox
import pymongo as pym

window = tk.Tk()
window.title("Password Manager Registration Form")
window.geometry("1300x750")
window.configure(bg = "#45aaf2")
mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')

db = mclient['py-passm-db']

collection = db["users"]

labTitle = tk.Label(window, text="LOGIN",bg="#45aaf2", fg="#fff", font=("Poppins", 70, "bold")).grid(row=0, column=0)

labUserLogin = tk.Label(window, text="USER NAME",bg="#45aaf2", fg="#fff",font=("Arial", 20, "bold")).grid(row=3, column=0,sticky="W", padx=160, pady=5)

inputNameLogin = tk.Entry(window, width=63, font=("Poppins", 18))
inputNameLogin.grid(row=4, column=0,sticky="W", padx=160, pady=5)

labPassLogin = tk.Label(window, text="PASSWORD",bg="#45aaf2", fg="#fff",font=("Arial", 20, "bold")).grid(row=6, column=0,sticky="W", padx=160, pady=6)

inputPassLogin = tk.Entry(window, width=63, font=("Poppins", 18),  show="*")
inputPassLogin.grid(row=7, column=0,sticky="W", padx=160, pady=5)

def login():
    if inputNameLogin.get() == "" or inputPassLogin.get() == "":
        messagebox.showerror("Invalid", "Enter Valid Data")
    else:
        c = collection.find_one({"username": inputNameLogin.get(), "password": inputPassLogin.get()})
        print(c)
        if c:
            messagebox.showinfo("Info", "Login Success")
            window.destroy()
            from admin import admin_panel
            username = c["username"]
            print(username)
            admin_panel(username)

        else:
            messagebox.showerror("Info", "Login Failed")

btnSubmit = tk.Button(window, text = "L o g i n",width= 15, command = login,bg="white", font=("Poppins", 15,"normal")).grid(row=13, column = 0,padx=10, pady=30)


window.mainloop()
