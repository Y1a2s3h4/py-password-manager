import tkinter as tk
from tkinter import messagebox
import pymongo as pym

window = tk.Tk()
window.title("Password Manager")
window.geometry("1200x600")
mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')


db = mclient['py-passm-db']

collection = db["pass_data"]


titleLabel = tk.Label(window, text="Enter Your Password For: ")
titleLabel.grid(row=1, column=0,sticky="W", padx=10, pady=10)

titleInput = tk.Entry(window, width=20)
titleInput.grid(row=1, column=1,sticky="W", padx=10, pady=10)

userLabel = tk.Label(window, text="Enter Your Username: ")
userLabel.grid(row=2, column=0,sticky="W", padx=10, pady=10)

userInput = tk.Entry(window, width=20)
userInput.grid(row=2, column=1,sticky="W", padx=10, pady=10)

passwordLabel = tk.Label(window, text="Enter Your Password: ")
passwordLabel.grid(row=3, column=0,sticky="W", padx=10, pady=10)

passwordInput = tk.Entry(window, width=20)
passwordInput.grid(row=3, column=1,sticky="W", padx=10, pady=10)





def addData():
    if titleInput.get()!="" and userInput.get()!="" and passwordInput.get()!="":
        tk.messagebox.showinfo("Info", "Added Data")
    else:
        tk.messagebox.showerror("Info", "Enter Valid Data")

    c = collection.insert_one({
        "password_reason": titleInput.get(),
        "username": userInput.get(),
        "password": passwordInput.get(),
    })

def show():
    frame = tk.Frame().grid(row=4, column=0, padx=0, pady=0)
    passwordForHeader = tk.Label(frame, text="Password For").grid(row=4, column=0, padx=0, pady=0)
    usernameHeader = tk.Label(frame, text="User Name").grid(row=4, column=1, padx=10, pady=10)
    passwordHeader = tk.Label(frame, text="Password").grid(row=4, column=2, padx=10, pady=10)
    data = collection.find()
    x=4
    for i in data:
        x+=1
        tk.Label(frame, text=i["password_reason"]).grid(row=x, column=0, padx=10, pady=10)
        tk.Label(frame, text=i["username"]).grid(row=x, column=1, padx=10, pady=10)
        tk.Label(frame, text=i["password"]).grid(row=x, column=2, padx=10, pady=10)


btnSubmit = tk.Button(window, text = "Add", command = addData, width=10).grid(row=3, column = 2, sticky="W", padx=10, pady=10)
ShowData = tk.Button(window, text = "Show Data", command = show, width=10).grid(row=3, column = 3, sticky="W", padx=30, pady=10)


window.mainloop()
