import sqlite3


# ========================================================
# Database Connection
# ========================================================

def get_connection():

    connection = sqlite3.connect("hospital.db")

    return connection


# ========================================================
# Create Database Tables
# ========================================================

def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    # ----------------------------------------------------
    # Patients Table
    # ----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (

            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            blood_group TEXT NOT NULL

        )
    """)

    # ----------------------------------------------------
    # Doctors Table
    # ----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (

            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            experience INTEGER NOT NULL,
            fee REAL NOT NULL

        )
    """)

    # ----------------------------------------------------
    # Appointments Table
    # ----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (

            id TEXT PRIMARY KEY,
            patient_id TEXT NOT NULL,
            doctor_id TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            reason TEXT NOT NULL

        )
    """)

    connection.commit()
    connection.close()