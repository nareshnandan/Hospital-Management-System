import tkinter as tk
from tkinter import ttk, messagebox


def show_doctors(content_frame):

    # ========================================================
    # Clear Existing Content
    # ========================================================

    for widget in content_frame.winfo_children():
        widget.destroy()

    # Stores the Treeview item currently being edited
    editing_doctor = None

    # ========================================================
    # Page Title
    # ========================================================

    page_title = tk.Label(
        content_frame,
        text="Doctor Management",
        font=("Arial", 22, "bold"),
        bg="#ECEFF1",
        fg="#263238"
    )

    page_title.pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )

    # ========================================================
    # Doctor Registration Form
    # ========================================================

    form_frame = tk.Frame(
        content_frame,
        bg="white"
    )

    form_frame.pack(
        padx=30,
        pady=10,
        fill="x"
    )

    # ========================================================
    # Doctor Name
    # ========================================================

    doctor_name_label = tk.Label(
        form_frame,
        text="Doctor Name",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    doctor_name_label.grid(
        row=0,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    doctor_name_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    doctor_name_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=15
    )

    # ========================================================
    # Specialization
    # ========================================================

    specialization_label = tk.Label(
        form_frame,
        text="Specialization",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    specialization_label.grid(
        row=1,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    specialization_combo = ttk.Combobox(
        form_frame,
        values=[
            "Cardiologist",
            "Dermatologist",
            "ENT Specialist",
            "General Physician",
            "Gynecologist",
            "Neurologist",
            "Orthopedic",
            "Pediatrician",
            "Psychiatrist",
            "Surgeon"
        ],
        state="readonly",
        width=32
    )

    specialization_combo.grid(
        row=1,
        column=1,
        padx=20,
        pady=15
    )

    # ========================================================
    # Phone Number
    # ========================================================

    phone_label = tk.Label(
        form_frame,
        text="Phone Number",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    phone_label.grid(
        row=2,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    phone_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    phone_entry.grid(
        row=2,
        column=1,
        padx=20,
        pady=15
    )

    # ========================================================
    # Email
    # ========================================================

    email_label = tk.Label(
        form_frame,
        text="Email",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    email_label.grid(
        row=3,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    email_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    email_entry.grid(
        row=3,
        column=1,
        padx=20,
        pady=15
    )

    # ========================================================
    # Experience
    # ========================================================

    experience_label = tk.Label(
        form_frame,
        text="Experience (Years)",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    experience_label.grid(
        row=4,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    experience_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    experience_entry.grid(
        row=4,
        column=1,
        padx=20,
        pady=15
    )

    # ========================================================
    # Consultation Fee
    # ========================================================

    fee_label = tk.Label(
        form_frame,
        text="Consultation Fee",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    fee_label.grid(
        row=5,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    fee_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    fee_entry.grid(
        row=5,
        column=1,
        padx=20,
        pady=15
    )

    # ========================================================
    # Register / Update Doctor Function
    # ========================================================

    def register_doctor():

        nonlocal editing_doctor

        doctor_name = doctor_name_entry.get().strip()
        specialization = specialization_combo.get()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()
        experience = experience_entry.get().strip()
        fee = fee_entry.get().strip()

        # ----------------------------------------------------
        # Required Field Validation
        # ----------------------------------------------------

        if not doctor_name or not specialization or not phone or not email or not experience or not fee:

            messagebox.showwarning(
                "Missing Information",
                "Please fill in all doctor details."
            )

            return

        # ----------------------------------------------------
        # Doctor Name Validation
        # Only letters and spaces are allowed
        # ----------------------------------------------------

        if not all(char.isalpha() or char.isspace() for char in doctor_name):

            messagebox.showwarning(
                "Invalid Doctor Name",
                "Doctor name should contain only letters and spaces."
            )

            return

        # ----------------------------------------------------
        # Mobile Number Validation
        # Exactly 10 digits
        # ----------------------------------------------------

        if not phone.isdigit() or len(phone) != 10:

            messagebox.showwarning(
                "Invalid Mobile Number",
                "Mobile number must contain exactly 10 digits."
            )

            return

        # ----------------------------------------------------
        # Experience Validation
        # Numbers only and between 0 and 60
        # ----------------------------------------------------

        if not experience.isdigit():

            messagebox.showwarning(
                "Invalid Experience",
                "Experience should contain numbers only."
            )

            return

        experience_value = int(experience)

        if experience_value < 0 or experience_value > 60:

            messagebox.showwarning(
                "Invalid Experience",
                "Experience must be between 0 and 60 years."
            )

            return

        # ----------------------------------------------------
        # Consultation Fee Validation
        # Numbers only
        # ----------------------------------------------------

        if not fee.isdigit():

            messagebox.showwarning(
                "Invalid Consultation Fee",
                "Consultation fee should contain numbers only."
            )

            return

        # ----------------------------------------------------
        # Update Existing Doctor
        # ----------------------------------------------------

        if editing_doctor is not None:

            doctor_id = doctor_table.item(
                editing_doctor,
                "values"
            )[0]

            doctor_table.item(
                editing_doctor,
                values=(
                    doctor_id,
                    doctor_name,
                    specialization,
                    phone,
                    email,
                    experience,
                    fee
                )
            )

            messagebox.showinfo(
                "Doctor Updated",
                "Doctor details updated successfully."
            )

            editing_doctor = None

            register_button.config(
                text="Register Doctor"
            )

        # ----------------------------------------------------
        # Register New Doctor
        # ----------------------------------------------------

        else:

            # Generate next Doctor ID
            doctor_number = 0

            for item in doctor_table.get_children():

                doctor_data = doctor_table.item(
                    item,
                    "values"
                )

                existing_id = doctor_data[0]

                try:
                    existing_number = int(existing_id[1:])

                    if existing_number > doctor_number:
                        doctor_number = existing_number

                except ValueError:
                    pass

            doctor_number += 1

            doctor_id = f"D{doctor_number:03d}"

            doctor_table.insert(
                "",
                "end",
                values=(
                    doctor_id,
                    doctor_name,
                    specialization,
                    phone,
                    email,
                    experience,
                    fee
                )
            )

            messagebox.showinfo(
                "Doctor Registered",
                f"Doctor {doctor_id} registered successfully."
            )

        # ----------------------------------------------------
        # Clear Form
        # ----------------------------------------------------

        doctor_name_entry.delete(
            0,
            tk.END
        )

        specialization_combo.set("")

        phone_entry.delete(
            0,
            tk.END
        )

        email_entry.delete(
            0,
            tk.END
        )

        experience_entry.delete(
            0,
            tk.END
        )

        fee_entry.delete(
            0,
            tk.END
        )

        # Clear table selection

        for item in doctor_table.selection():

            doctor_table.selection_remove(item)

    # ========================================================
    # Search Doctor
    # ========================================================

    def search_doctors():

        search_text = search_entry.get().lower()

        if not search_text:
            messagebox.showwarning(
                "Search",
                "Please enter a Doctor ID or Doctor Name."
            )
            return

        for item in doctor_table.get_children():

            values = doctor_table.item(
                item,
                "values"
            )

            doctor_id = values[0].lower()
            doctor_name = values[1].lower()

            if search_text in doctor_id or search_text in doctor_name:

                doctor_table.selection_set(item)
                doctor_table.focus(item)
                doctor_table.see(item)

                return

        messagebox.showinfo(
            "Search Result",
            "No doctor found."
        )

    # ========================================================
    # Clear Search
    # ========================================================

    def clear_search():

        search_entry.delete(
            0,
            tk.END
        )

        for item in doctor_table.selection():

            doctor_table.selection_remove(item)

    # ========================================================
    # Edit Doctor
    # ========================================================

    def edit_doctor():

        selected_item = doctor_table.selection()

        # Check whether a doctor is selected
        if not selected_item:

            messagebox.showwarning(
                "No Doctor Selected",
                "Please select a doctor from the table."
            )

            return

        doctor_data = doctor_table.item(
            selected_item[0],
            "values"
        )

        nonlocal editing_doctor

        # Remember selected doctor
        editing_doctor = selected_item[0]

        # ----------------------------------------------------
        # Load Doctor Name
        # ----------------------------------------------------

        doctor_name_entry.delete(
            0,
            tk.END
        )

        doctor_name_entry.insert(
            0,
            doctor_data[1]
        )

        # ----------------------------------------------------
        # Load Specialization
        # ----------------------------------------------------

        specialization_combo.set(
            doctor_data[2]
        )

        # ----------------------------------------------------
        # Load Phone
        # ----------------------------------------------------

        phone_entry.delete(
            0,
            tk.END
        )

        phone_entry.insert(
            0,
            doctor_data[3]
        )

        # ----------------------------------------------------
        # Load Email
        # ----------------------------------------------------

        email_entry.delete(
            0,
            tk.END
        )

        email_entry.insert(
            0,
            doctor_data[4]
        )

        # ----------------------------------------------------
        # Load Experience
        # ----------------------------------------------------

        experience_entry.delete(
            0,
            tk.END
        )

        experience_entry.insert(
            0,
            doctor_data[5]
        )

        # ----------------------------------------------------
        # Load Consultation Fee
        # ----------------------------------------------------

        fee_entry.delete(
            0,
            tk.END
        )

        fee_entry.insert(
            0,
            doctor_data[6]
        )

        # Change button text

        register_button.config(
            text="Update Doctor"
        )
    
    # ========================================================
    # Delete Doctor
    # ========================================================

    def delete_doctor():

        nonlocal editing_doctor

        selected_item = doctor_table.selection()

        # ----------------------------------------------------
        # Check whether a doctor is selected
        # ----------------------------------------------------

        if not selected_item:

            messagebox.showwarning(
                "No Doctor Selected",
                "Please select a doctor from the table."
            )

            return

        # Get selected doctor details
        doctor_data = doctor_table.item(
            selected_item[0],
            "values"
        )

        doctor_id = doctor_data[0]
        doctor_name = doctor_data[1]

        # ----------------------------------------------------
        # Confirmation Before Delete
        # ----------------------------------------------------

        confirm_delete = messagebox.askyesno(
            "Delete Doctor",
            f"Are you sure you want to delete\n"
            f"Doctor {doctor_id} - {doctor_name}?"
        )

        if not confirm_delete:
            return

        # ----------------------------------------------------
        # Delete Doctor
        # ----------------------------------------------------

        doctor_table.delete(
            selected_item[0]
        )

        # ----------------------------------------------------
        # Reset Edit Mode
        # ----------------------------------------------------

        editing_doctor = None

        register_button.config(
            text="Register Doctor"
        )

        # ----------------------------------------------------
        # Clear Form
        # ----------------------------------------------------

        doctor_name_entry.delete(
            0,
            tk.END
        )

        specialization_combo.set("")

        phone_entry.delete(
            0,
            tk.END
        )

        email_entry.delete(
            0,
            tk.END
        )

        experience_entry.delete(
            0,
            tk.END
        )

        fee_entry.delete(
            0,
            tk.END
        )

        # ----------------------------------------------------
        # Show Success Message
        # ----------------------------------------------------

        messagebox.showinfo(
            "Doctor Deleted",
            f"Doctor {doctor_id} deleted successfully."
        )

    # ========================================================
    # Register Doctor Button
    # ========================================================

    register_button = tk.Button(
        form_frame,
        text="Register Doctor",
        font=("Arial", 11, "bold"),
        bg="#1976D2",
        fg="white",
        relief="flat",
        padx=20,
        pady=8,
        command=register_doctor
    )

    register_button.grid(
        row=6,
        column=1,
        padx=20,
        pady=20,
        sticky="e"
    )

    # ========================================================
    # Registered Doctors Section
    # ========================================================

    doctors_title = tk.Label(
        content_frame,
        text="Registered Doctors",
        font=("Arial", 16, "bold"),
        bg="#ECEFF1",
        fg="#263238"
    )

    doctors_title.pack(
        anchor="w",
        padx=30,
        pady=(20, 10)
    )

    # ========================================================
    # Search Frame
    # ========================================================

    search_frame = tk.Frame(
        content_frame,
        bg="#ECEFF1"
    )

    search_frame.pack(
        fill="x",
        padx=20,
        pady=(10, 5)
    )

    # Search Label

    search_label = tk.Label(
        search_frame,
        text="Search Doctor:",
        font=("Arial", 11, "bold"),
        bg="#ECEFF1"
    )

    search_label.pack(
        side="left",
        padx=(0, 10)
    )

    # Search Entry

    search_entry = tk.Entry(
        search_frame,
        font=("Arial", 11),
        width=30
    )

    search_entry.pack(
        side="left"
    )

    # Search Button

    search_button = tk.Button(
        search_frame,
        text="Search",
        font=("Arial", 10, "bold"),
        bg="#1976D2",
        fg="white",
        relief="flat",
        padx=15,
        pady=5,
        command=search_doctors
    )

    search_button.pack(
        side="left",
        padx=10
    )

    # Clear Button

    clear_button = tk.Button(
        search_frame,
        text="Clear",
        font=("Arial", 10, "bold"),
        bg="#757575",
        fg="white",
        relief="flat",
        padx=15,
        pady=5,
        command=clear_search
    )

    clear_button.pack(
        side="left"
    )

    # Edit Button                                      

    edit_button = tk.Button(
        search_frame,
        text="Edit Doctor",
        font=("Arial", 10, "bold"),
        bg="#388E3C",
        fg="white",
        relief="flat",
        padx=15,
        pady=5,
        command=edit_doctor
    )

    edit_button.pack(
        side="left",
        padx=10
    )
    
    # Delete Button
    delete_button = tk.Button(
        search_frame,
        text="Delete Doctor",
        font=("Arial", 10, "bold"),
        bg="#D32F2F",
        fg="white",
        relief="flat",
        padx=15,
        pady=5,
        command=delete_doctor
    )

    delete_button.pack(
        side="left",
        padx=5
    )

    # ========================================================
    # Doctor Table Frame
    # ========================================================

    table_frame = tk.Frame(
        content_frame,
        bg="white"
    )

    table_frame.pack(
        padx=30,
        pady=5,
        fill="both",
        expand=True
    )

    # ========================================================
    # Doctor Table
    # ========================================================

    doctor_table = ttk.Treeview(
        table_frame,
        columns=(
            "id",
            "name",
            "specialization",
            "phone",
            "email",
            "experience",
            "fee"
        ),
        show="headings"
    )

    # ========================================================
    # Table Headings
    # ========================================================

    doctor_table.heading(
        "id",
        text="ID"
    )

    doctor_table.heading(
        "name",
        text="Doctor Name"
    )

    doctor_table.heading(
        "specialization",
        text="Specialization"
    )

    doctor_table.heading(
        "phone",
        text="Phone"
    )

    doctor_table.heading(
        "email",
        text="Email"
    )

    doctor_table.heading(
        "experience",
        text="Experience"
    )

    doctor_table.heading(
        "fee",
        text="Consultation Fee"
    )

    # ========================================================
    # Column Widths
    # ========================================================

    doctor_table.column(
        "id",
        width=60,
        anchor="center"
    )

    doctor_table.column(
        "name",
        width=150,
        anchor="center"
    )

    doctor_table.column(
        "specialization",
        width=150,
        anchor="center"
    )

    doctor_table.column(
        "phone",
        width=120,
        anchor="center"
    )

    doctor_table.column(
        "email",
        width=180,
        anchor="center"
    )

    doctor_table.column(
        "experience",
        width=100,
        anchor="center"
    )

    doctor_table.column(
        "fee",
        width=120,
        anchor="center"
    )

    doctor_table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )
    
