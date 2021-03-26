import tkinter as tk
from tkinter import messagebox
import pymongo as pym
# import admin
window = tk.Tk()
window.title("Password Manager")
window.geometry("700x600")
mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')


db = mclient['py-passm-db']

collection = db["users"]

labTitle = tk.Label(window, text="Password Manager Register", font=("Arial", 25))
labTitle.grid(row=0, column=1)

labUser = tk.Label(window, text="User Name")
labUser.grid(row=1, column=0,sticky="W", padx=10, pady=10)

inputName = tk.Entry(window)
inputName.grid(row=1, column=1,sticky="W", padx=10, pady=10)

labPass = tk.Label(window, text="Password")
labPass.grid(row=2, column=0,sticky="W", padx=10, pady=10)

inputPass = tk.Entry(window)
inputPass.grid(row=2, column=1,sticky="W", padx=10, pady=10)


labTitle = tk.Label(window, text="Password Manager Login", font=("Arial", 25))
labTitle.grid(row=4, column=1)

labUserLogin = tk.Label(window, text="User Name")
labUserLogin.grid(row=5, column=0,sticky="W", padx=10, pady=10)

inputNameLogin = tk.Entry(window)
inputNameLogin.grid(row=5, column=1,sticky="W", padx=10, pady=10)

labPassLogin = tk.Label(window, text="Password")
labPassLogin.grid(row=6, column=0,sticky="W", padx=10, pady=10)

inputPassLogin = tk.Entry(window)
inputPassLogin.grid(row=6, column=1,sticky="W", padx=10, pady=10)

def reg():
    print(inputName.get())
    print(inputPass.get())
    c = collection.insert_one({
        "username": inputName.get(),
        "password": inputPass.get(),
    })
    if c:
        messagebox.showinfo("Info", "Register Success")

    else:
        messagebox.showerror("Info", "Register Failed")

def login():
    print(inputNameLogin.get())
    print(inputPassLogin.get())
    
    c = collection.find_one({"username": inputNameLogin.get(), "password": inputPassLogin.get()})
    print(c)
    if c:
        messagebox.showinfo("Info", "Login Success")
        window.destroy()
        import admin

    else:
        messagebox.showerror("Info", "Login Failed")

btnSubmit = tk.Button(window, text = "Register", command = reg)
btnSubmit.grid(row=3, column = 0,padx=10, pady=10)

btnSubmit = tk.Button(window, text = "Login", command = login)
btnSubmit.grid(row=7, column = 0,padx=10, pady=10)

print(inputName.get())

window.mainloop()
