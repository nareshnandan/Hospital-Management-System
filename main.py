import tkinter as tk
from datetime import datetime

from screens.dashboard import show_dashboard
from screens.patients import show_patients
from screens.doctors import show_doctors


# ============================================================
# Main Window
# ============================================================

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("900x600")
root.configure(bg="white")


# ============================================================
# Header Frame
# ============================================================

header_frame = tk.Frame(
    root,
    bg="#1976D2",
    height=70
)

header_frame.pack(fill="x")


# Header Title
header_title = tk.Label(
    header_frame,
    text="Hospital Management System",
    font=("Arial", 20, "bold"),
    bg="#1976D2",
    fg="white"
)

header_title.pack(
    side="left",
    padx=20,
    pady=15
)


# Date Label
date_label = tk.Label(
    header_frame,
    text=datetime.now().strftime("%d-%m-%Y"),
    font=("Arial", 11),
    bg="#1976D2",
    fg="white"
)

date_label.pack(
    side="right",
    padx=20
)


# Admin Label
admin_label = tk.Label(
    header_frame,
    text="Admin",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white"
)

admin_label.pack(
    side="right",
    padx=10
)


# ============================================================
# Navigation Frame
# ============================================================

navigation_frame = tk.Frame(
    root,
    bg="#263238",
    width=200
)

navigation_frame.pack(
    side="left",
    fill="y"
)


# ============================================================
# Content Frame
# ============================================================

content_frame = tk.Frame(
    root,
    bg="#ECEFF1"
)

content_frame.pack(
    side="right",
    fill="both",
    expand=True
)


# ============================================================
# Navigation Buttons
# ============================================================

# Dashboard Button
dashboard_button = tk.Button(
    navigation_frame,
    text="Dashboard",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat",
    command=lambda: show_dashboard(content_frame)
)

dashboard_button.pack(
    fill="x",
    padx=10,
    pady=5
)


# Patients Button
patients_button = tk.Button(
    navigation_frame,
    text="Patients",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat",
    command=lambda: show_patients(content_frame)
)

patients_button.pack(
    fill="x",
    padx=10,
    pady=5
)


# Doctors Button
doctors_button = tk.Button(
    navigation_frame,
    text="Doctors",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat",
    command=lambda: show_doctors(content_frame)
)

doctors_button.pack(
    fill="x",
    padx=10,
    pady=5
)


# Appointments Button
appointments_button = tk.Button(
    navigation_frame,
    text="Appointments",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat"
)

appointments_button.pack(
    fill="x",
    padx=10,
    pady=5
)


# Reports Button
reports_button = tk.Button(
    navigation_frame,
    text="Reports",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat"
)

reports_button.pack(
    fill="x",
    padx=10,
    pady=5
)


# Settings Button
settings_button = tk.Button(
    navigation_frame,
    text="Settings",
    font=("Arial", 12),
    bg="#263238",
    fg="white",
    relief="flat"
)

settings_button.pack(
    fill="x",
    padx=10,
    pady=5
)


# ============================================================
# Show Dashboard When Application Starts
# ============================================================

show_dashboard(content_frame)


# ============================================================
# Start Application
# ============================================================

root.mainloop()