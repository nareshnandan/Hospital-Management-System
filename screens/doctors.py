import tkinter as tk
from tkinter import ttk


def show_doctors(content_frame):

    # ========================================================
    # Clear Existing Content
    # ========================================================

    for widget in content_frame.winfo_children():
        widget.destroy()

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
    # Register Doctor Function
    # ========================================================

    def register_doctor():

        doctor_name = doctor_name_entry.get()
        specialization = specialization_combo.get()
        phone = phone_entry.get()
        email = email_entry.get()
        experience = experience_entry.get()
        fee = fee_entry.get()

        # Check required fields

        if not doctor_name or not specialization or not phone or not email or not experience or not fee:
            tk.messagebox.showwarning(
                "Missing Information",
                "Please fill in all doctor details."
            )
            return

        # Generate Doctor ID

        doctor_number = len(doctor_table.get_children()) + 1
        doctor_id = f"D{doctor_number:03d}"

        # Add doctor to table

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

        # Clear form

        doctor_name_entry.delete(0, tk.END)
        specialization_combo.set("")
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        experience_entry.delete(0, tk.END)
        fee_entry.delete(0, tk.END)

        # Success message

        tk.messagebox.showinfo(
            "Doctor Registered",
            f"Doctor {doctor_id} registered successfully."
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

