!pip install streamlit pyngrok reportlab
import pandas as pd
import streamlit as st
from datetime import datetime
from reportlab.pdfgen import canvas
from pyngrok import ngrok
import re
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(flight_data, flight_id):
    flight = flight_data.iloc[flight_id]
    filename = f"Flight_{flight_id}_Report.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, f"Flight Report - Flight ID: {flight_id}")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Date of Flight Operations: {flight['Date']}")
    c.drawString(50, height - 120, f"Aircraft Registration: {flight['Aircraft Registration']}")
    c.drawString(50, height - 140, f"From Location: {flight['From']} - Planned Departure: {flight['Planned Departure']} / Actual: {flight['Actual Departure']}")
    c.drawString(50, height - 160, f"Arrival Location: {flight['To']} - Planned Arrival: {flight['Planned Arrival']} / Actual: {flight['Actual Arrival']}")
    planned_duration = flight['Planned Duration']
    actual_duration = flight['Actual Duration']
    c.drawString(50, height - 180, f"Planned Duration: {planned_duration}")
    c.drawString(50, height - 200, f"Actual Duration: {actual_duration}")
    expenses = {"Catering": 200, "Landing and Navigation": 150, "Crew Hotel": 300, "Ground Handling": 400, "Miscellaneous": 100}
    total_expense = sum(expenses.values())
    c.drawString(50, height - 240, "Expenses:")
    y = height - 260
    for category, amount in expenses.items():
        c.drawString(70, y, f"{category}: ${amount}")
        y -= 20
    c.drawString(50, y, f"Total Expenses: ${total_expense}")
    c.save()
    return filename

def app():
    st.title("Flight Management System")

    st.subheader("Add New Flight Record")
    date_of_operation = st.date_input("Date of Flight Operations")
    aircraft_registration = st.text_input("Aircraft Registration")
    from_location = st.text_input("From Location (ICAO/IATA)")
    if from_location and not validate_location_code(from_location):
        st.error("Location code must be 3 or 4 uppercase alphabetic characters (ICAO/IATA code).")
    planned_departure_time = st.time_input("Planned Time of Departure")
    actual_departure_time = st.time_input("Actual Time of Departure")
    arrival_location = st.text_input("Arrival Location (ICAO/IATA)")
    if arrival_location and not validate_location_code(arrival_location):
        st.error("Location code must be 3 or 4 uppercase alphabetic characters (ICAO/IATA code).")
    planned_arrival_time = st.time_input("Planned Time of Arrival")
    actual_arrival_time = st.time_input("Actual Time of Arrival")

    if st.button("Add Flight Record"):
        if is_unique_record(flight_data, date_of_operation, aircraft_registration):
            new_record = {
                "Date": date_of_operation,
                "Aircraft Registration": aircraft_registration,
                "From": from_location,
                "Planned Departure": planned_departure_time,
                "Actual Departure": actual_departure_time,
                "To": arrival_location,
                "Planned Arrival": planned_arrival_time,
                "Actual Arrival": actual_arrival_time
            }
            flight_data.append(new_record, ignore_index=True)
            save_flight_data(flight_data)
            st.success("Flight record added successfully!")
        else:
            st.error("A record with this date and registration already exists.")

    # Export PDF Button
    for idx, row in flight_data.iterrows():
        if st.button(f"Export Flight ID {idx} to PDF"):
            pdf_file = generate_pdf(flight_data, idx)
            with open(pdf_file, "rb") as pdf:
                st.download_button("Download PDF", pdf, file_name=pdf_file, mime="application/pdf")
              import os
os.environ["saudia"] = "xxxxxxxxxxxxxxxxxxxxxxx"
from pyngrok import ngrok

# Start ngrok tunnel on port 8501 using HTTP protocol
public_url = ngrok.connect(addr="8501", proto="http")
print("Streamlit app running at:", public_url)

# Run Streamlit app
!streamlit run app.py
