import tkinter as tk
import re

class DomainForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.name_label = tk.Label(self, text="NAME:")
        self.name_entry = tk.Entry(self)
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        self.email_label = tk.Label(self, text="EMAIL ID:")
        self.email_entry = tk.Entry(self)
        self.email_label.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=1)

        self.phone_label = tk.Label(self, text="PHONE NUMBER:")
        self.phone_entry = tk.Entry(self)
        self.phone_label.grid(row=2, column=0)
        self.phone_entry.grid(row=2, column=1)

        self.validate_button = tk.Button(self, text="Validate", command=self.validate_form)
        self.validate_button.grid(row=3, column=1)

    def validate_form(self):
        # Get the form values
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        # Validate the name
        if not re.match(r'^[a-zA-Z]+$', name):
          #   tk.messagebox.showerror("Error", "Invalid name")
            print("ERROR - INVALID NAME")
            return

        # Validate the email ID
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
          #   tk.messagebox.showerror("Error", "Invalid email ID")
            print("ERROR - INVALID EMAIL")
            return

        # Validate the phone number
        if not re.match(r'^[0-9]{10}$', phone):
          #   tk.messagebox.showerror("Error", "Invalid phone number")
            print("ERROR - INVALID PHONE NUMBER")
            return

        # All fields are valid
     #    tk.messagebox.showinfo("Success", "All fields are valid")
            print("SUCCESS - ALL THE PROVIDED FIELDS ARE CORRECT")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("HELLO APPLICATION")

    form = DomainForm(root)
    form.pack()

    root.mainloop()
