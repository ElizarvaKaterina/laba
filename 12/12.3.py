class IceCreamStand:
    def __init__(self, name, flavors):
        self.name = name
        self.flavors = flavors

    def get_menu(self):
        menu = "Добро пожаловать на Литейный мост в кафе " + self.name + "\n"
        menu += "У нас есть мороженое:\n"
        for flavor in self.flavors:
            menu += "- " + flavor + "\n"
        return menu

import tkinter as tk

my_stand = IceCreamStand("Мороженица", ["клубничное", "ягодное", "имбирное"],)
root = tk.Tk()
root.title("Мороженица")
menu_label = tk.Label(root, text=my_stand.get_menu())
menu_label.pack()
root.mainloop()
