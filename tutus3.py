import tkinter as tk
from tkinter import ttk
import sqlite3

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("pharmacy.db")
        self.create_tables()

        # Create GUI components
        self.create_gui()

    def create_tables(self):
        # Create a table for medicines
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS medicines (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)

    def create_gui(self):
        # Create a notebook to switch between different views
        self.notebook = ttk.Notebook(self.root)

        # Medicine tab
        medicine_frame = ttk.Frame(self.notebook)
        self.notebook.add(medicine_frame, text="Medicines")

        # Medicine table
        self.tree = ttk.Treeview(medicine_frame, columns=("Name", "Quantity", "Price"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack()

        # Load medicines into the table
        self.load_medicines()

        # Add medicine button
        add_button = ttk.Button(medicine_frame, text="Add Medicine", command=self.add_medicine)
        add_button.pack(pady=10)

        # Pack the notebook
        self.notebook.pack(padx=10, pady=10)

    def load_medicines(self):
        # Clear existing items in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch medicines from the database and populate the table
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM medicines")
            for row in cursor:
                self.tree.insert("", "end", values=row)

    def add_medicine(self):
        # Create a popup window for adding a new medicine
        popup = tk.Toplevel()
        popup.title("Add Medicine")

        # Entry fields
        name_label = ttk.Label(popup, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        name_entry = ttk.Entry(popup)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        quantity_label = ttk.Label(popup, text="Quantity:")
        quantity_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        quantity_entry = ttk.Entry(popup)
        quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        price_label = ttk.Label(popup, text="Price:")
        price_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        price_entry = ttk.Entry(popup)
        price_entry.grid(row=2, column=1, padx=10, pady=5)

        # Save button
        save_button = ttk.Button(popup, text="Save", command=lambda: self.save_medicine(
            name_entry.get(), quantity_entry.get(), price_entry.get(), popup))
        save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_medicine(self, name, quantity, price, popup):
        # Validate input
        if not name or not quantity or not price:
            tk.messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Insert the new medicine into the database
        with self.conn:
            self.conn.execute("INSERT INTO medicines (name, quantity, price) VALUES (?, ?, ?)",
                              (name, quantity, price))

        # Update the table and close the popup
        self.load_medicines()
        popup.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()
