import streamlit as st
import cv2
import numpy as np
import os
from PIL import Image
import tensorflow as tf

# Placeholder function for hazard detection (AI Model can be integrated here)
def detect_hazards(image, job_type):
    """Analyze the image and return detected hazards based on job type."""
    hazards = []
    
    # Example hazard recognition logic
    if job_type.lower() == "working at height":
        hazards.append("Ensure harness and fall protection are visible.")
    elif job_type.lower() == "welding":
        hazards.append("Check for eye protection and fire hazards.")
    elif job_type.lower() == "lifting operation":
        hazards.append("Confirm slings and lifting points are correctly attached.")
    
    # Placeholder: AI model could analyze PPE detection, obstructions, etc.
    hazards.append("(AI Detection Placeholder: Hazard identification pending model integration)")
    
    return hazards

# Streamlit App
st.title("AI Hazard Recognition Prototype")

# Step 1: Ask for the Job Type
job_type = st.text_input("Enter the job you are performing:")

# Step 2: Upload up to 5 Images
uploaded_images = st.file_uploader("Upload up to 5 photos of the work area", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_images and job_type:
    st.write(f"### Job: {job_type}")
    st.write("### Uploaded Images:")
    
    for uploaded_file in uploaded_images:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded: {uploaded_file.name}", use_column_width=True)
        
        # Perform hazard detection
        hazards = detect_hazards(image, job_type)

        # Display detected hazards
        if hazards:
            st.write("#### Detected Hazards:")
            for hazard in hazards:
                st.write(f"- {hazard}")
        else:
            st.write("No hazards detected (yet). AI model improvements required.")
