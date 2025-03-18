import streamlit as st
import numpy as np
import os
from PIL import Image
import cv2
import torch
from ultralytics import YOLO

# Load a pre-trained AI model (YOLOv8 for object detection)
def load_ai_model():
    model = YOLO("yolov8n.pt")  # Using a small pre-trained YOLOv8 model
    return model

def detect_hazards(image, job_type, model):
    """AI-based hazard detection using YOLOv8 object detection."""
    hazards = []
    
    # Convert image for OpenCV processing
    image_np = np.array(image.convert('RGB'))
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    # Run YOLOv8 on the image
    results = model(image_np)
    detected_objects = []
    
    for result in results:
        for box in result.boxes:
            cls = result.names[int(box.cls)]
            detected_objects.append(cls)
    
    # Map detected objects to hazard warnings
    if "ladder" in detected_objects and "working at height" in job_type.lower():
        hazards.append("⚠️ Ladder detected - Ensure proper harness use.")
    if "fire extinguisher" not in detected_objects and "welding" in job_type.lower():
        hazards.append("⚠️ No fire extinguisher detected - Fire risk present.")
    if "broken pipe" in detected_objects:
        hazards.append("⚠️ Broken pipe detected - Potential gas leak hazard.")
    
    return hazards, detected_objects

# Load AI model
aio_model = load_ai_model()

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
        hazards, detected_objects = detect_hazards(image, job_type, aio_model)

        # Display detected hazards
        if hazards:
            st.write("#### Detected Hazards:")
            for hazard in hazards:
                st.write(f"- {hazard}")
        else:
            st.write("✅ No specific hazards detected based on AI model.")
        
        # Show detected objects
        st.write("#### Objects Identified in Image:")
        if detected_objects:
            st.write(", ".join(detected_objects))
        else:
            st.write("No recognizable objects detected.")

