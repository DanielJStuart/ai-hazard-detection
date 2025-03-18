import streamlit as st
import numpy as np
import os
from PIL import Image
import cv2
import tensorflow as tf

# Load a pre-trained AI model (placeholder for now)
def load_ai_model():
    # This should be replaced with an actual trained model for hazard detection
    model = None  # Placeholder
    return model

def detect_hazards(image, job_type, model):
    """AI-based hazard detection using image recognition."""
    hazards = []
    
    # Convert image for OpenCV processing
    image = np.array(image.convert('RGB'))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Placeholder AI processing (replace with real AI detection model)
    if "welding" in job_type.lower():
        hazards.append("⚠️ Fire risk detected - Ensure fire blankets are used.")
    
    if "working at height" in job_type.lower():
        hazards.append("⚠️ Fall hazard detected - Check for proper harness use.")
        hazards.append("⚠️ Unstable footing - Ensure safety barriers are in place.")
    
    if "lifting" in job_type.lower():
        hazards.append("⚠️ Load imbalance detected - Verify correct sling angles.")
        hazards.append("⚠️ Personnel too close - Ensure safe lifting distance.")
    
    # AI-based detection logic goes here (e.g., model prediction)
    # For now, returning placeholder hazards
    return hazards

# Load AI model (placeholder for now)
ai_model = load_ai_model()

# Streamlit UI
st.title("AI Offshore Hazard Detection")
st.write("Upload images and specify the job type to identify potential hazards using AI.")

# User Input
job_type = st.text_input("Enter the job/task being performed (e.g., 'Welding', 'Lifting', 'Working at Height')")

# File Upload
uploaded_images = st.file_uploader("Upload images (up to 5)", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Process Images
if uploaded_images and job_type:
    st.write(f"### Job: {job_type}")
    st.write("### Uploaded Images:")
    
    for uploaded_file in uploaded_images:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded: {uploaded_file.name}", use_container_width=True)
        
        # Perform AI hazard detection
        hazards = detect_hazards(image, job_type, ai_model)

        # Display detected hazards
        if hazards:
            st.write("#### Detected Hazards:")
            for hazard in hazards:
                st.write(f"- {hazard}")
        else:
            st.write("✅ No hazards detected. AI model improvements needed.")

