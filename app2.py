import streamlit as st
import pandas as pd

# Title of the app
st.title("Nzuzos Profile")

st.header ("Education")
st. write ("Curro Grantleigh College: NSC (2016 - 2020)")
st.write ("University of the Western Cape: BSc Medical Bioacience (2021 - 2023)")
st. write ("University of the Western Cape: BSc Medical Bioscience (Hons) (2024 - 2024)")
st. write ("Stellenbosch University/SAMRC: MSc Computational Biology and Bioinformatics (2025 - Current)")

# Collect basic information
name = "Nzuzo Mdluli"
field = "Computational Biology and Bioinformatics"
institution = "Stellenbosch Univerisity"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")




st.header ("Research Field")
st.write ("Bioinformatics is a field that combines biology, computer science, and information technology to analyze and interpret biological data, particularly large datasets like genetic sequences, protein structures, and molecular interactions. It involves using computational tools and algorithms to store, manage, and analyze complex biological data to gain insights into areas like genetics, evolution, drug discovery, and personalized medicine.")
st.write ("MERS-CoV (Middle East Respiratory Syndrome Coronavirus) is a virus that emerged in 2012 and causes severe respiratory illness in humans. The virus, like other coronaviruses, interacts with the human immune system, including T cells, which are crucial for adaptive immunity. The adaptation of MERS-CoV to T cell immune responses, particularly at immunodominant epitopes, is an important area of study in understanding how the virus evades immune recognition and persists or leads to disease.")



# Add a contact section
st.header("Contact Information")
email = "lindonzuzo@icloud.com"
number = "0781925077"
st.write(f"You can reach {name} at {email}.")