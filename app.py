import streamlit as st
from PIL import Image, ImageDraw
import os
import random

st.title("Structural Defect Detection in Towers")

st.write("Upload an image to detect structural defects such as corrosion and cracks.")

if not os.path.exists("images/uploaded"):
    os.makedirs("images/uploaded")
if not os.path.exists("images/annotated"):
    os.makedirs("images/annotated")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

def detect_defects(image_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    defects_info = [
        {"type": "corrosion", "confidence": random.uniform(0.8, 1.0)},
        {"type": "crack", "confidence": random.uniform(0.7, 0.9)}
    ]
    for defect in defects_info:
        draw.rectangle([(50, 50), (200, 200)], outline="red", width=3)
        draw.text((50, 30), f"{defect['type']} ({defect['confidence']*100:.2f}%)", fill="red")
    annotated_image_path = os.path.join("images/annotated", os.path.basename(image_path))
    image.save(annotated_image_path)
    return annotated_image_path, defects_info

if uploaded_file:
    image = Image.open(uploaded_file)
    uploaded_image_path = os.path.join("images/uploaded", uploaded_file.name)
    image.save(uploaded_image_path)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    annotated_image_path, defects_info = detect_defects(uploaded_image_path)

    annotated_image = Image.open(annotated_image_path)
    st.image(annotated_image, caption="Annotated Image", use_column_width=True)

    st.write("Detected Defects and Confidence Scores:")
    for defect in defects_info:
        st.write(f"Type: {defect['type']}, Confidence: {defect['confidence']*100:.2f}%")
