import tkinter as tk

class DomainDetailsForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create labels and text boxes for the domain name and student name
        self.domain_name_label = tk.Label(self, text="USERNAME:")
        self.domain_name_entry = tk.Entry(self)
        self.student_name_label = tk.Label(self, text="USERID:")
        self.student_name_entry = tk.Entry(self)

        # Create radio buttons for the domain type
        self.domain_type_label = tk.Label(self, text="ACCOUNT:")
        self.domain_type_var = tk.IntVar()
        self.clear = [
            tk.Radiobutton(self, text="PERSONAL", variable=self.domain_type_var, value=0),
            tk.Radiobutton(self, text="PAGE", variable=self.domain_type_var, value=1),
        ]

        # Create a menu for selecting the domain registrar
        self.domain_registrar_label = tk.Label(self, text="SELECTPAGE:")
        self.domain_registrar_menu = tk.OptionMenu(self, tk.StringVar(), "SUBHAMGORAI", "KOLKATADAIRY", "BANGALOREFUN", "NEWS18", "CNBC", "DISCOVERYCHANNEL", "NATGEO")

        # Create a text box for other details
        self.other_details_label = tk.Label(self, text="Other details:")
        self.other_details_text = tk.Text(self, height=5, width=20)

        # Create a submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit)

        # Grid the widgets
        self.domain_name_label.grid(row=0, column=0)
        self.domain_name_entry.grid(row=0, column=1)
        self.student_name_label.grid(row=1, column=0)
        self.student_name_entry.grid(row=1, column=1)
        self.domain_type_label.grid(row=2, column=0)
        for i, radio_button in enumerate(self.clear):
            radio_button.grid(row=2, column=i+1)
        self.domain_registrar_label.grid(row=3, column=0)
        self.domain_registrar_menu.grid(row=3, column=1)
        self.other_details_label.grid(row=4, column=0)
        self.other_details_text.grid(row=4, column=1)
        self.submit_button.grid(row=5, column=1)

    def on_submit(self):
        # Get the domain details from the form
        domain_name = self.domain_name_entry.get()
        student_name = self.student_name_entry.get()
        domain_type = self.domain_type_var.get()
        other_details = self.other_details_text.get("1.0", "end-1c")

        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("HELLO APPLICATION");
    domain_details_form = DomainDetailsForm(root)
    domain_details_form.pack()
    root.mainloop()
