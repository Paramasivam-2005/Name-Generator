import streamlit as st
import genai  # Import generate function from genai.py

st.title("🍽️ Restaurant Name Generator")

# Sidebar to select cuisine
cuisine = st.sidebar.selectbox("Select Cuisine", ("Indian", "American", "Chinese"))

# Generate response when a cuisine is selected
if cuisine:
    response = genai.generate(cuisine)  # Call function from genai.py
    
    # Display restaurant name
    st.header(f"🏠 Restaurant Name: {response['restaurant_name'].strip()}")

    # Display menu items
    items = response["menu_items"].strip().split(',')
    st.subheader("📜 Menu Items:")
    
    for item in items:
        st.write(f"🍴 {item.strip()}")
