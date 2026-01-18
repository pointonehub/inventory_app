#retro game store
import tkinter as tk
root = tk.Tk()

root.title("Inventory")
root.geometry("600x500")

appname = tk.Label(root, text="The Retro Vault", font=("Arial", 10))
appname.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")



root.mainloop()
