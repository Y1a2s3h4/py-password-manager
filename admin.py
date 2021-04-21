import tkinter as tk
from tkinter import messagebox
import pymongo as pym

def admin_panel(name):
    window = tk.Tk()
    window.title("Password Manager")
    window.geometry("1300x750")
    window.configure(bg = "#45aaf2")
    mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')

    db = mclient['py-passm-db']

    collection = db["users"]


    titleLabel = tk.Label(window, text="Enter Your Password For: ",bg="#45aaf2", fg="#fff", font=("Poppins", 16, "normal")).grid(row=1, column=0,sticky="W", padx=10, pady=10)

    titleInput = tk.Entry(window, width=20, font=("Poppins", 16))
    titleInput.grid(row=2, column=0,sticky="W", padx=10, pady=10)

    userLabel = tk.Label(window, text="Enter Your Username: ",bg="#45aaf2", fg="#fff", font=("Poppins", 16, "normal")).grid(row=4, column=0,sticky="W", padx=10, pady=10)

    userInput = tk.Entry(window, width=20, font=("Poppins", 16))
    userInput.grid(row=5, column=0,sticky="W", padx=10, pady=10)

    passwordLabel = tk.Label(window, text="Enter Your Password: ",bg="#45aaf2", fg="#fff", font=("Poppins", 16, "normal")).grid(row=7, column=0,sticky="W", padx=10, pady=10)

    passwordInput = tk.Entry(window, width=20, font=("Poppins", 16))
    passwordInput.grid(row=8, column=0,sticky="W", padx=10, pady=10)


    def addData():
        password_reason = titleInput.get()
        username = userInput.get()
        password = passwordInput.get()
        if password_reason!="" and username!="" and password!="":
            useName = collection.update({"username": name}, {"$push": {"allData": {"password_reason": password_reason ,"username": username ,"password": password}}})
            tk.messagebox.showinfo("Info", "Added Data")
        else:
            tk.messagebox.showerror("Info", "Enter Valid Data")

    def show():
        frame = tk.Frame().grid(row=0, column=0)
        passwordForHeader = tk.Label(frame, text="Password For",bg="#45aaf2", fg="#fff", font=("Poppins", 14)).grid(row=1, column=4, padx=30, pady=0)
        usernameHeader = tk.Label(frame, text="User Name",bg="#45aaf2", fg="#fff", font=("Poppins", 14)).grid(row=1, column=5, padx=30, pady=10)
        passwordHeader = tk.Label(frame, text="Password",bg="#45aaf2", fg="#fff", font=("Poppins", 14)).grid(row=1, column=6, padx=30, pady=10)
        data = collection.find_one({"username": name})
        print(data)
        x=1
        for i in data["allData"]:
            x+=1
            tk.Label(frame, text=i["password_reason"],bg="#45aaf2", fg="#fff", font=("Poppins", 14)).grid(row=x, column=4, padx=25, pady=10)
            tk.Label(frame, text=i["username"],bg="#45aaf2", fg="#fff", font=("Poppins", 14)).grid(row=x, column=5, padx=25, pady=10)
            tk.Label(frame, text=i["password"],bg="#45aaf2", fg="#fff", font=("Poppins", 14)).grid(row=x, column=6, padx=25, pady=10)

    def logout():
        ans = tk.messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if ans:
            window.destroy()
            import login

    btnSubmit = tk.Button(window, text = "Add", command = addData, width=10, font=("Poppins", 16)).grid(row=10, column = 0, sticky="W", padx=10, pady=10)
    ShowData = tk.Button(window, text = "Show Data", command = show, width=10, font=("Poppins", 16)).grid(row=10, column = 1, sticky="W", padx=10, pady=10)
    btnLogout = tk.Button(window, text = "Logout", command = logout, width=10, font=("Poppins", 16)).grid(row=10, column = 2, sticky="W", padx=10, pady=10)


    window.mainloop()
