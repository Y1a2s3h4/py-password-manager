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

labTitle = tk.Label(window, text="REGISTRATION",bg="#45aaf2", fg="#fff", font=("Poppins", 70, "bold")).grid(row=0, column=0,padx=0, pady=0)

labUser = tk.Label(window, text="USER NAME",bg="#45aaf2", fg="#fff",font=("Arial", 20, "bold")).grid(row=3, column=0,sticky="W", padx=160, pady=5)

inputName = tk.Entry(window, width=63, font=("Poppins", 18))
inputName.grid(row=4, column=0,sticky="W", padx=160, pady=5)

labPass = tk.Label(window, text="PASSWORD",bg="#45aaf2", fg="#fff",font=("Arial", 20, "bold")).grid(row=6, column=0,sticky="W", padx=160, pady=(45,0))

inputPass = tk.Entry(window, width=63, font=("Poppins", 18), show="*")
inputPass.grid(row=7, column=0,sticky="W", padx=160, pady=5)

def reg():
    if inputName.get() == "" or inputPass.get() == "":
        messagebox.showerror("Invalid", "Enter Valid Data")
    else:
        c = collection.insert_one({
            "username": inputName.get(),
            "password": inputPass.get(),
        })
        if c:
            messagebox.showinfo("Info", "Register Success!")
            window.destroy()
            import login
        else:
            messagebox.showerror("Info", "Register Failed")


btnSubmitReg = tk.Button(window, text = "R e g i s t e r",width= 15, command = reg,bg="white", font=("Poppins", 15,"normal")).grid(row=13, column = 0,padx=10, pady=(70,0))

window.mainloop()
