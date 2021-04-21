import tkinter as tk
from tkinter import messagebox
import pymongo as pym
# import admin
window = tk.Tk()
window.title("Password Manager")
window.geometry("1300x750")
window.configure(bg = "#45aaf2")
mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')

db = mclient['py-passm-db']

collection = db["users"]

passManager = tk.Label(window, text = "PASSWORD MANAGER", font=("Poppins", 60, "bold"), bg="#45aaf2", fg="#fff").grid(row=0, column=0,sticky="W",padx=185, pady=40)
# labTitle = tk.Label(window, text="Password Manager Register", font=("Arial", 25))
# labTitle.grid(row=0, column=1)

# labUser = tk.Label(window, text="User Name")
# labUser.grid(row=1, column=0,sticky="W", padx=10, pady=10)

# inputName = tk.Entry(window)
# inputName.grid(row=1, column=1,sticky="W", padx=10, pady=10)

# labPass = tk.Label(window, text="Password")
# labPass.grid(row=2, column=0,sticky="W", padx=10, pady=10)

# inputPass = tk.Entry(window, show="*")
# inputPass.grid(row=2, column=1,sticky="W", padx=10, pady=10)


# labTitle = tk.Label(window, text="Password Manager Login", font=("Arial", 25)).grid(row=4, column=1)

# labUserLogin = tk.Label(window, text="User Name").grid(row=5, column=0,sticky="W", padx=10, pady=10)

# inputNameLogin = tk.Entry(window)
# inputNameLogin.grid(row=5, column=1,sticky="W", padx=10, pady=10)

# labPassLogin = tk.Label(window, text="Password").grid(row=6, column=0,sticky="W", padx=10, pady=10)

# inputPassLogin = tk.Entry(window, show="*")
# inputPassLogin.grid(row=6, column=1,sticky="W", padx=10, pady=10)

# def reg():
#     c = collection.insert_one({
#         "username": inputName.get(),
#         "password": inputPass.get(),
#     })
#     if c:
#         messagebox.showinfo("Info", "Register Success! Now Below Login")

#     else:
#         messagebox.showerror("Info", "Register Failed")

# def login():
#     print(inputNameLogin.get())
#     print(inputPassLogin.get())
    
#     c = collection.find_one({"username": inputNameLogin.get(), "password": inputPassLogin.get()})
#     print(c)
#     if c:
#         messagebox.showinfo("Info", "Login Success")
#         window.destroy()
#         from admin import admin_panel
#         username = c["username"]
#         print(username)
#         admin_panel(username)

#     else:
#         messagebox.showerror("Info", "Login Failed")
def reg():
    window.destroy()
    import registration

def login():
    window.destroy()
    import login

btnSubmitReg = tk.Button(window, text = "REGISTER", command= reg ,width=15, height=1, font=("Poppins", 25,"normal")).grid(row=1, column = 0,padx=0, pady=30)

btnSubmitLogin = tk.Button(window, text = "LOGIN", command= login ,width=15, height=1, font=("Poppins", 25,"normal")).grid(row=2, column = 0,padx=10, pady=30)


window.mainloop()
