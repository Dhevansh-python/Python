import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root=root
        self.root.title("Restaurant Managemant App")

        self.menu_items={
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 2,
            "PIZZA MEAL": 2,
            "CHESSE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate=1.32

        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame,text="Restaurant Order Management",font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels={}

        self.menu_quantities={}

        for i, (item, price)in enumerate(self.menu_items.items(), start=1):
            label=ttk.Label(frame, text=f"{item} (${price}):", font=("Arial", 12))

            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item]=label       