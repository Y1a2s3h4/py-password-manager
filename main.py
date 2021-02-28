import tkinter as tk
import pymongo as pym
window = tk.Tk()
window.title("Password Manager")
window.geometry("700x600")
mclient = pym.MongoClient('mongodb://py-admin:py-password-manager@py-password-manager-shard-00-00.vcmoa.mongodb.net:27017,py-password-manager-shard-00-01.vcmoa.mongodb.net:27017,py-password-manager-shard-00-02.vcmoa.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-7oldae-shard-0&authSource=admin&retryWrites=true&w=majority')


db = mclient['py-passm-db']

collection = db["users"]

labTitle = tk.Label(window, text="Password Manager", font=("Arial", 25))
labTitle.grid(row=0, column=1)

labUser = tk.Label(window, text="User Name")
labUser.grid(row=1, column=0,sticky="W", padx=10, pady=10)

inputName = tk.Entry(window)
inputName.grid(row=1, column=1,sticky="W", padx=10, pady=10)

labPass = tk.Label(window, text="Password")
labPass.grid(row=2, column=0,sticky="W", padx=10, pady=10)

inputPass = tk.Entry(window)
inputPass.grid(row=2, column=1,sticky="W", padx=10, pady=10)

def reg():
    print(inputName.get())
    print(inputPass.get())
    collection.insert_one({
        "username": inputName.get(),
        "password": inputPass.get(),
    })


btnSubmit = tk.Button(window, text = "Register", command = reg)
btnSubmit.grid(row=3, column = 0,padx=10, pady=10)

print(inputName.get())

window.mainloop()
