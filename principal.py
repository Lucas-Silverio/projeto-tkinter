import tkinter as tk
from views.pet_shop_app import PetshopApp

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False,False)
    app = PetshopApp(root)
    app.preencher_lista()
    root.geometry("1050x600")
    root.mainloop()