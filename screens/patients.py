import tkinter as tk
from tkinter import ttk, messagebox

def show_patients(content_frame):

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
        text="Patient Management",
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
    # Patient Registration Form
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
    # Patient Name
    # ========================================================

    name_label = tk.Label(
        form_frame,
        text="Patient Name",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    name_label.grid(
        row=0,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )


    name_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    name_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=15
    )


    # ========================================================
    # Age
    # ========================================================

    age_label = tk.Label(
        form_frame,
        text="Age",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    age_label.grid(
        row=1,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )


    age_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    age_entry.grid(
        row=1,
        column=1,
        padx=20,
        pady=15
    )


    # ========================================================
    # Gender
    # ========================================================

    gender_label = tk.Label(
        form_frame,
        text="Gender",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    gender_label.grid(
        row=2,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )


    gender_combo = ttk.Combobox(
        form_frame,
        values=[
            "Male",
            "Female",
            "Other"
        ],
        state="readonly",
        width=32
    )

    gender_combo.grid(
        row=2,
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
        row=3,
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
        row=3,
        column=1,
        padx=20,
        pady=15
    )


    # ========================================================
    # Address
    # ========================================================

    address_label = tk.Label(
        form_frame,
        text="Address",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    address_label.grid(
        row=4,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )


    address_entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=35
    )

    address_entry.grid(
        row=4,
        column=1,
        padx=20,
        pady=15
    )


    # ========================================================
    # Blood Group
    # ========================================================

    blood_label = tk.Label(
        form_frame,
        text="Blood Group",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )

    blood_label.grid(
        row=5,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )


    blood_combo = ttk.Combobox(
        form_frame,
        values=[
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ],
        state="readonly",
        width=32
    )

    blood_combo.grid(
        row=5,
        column=1,
        padx=20,
        pady=15
    )

    # ========================================================
    # Register Patient Function
    # ========================================================

    def register_patient():

        name = name_entry.get()
        age = age_entry.get()
        gender = gender_combo.get()
        phone = phone_entry.get()
        address = address_entry.get()
        blood_group = blood_combo.get()

        # Validate required fields

        if not name or not age or not gender or not phone or not address or not blood_group:
            tk.messagebox.showwarning(
                "Missing Information",
                "Please fill in all patient details."
            )
            return

        # Validate Patient Name

        if not name.replace(" ", "").isalpha():
            messagebox.showwarning(
                "Invalid Name",
                "Patient name must contain only letters and spaces."
            )
            return

        # Validate Age

        try:
            age = int(age)
        except ValueError:
            messagebox.showwarning(
                "Invalid Age",
                "Age must be a number."
            )
            return

        if age <= 0 or age > 120:
            messagebox.showwarning(
                "Invalid Age",
                "Please enter a valid age between 1 and 120."
            )
            return

        # Validate Phone Number

        if not phone.isdigit():
            messagebox.showwarning(
                "Invalid Phone Number",
                "Phone number must contain only digits."
            )
            return

        if len(phone) != 10:
            messagebox.showwarning(
                "Invalid Phone Number",
                "Phone number must contain exactly 10 digits."
            )
            return

        # Generate Patient ID
        patient_number = len(patient_table.get_children()) + 1
        patient_id = f"P{patient_number:03d}"

        patient_table.insert(
            "",
            "end",
            values=(
                patient_id,
                name,
                age,
                gender,
                phone,
                address,
                blood_group
            )
        )


        # Clear form fields
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_combo.set("")
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        blood_combo.set("")


    def search_patients():
        search_text = search_entry.get().lower()

        for item in patient_table.get_children():
            values = patient_table.item(item, "values")

            patient_id = values[0].lower()
            patient_name = values[1].lower()

            if search_text in patient_id or search_text in patient_name:
                patient_table.selection_set(item)
                patient_table.focus(item)
                patient_table.see(item)
                return

        messagebox.showinfo(
            "Search Result",
            "No patient found."
        )

    # ========================================================
    # Register Button
    # ========================================================

    register_button = tk.Button(
        form_frame,
        text="Register Patient",
        font=("Arial", 11, "bold"),
        bg="#1976D2",
        fg="white",
        relief="flat",
        padx=20,
        pady=8,
        command=register_patient
    )

    register_button.grid(
        row=6,
        column=1,
        padx=20,
        pady=20,
        sticky="e"
    )

    # ========================================================
    # Registered Patients Section
    # ========================================================

    patients_title = tk.Label(
        content_frame,
        text="Registered Patients",
        font=("Arial", 16, "bold"),
        bg="#ECEFF1",
        fg="#263238"
    )

    patients_title.pack(
        anchor="w",
        padx=30,
        pady=(20, 10)
    )

    # Search Frame

    search_frame = tk.Frame(content_frame, bg="#ECEFF1")
    search_frame.pack(fill="x", padx=20, pady=(10, 5))

    search_label = tk.Label(
        search_frame,
        text="Search Patient:",
        font=("Arial", 11, "bold"),
        bg="#ECEFF1"
    )
    search_label.pack(side="left", padx=(0, 10))

    search_entry = tk.Entry(
        search_frame,
        font=("Arial", 11),
        width=30
    )
    search_entry.pack(side="left")
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
        command=search_patients
    )
    search_button.pack(side="left", padx=10)

    # ========================================================
    # Patient Table
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


    patient_table = ttk.Treeview(
        table_frame,
        columns=(
            "id",
            "name",
            "age",
            "gender",
            "phone",
            "address",
            "blood"
        ),
        show="headings"
    )


    # Table Headings

    patient_table.heading(
        "id",
        text="ID"
    )

    patient_table.heading(
        "name",
        text="Name"
    )

    patient_table.heading(
        "age",
        text="Age"
    )

    patient_table.heading(
        "gender",
        text="Gender"
    )

    patient_table.heading(
        "phone",
        text="Phone"
    )

    patient_table.heading(
        "address",
        text="Address"
    )

    patient_table.heading(
        "blood",
        text="Blood Group"
    )


    # Column Widths

    patient_table.column(
        "id",
        width=50,
        anchor="center"
    )

    patient_table.column(
        "name",
        width=150,
        anchor="center"
    )

    patient_table.column(
        "age",
        width=60,
        anchor="center"
    )

    patient_table.column(
        "gender",
        width=100,
        anchor="center"
    )

    patient_table.column(
        "phone",
        width=130,
        anchor="center"
    )

    patient_table.column(
        "address",
        width=180,
        anchor="center"
    )

    patient_table.column(
        "blood",
        width=100,
        anchor="center"
    )


    patient_table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )