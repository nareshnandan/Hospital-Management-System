import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("900x600")
root.configure(bg="white")

# Header frame __________________________________________________________________
header_frame = tk.Frame(
    root,
    bg = "#1976D2",
    height = 70
)
header_frame.pack(fill = "x")

# Header title
header_title = tk.Label(
    header_frame,
    text="Hospital Management System",
    font=("Arial", 20, "bold"),
    bg="#1976D2",
    fg="white"
)
header_title.pack(side="left", padx=20, pady=15)

# Date label
date_label = tk.Label(
    header_frame,
    text=datetime.now().strftime("%d-%m-%Y"),
    font=("Arial", 11),
    bg="#1976D2",
    fg="white"
)
date_label.pack(side="right", padx=20)

# Admin label
admin_label = tk.Label(
    header_frame,
    text="Admin",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white"
)
admin_label.pack(side="right", padx=10)

# Navigation Frame_______________________________________________________________
navigation_frame = tk.Frame(
    root,
    bg="#263238",
    width=200
)
navigation_frame.pack(side="left", fill="y")

# Content Frame___________________________________________________________________
content_frame = tk.Frame(
    root,
    bg="#ECEFF1"
)
content_frame.pack(side="right", fill="both", expand=True)

# Dashboard Function______________________________________________________________
def show_dashboard():

    # Remove existing widgets from content area
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Dashboard title
    dashboard_title = tk.Label(
        content_frame,
        text="Dashboard",
        font=("Arial", 22, "bold"),
        bg="#ECEFF1",
        fg="#263238"
    )
    dashboard_title.pack(anchor="w", padx=30, pady=(25, 5))

    # Welcome message
    welcome_label = tk.Label(
        content_frame,
        text="Welcome to Hospital Management System",
        font=("Arial", 12),
        bg="#ECEFF1",
        fg="#546E7A"
    )
    welcome_label.pack(anchor="w", padx=30, pady=5)

    stats_frame = tk.Frame(
        content_frame,
        bg="#ECEFF1"
    )

    stats_frame.pack(
        fill="x",
        padx=30,
        pady=25
    )    

    patient_card = tk.Frame(
        stats_frame,
        bg="white",
        width=200,
        height=120
    )

    patient_card.pack(
        side="left",
        padx=(0, 15)
    )

    patient_title = tk.Label(
        patient_card,
        text="Total Patients",
        font=("Arial", 11),
        bg="white",
        fg="#546E7A"
    )

    patient_title.pack(pady=(20, 5))

    patient_count = tk.Label(
        patient_card,
        text="125",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="#1976D2"
    )

    patient_count.pack()

    doctor_card = tk.Frame(
        stats_frame,
        bg="white",
        width=200,
        height=120
    )

    doctor_card.pack(
        side="left",
        padx=15
    )
    doctor_title = tk.Label(
        doctor_card,
        text="Total Doctors",
        font=("Arial", 11),
        bg="white",
        fg="#546E7A"
    )

    doctor_title.pack(pady=(20, 5))
    doctor_count = tk.Label(
        doctor_card,
        text="12",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="#1976D2"
    )

    doctor_count.pack()

    appointment_card = tk.Frame(
        stats_frame,
        bg="white",
        width=200,
        height=120
    )

    appointment_card.pack(
        side="left",
        padx=15
    )

    appointment_title = tk.Label(
        appointment_card,
        text="Today's Appointments",
        font=("Arial", 11),
        bg="white",
        fg="#546E7A"
    )

    appointment_title.pack(pady=(20, 5))

    appointment_count = tk.Label(
        appointment_card,
        text="18",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="#1976D2"
    )

    appointment_count.pack()

# Show patient functions________________________________________________________
def show_patients():

    # Clear existing content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Page title
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

    form_frame = tk.Frame(
        content_frame,
        bg="white"
    )

    form_frame.pack(
        padx=30,
        pady=10,
        fill="x"
    )
        
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

    phone_label = tk.Label(
        form_frame,
        text="Phone Number",
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )
# Phone number
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

# Address
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

# Blood Group
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

# Register

    register_button = tk.Button(
        form_frame,
        text="Register Patient",
        font=("Arial", 11, "bold"),
        bg="#1976D2",
        fg="white",
        relief="flat",
        padx=20,
        pady=8
    )

    register_button.grid(
        row=6,
        column=1,
        padx=20,
        pady=20,
        sticky="e"
    )
# Buttons_______________________________________________________________________

# Dashboard button
dashboard_button = tk.Button(
    navigation_frame,
    text="Dashboard",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat",
    command=show_dashboard
)
dashboard_button.pack(fill="x", padx=10, pady=5)

# Patients button
patients_button = tk.Button(
    navigation_frame,
    text="Patients",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat",
    command=show_patients
)
patients_button.pack(fill="x", padx=10, pady=5)

# Doctors button
doctors_button = tk.Button(
    navigation_frame,
    text="Doctors",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat"
)
doctors_button.pack(fill="x", padx=10, pady=5)

# Appointments button
appointments_button = tk.Button(
    navigation_frame,
    text="Appointments",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat"
)
appointments_button.pack(fill="x", padx=10, pady=5)

# Reports button
reports_button = tk.Button(
    navigation_frame,
    text="Reports",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat"
)
reports_button.pack(fill="x", padx=10, pady=5)

# Settings button
settings_button = tk.Button(
    navigation_frame,
    text="Settings",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat"
)
settings_button.pack(fill="x", padx=10, pady=5)


show_dashboard()
root.mainloop()

