import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymongo as pym

def del_credentials(name):
    window = tk.Toplevel()
    window.title("Password Manager Admin")
    window.geometry("580x750")
    window.configure(bg = "#45aaf2")
    mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')

    db = mclient['py-passm-db']

    collection = db["users"]


    titleLabel = tk.Label(window, text="Enter Your Password For: ",bg="#45aaf2", fg="#fff", font=("Poppins", 16, "normal")).grid(row=1, column=0,sticky="W", padx=10, pady=(10,0))

    titleInput = tk.Entry(window, width=30, font=("Poppins", 16))
    titleInput.grid(row=2, column=0,sticky="W", padx=10, pady=10)

    userLabel = tk.Label(window, text="Enter Your Username: ",bg="#45aaf2", fg="#fff", font=("Poppins", 16, "normal")).grid(row=4, column=0,sticky="W", padx=10, pady=(10,0))

    userInput = tk.Entry(window, width=30, font=("Poppins", 16))
    userInput.grid(row=5, column=0,sticky="W", padx=10, pady=10)

    passwordLabel = tk.Label(window, text="Enter Your Password: ",bg="#45aaf2", fg="#fff", font=("Poppins", 16, "normal")).grid(row=7, column=0,sticky="W", padx=10, pady=(10,0))

    passwordInput = tk.Entry(window, width=30, font=("Poppins", 16))
    passwordInput.grid(row=8, column=0,sticky="W", padx=10, pady=10)


    def deleteData():
        password_reason = titleInput.get()
        username = userInput.get()
        password = passwordInput.get()
    
        if password_reason!="" and username!="" and password!="":
            useName = collection.update({"username": name}, {"$pull": {"allData": {"password_reason": password_reason ,"username": username ,"password": password}}})
            tk.messagebox.showinfo("Info", "Data Deleted")
        else:
            tk.messagebox.showerror("Info", "Enter Valid Data")
        

    def show():
        top = tk.Toplevel()
        top.title("Data")
        top.geometry("1300x750")

        # frame = tk.Frame(top).grid(row=11, column=2)
        table = ttk.Treeview(top,height=100, columns=("Password For","User Name","Password"))
        # table.column("Password For", "User Name", "Password")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Poppins", 20, "normal"))
        style.configure("Treeview", rowheight=40, font=("Poppins", 14))

        table.heading('#0', text="")
        table.heading('Password For', text="Password For")
        table.heading('User Name', text="User Name")
        table.heading('Password', text="Password")

        table.column('#0', width=0, stretch=tk.NO)
        table.column('Password For', anchor=tk.CENTER, width=250, stretch=tk.YES)
        table.column('User Name', anchor=tk.CENTER, width=250, stretch=tk.YES)
        table.column('Password', anchor=tk.CENTER, width=250, stretch=tk.YES)


        table.grid(row=1, columnspan=140, padx=260, pady=10)

        data = collection.find_one({"username": name})
        for i in data["allData"]:
            table.insert(parent="", index="end", values=(i["password_reason"],i["username"],i["password"]))

        top.mainloop()


    btnSubmit = tk.Button(window, text = "Delete", command = deleteData, width=10, font=("Poppins", 16)).grid(row=10,sticky="W" ,column = 0,padx=10,pady=10)
    ShowData = tk.Button(window, text = "Show Data", command = show, width=10, font=("Poppins", 16)).grid(row=10,sticky="W" ,column = 0, padx=(200,0), pady=10, ipadx=20)


    window.mainloop()
