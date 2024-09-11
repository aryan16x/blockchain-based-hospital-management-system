import streamlit as st
from interect import add_patient, get_patient, get_all_patient_ids

st.title("Blockchain-based Hospital Management with IoT Sensor Data")
st.subheader("ARYAN GADHIYA [21BCT0208]")

# Add new patient
st.subheader("Add New Patient")
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, step=1)
medical_history = st.text_area("Medical History")
treatment = st.text_area("Treatment")

if st.button("Add Patient"):
    tx_hash = add_patient(name, age, medical_history, treatment)
    st.success(f"Patient added successfully! Transaction Hash: {tx_hash}")

# Retrieve patient data
st.subheader("Retrieve Patient Data")
patient_ids = get_all_patient_ids()

if patient_ids:
    selected_id = st.selectbox("Select Patient ID", patient_ids)
    if st.button("Get Patient Details"):
        patient_data = get_patient(selected_id)
        if patient_data:
            st.write(f"ID: {patient_data[0]}")
            st.write(f"Name: {patient_data[1]}")
            st.write(f"Age: {patient_data[2]}")
            st.write(f"Medical History: {patient_data[3]}")
            st.write(f"Treatment: {patient_data[4]}")
            st.write(f"Temperature: {patient_data[5]} °C")
            st.write(f"Heart Rate: {patient_data[6]} bpm")
        else:
            st.error("Patient data not found or error occurred.")
else:
    st.write("No patients found.")
