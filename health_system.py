# PROG211 - Health - Patient Record System
# DPG Compliant

class Patient:
    total_patients = 0

    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        Patient.total_patients += 1

    def display_info(self): # instance method - Lecture 3
        return f"[Patient] ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}"

    def update_record(self, new_diagnosis): # method required in Task 1
        self.diagnosis = new_diagnosis

    @classmethod
    def get_total_patients(cls): # class method - Lecture 3
        return cls.total_patients

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display_info(self):
        return f"[Doctor] ID: {self.doctor_id}, Name: {self.name}, Spec: {self.specialization}"

# Task 2 - ONE data structure only: Dictionary
hospital_db = {}

def add_patient(patient):
    hospital_db[patient.patient_id] = patient

def display_all():
    for p in hospital_db.values():
        print(p.display_info())

# Object creation and interaction
p1 = Patient(101, "Mohamed Sesay", 30, "Malaria")
p2 = Patient(102, "Fatima Conteh", 25, "Typhoid")
p3 = Patient(103, "Abu Bakarr", 40, "Checkup")
d1 = Doctor(1, "Dr. Kamara", "General")

add_patient(p1)
add_patient(p2)
add_patient(p3)

display_all()
print(f"Total Patients: {Patient.get_total_patients()}")
print(f"Doctor: {d1.display_info()}")