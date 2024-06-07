import streamlit as st
import pandas as pd
import os

# Define the range of pages
pages = list(range(23, 42))

# Add the title
st.title("IGCSE Spanish-English Vocabulary")

# Add custom CSS to change the font size in the main content and sidebar
st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
    }
    .bold-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .sidebar .sidebar-content {
        font-size:24px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Create a sidebar with a selection box for the user to choose a page number
page_number = st.sidebar.selectbox('Select a page number:', pages)

# Generate the corresponding CSV filename
csv_filename = f"IGCSE 2022-24-sy - {page_number}.csv"

# Load the CSV file
if os.path.exists(csv_filename):
    df = pd.read_csv(csv_filename)
    if not df.empty:
        st.write(f"Words from page {page_number}")
        for i, row in df.iterrows():
            spanish_word = row['Spanish']
            english_word = row['English']

            col1, col2, col3 = st.columns([2, 1, 2])
            with col1:
                st.markdown(f"<div class='big-font'>{spanish_word}</div>", unsafe_allow_html=True)
            with col2:
                if st.button(f"Reveal {i}", key=f"button_{i}"):
                    with col3:
                        st.markdown(f"<div class='bold-font'>{english_word}</div>", unsafe_allow_html=True)
else:
    st.write(f"CSV file for page {page_number} not found.")
