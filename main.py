import tkinter as tk
from tkinter import messagebox
import pymongo as pym
window = tk.Tk()
window.title("Password Manager")
window.geometry("1300x750")
window.configure(bg = "#45aaf2")
mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')

db = mclient['py-passm-db']

collection = db["users"]

passManager = tk.Label(window, text = "PASSWORD MANAGER", font=("Poppins", 60, "bold"), bg="#45aaf2", fg="#fff").grid(row=0, column=0,sticky="W",padx=185, pady=40)

def reg():
    window.destroy()
    import registration

def login():
    window.destroy()
    import login

btnSubmitReg = tk.Button(window, text = "REGISTER", command= reg ,width=15, height=1, font=("Poppins", 25,"normal")).grid(row=1, column = 0,padx=0, pady=30)

btnSubmitLogin = tk.Button(window, text = "LOGIN", command= login ,width=15, height=1, font=("Poppins", 25,"normal")).grid(row=2, column = 0,padx=10, pady=30)


window.mainloop()
