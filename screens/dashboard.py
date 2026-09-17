import tkinter as tk


def show_dashboard(content_frame):

    # Remove existing widgets from content area
    for widget in content_frame.winfo_children():
        widget.destroy()


    # ========================================================
    # Dashboard Title
    # ========================================================

    dashboard_title = tk.Label(
        content_frame,
        text="Dashboard",
        font=("Arial", 22, "bold"),
        bg="#ECEFF1",
        fg="#263238"
    )

    dashboard_title.pack(
        anchor="w",
        padx=30,
        pady=(25, 5)
    )


    # ========================================================
    # Welcome Message
    # ========================================================

    welcome_label = tk.Label(
        content_frame,
        text="Welcome to Hospital Management System",
        font=("Arial", 12),
        bg="#ECEFF1",
        fg="#546E7A"
    )

    welcome_label.pack(
        anchor="w",
        padx=30,
        pady=5
    )


    # ========================================================
    # Statistics Frame
    # ========================================================

    stats_frame = tk.Frame(
        content_frame,
        bg="#ECEFF1"
    )

    stats_frame.pack(
        fill="x",
        padx=30,
        pady=25
    )


    # ========================================================
    # Patient Card
    # ========================================================

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

    patient_title.pack(
        pady=(20, 5)
    )

    patient_count = tk.Label(
        patient_card,
        text="125",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="#1976D2"
    )

    patient_count.pack()

    # ========================================================
    # Doctor Card
    # ========================================================

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

    doctor_title.pack(
        pady=(20, 5)
    )

    doctor_count = tk.Label(
        doctor_card,
        text="12",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="#1976D2"
    )

    doctor_count.pack()

    # ========================================================
    # Appointment Card
    # ========================================================

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

    appointment_title.pack(
        pady=(20, 5)
    )


    appointment_count = tk.Label(
        appointment_card,
        text="18",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="#1976D2"
    )

    appointment_count.pack()