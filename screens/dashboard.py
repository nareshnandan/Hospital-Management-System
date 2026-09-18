import tkinter as tk
from datetime import datetime


def show_dashboard(content_frame):

    # ========================================================
    # Clear Existing Content
    # ========================================================

    for widget in content_frame.winfo_children():
        widget.destroy()


    # ========================================================
    # Dashboard Header
    # ========================================================

    header_frame = tk.Frame(
        content_frame,
        bg="#ECEFF1"
    )

    header_frame.pack(
        fill="x",
        padx=30,
        pady=(25, 10)
    )


    # Dashboard Title

    dashboard_title = tk.Label(
        header_frame,
        text="Dashboard",
        font=("Arial", 24, "bold"),
        bg="#ECEFF1",
        fg="#263238"
    )

    dashboard_title.pack(
        anchor="w"
    )


    # Welcome Message

    welcome_label = tk.Label(
        header_frame,
        text="Welcome back, Admin! Here's your hospital overview.",
        font=("Arial", 11),
        bg="#ECEFF1",
        fg="#607D8B"
    )

    welcome_label.pack(
        anchor="w",
        pady=(4, 0)
    )


    # Current Date

    current_date = datetime.now().strftime("%A, %d %B %Y")

    date_label = tk.Label(
        header_frame,
        text=current_date,
        font=("Arial", 10),
        bg="#ECEFF1",
        fg="#78909C"
    )

    date_label.pack(
        anchor="e",
        pady=(0, 5)
    )


    # ========================================================
    # Statistics Cards
    # ========================================================

    stats_frame = tk.Frame(
        content_frame,
        bg="#ECEFF1"
    )

    stats_frame.pack(
        fill="x",
        padx=30,
        pady=15
    )


    # --------------------------------------------------------
    # Patient Card
    # --------------------------------------------------------

    patient_card = tk.Frame(
        stats_frame,
        bg="white",
        width=185,
        height=125,
        highlightbackground="#BBDEFB",
        highlightthickness=1
    )

    patient_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )

    patient_icon = tk.Label(
        patient_card,
        text="👤",
        font=("Arial", 20),
        bg="white"
    )

    patient_icon.pack(
        anchor="w",
        padx=18,
        pady=(15, 0)
    )

    patient_title = tk.Label(
        patient_card,
        text="Total Patients",
        font=("Arial", 10),
        bg="white",
        fg="#607D8B"
    )

    patient_title.pack(
        anchor="w",
        padx=18,
        pady=(5, 0)
    )

    patient_count = tk.Label(
        patient_card,
        text="125",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#1976D2"
    )

    patient_count.pack(
        anchor="w",
        padx=18
    )


    # --------------------------------------------------------
    # Doctor Card
    # --------------------------------------------------------

    doctor_card = tk.Frame(
        stats_frame,
        bg="white",
        width=185,
        height=125,
        highlightbackground="#C8E6C9",
        highlightthickness=1
    )

    doctor_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )

    doctor_icon = tk.Label(
        doctor_card,
        text="👨‍⚕️",
        font=("Arial", 20),
        bg="white"
    )

    doctor_icon.pack(
        anchor="w",
        padx=18,
        pady=(15, 0)
    )

    doctor_title = tk.Label(
        doctor_card,
        text="Total Doctors",
        font=("Arial", 10),
        bg="white",
        fg="#607D8B"
    )

    doctor_title.pack(
        anchor="w",
        padx=18,
        pady=(5, 0)
    )

    doctor_count = tk.Label(
        doctor_card,
        text="12",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#388E3C"
    )

    doctor_count.pack(
        anchor="w",
        padx=18
    )


    # --------------------------------------------------------
    # Appointment Card
    # --------------------------------------------------------

    appointment_card = tk.Frame(
        stats_frame,
        bg="white",
        width=185,
        height=125,
        highlightbackground="#FFE0B2",
        highlightthickness=1
    )

    appointment_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )

    appointment_icon = tk.Label(
        appointment_card,
        text="📅",
        font=("Arial", 20),
        bg="white"
    )

    appointment_icon.pack(
        anchor="w",
        padx=18,
        pady=(15, 0)
    )

    appointment_title = tk.Label(
        appointment_card,
        text="Today's Appointments",
        font=("Arial", 10),
        bg="white",
        fg="#607D8B"
    )

    appointment_title.pack(
        anchor="w",
        padx=18,
        pady=(5, 0)
    )

    appointment_count = tk.Label(
        appointment_card,
        text="18",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#F57C00"
    )

    appointment_count.pack(
        anchor="w",
        padx=18
    )


    # --------------------------------------------------------
    # Department Card
    # --------------------------------------------------------

    department_card = tk.Frame(
        stats_frame,
        bg="white",
        width=185,
        height=125,
        highlightbackground="#E1BEE7",
        highlightthickness=1
    )

    department_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(10, 0)
    )

    department_icon = tk.Label(
        department_card,
        text="🏥",
        font=("Arial", 20),
        bg="white"
    )

    department_icon.pack(
        anchor="w",
        padx=18,
        pady=(15, 0)
    )

    department_title = tk.Label(
        department_card,
        text="Departments",
        font=("Arial", 10),
        bg="white",
        fg="#607D8B"
    )

    department_title.pack(
        anchor="w",
        padx=18,
        pady=(5, 0)
    )

    department_count = tk.Label(
        department_card,
        text="8",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#7B1FA2"
    )

    department_count.pack(
        anchor="w",
        padx=18
    )


    # ========================================================
    # Lower Dashboard Area
    # ========================================================

    lower_frame = tk.Frame(
        content_frame,
        bg="#ECEFF1"
    )

    lower_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(10, 25)
    )


    # ========================================================
    # Today's Overview
    # ========================================================

    overview_frame = tk.Frame(
        lower_frame,
        bg="white",
        highlightbackground="#CFD8DC",
        highlightthickness=1
    )

    overview_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )


    overview_title = tk.Label(
        overview_frame,
        text="Today's Overview",
        font=("Arial", 14, "bold"),
        bg="white",
        fg="#263238"
    )

    overview_title.pack(
        anchor="w",
        padx=20,
        pady=(18, 15)
    )


    # Overview rows

    overview_data = [
        ("Appointments", "18"),
        ("Registered Patients", "125"),
        ("Available Doctors", "12"),
        ("Departments", "8")
    ]


    for title, value in overview_data:

        row = tk.Frame(
            overview_frame,
            bg="white"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=7
        )

        title_label = tk.Label(
            row,
            text=title,
            font=("Arial", 10),
            bg="white",
            fg="#607D8B"
        )

        title_label.pack(
            side="left"
        )

        value_label = tk.Label(
            row,
            text=value,
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#263238"
        )

        value_label.pack(
            side="right"
        )


    # ========================================================
    # Quick Actions
    # ========================================================

    actions_frame = tk.Frame(
        lower_frame,
        bg="white",
        highlightbackground="#CFD8DC",
        highlightthickness=1
    )

    actions_frame.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(10, 0)
    )


    actions_title = tk.Label(
        actions_frame,
        text="Quick Actions",
        font=("Arial", 14, "bold"),
        bg="white",
        fg="#263238"
    )

    actions_title.pack(
        anchor="w",
        padx=20,
        pady=(18, 15)
    )


    # Register Patient Button

    patient_button = tk.Button(
        actions_frame,
        text="+  Register Patient",
        font=("Arial", 10, "bold"),
        bg="#1976D2",
        fg="white",
        relief="flat",
        cursor="hand2",
        width=25,
        pady=7
    )

    patient_button.pack(
        padx=20,
        pady=5
    )


    # Register Doctor Button

    doctor_button = tk.Button(
        actions_frame,
        text="+  Register Doctor",
        font=("Arial", 10, "bold"),
        bg="#388E3C",
        fg="white",
        relief="flat",
        cursor="hand2",
        width=25,
        pady=7
    )

    doctor_button.pack(
        padx=20,
        pady=5
    )


    # New Appointment Button

    appointment_button = tk.Button(
        actions_frame,
        text="+  New Appointment",
        font=("Arial", 10, "bold"),
        bg="#F57C00",
        fg="white",
        relief="flat",
        cursor="hand2",
        width=25,
        pady=7
    )

    appointment_button.pack(
        padx=20,
        pady=5
    )