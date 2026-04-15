import streamlit as st
import random
import time

# Set the page configuration
st.set_page_config(
    page_title="Air Quality Index Monitor",
    page_icon="🌍",
    layout="wide",
)

# Title and description
st.title("🌍 Air Quality Index Monitor")
st.write("This IoT-based interface displays real-time Air Quality Index (AQI) measurements. The AQI values are simulated for demonstration purposes.")

# Sidebar for user input
st.sidebar.title("Settings")
update_interval = st.sidebar.slider("Update Interval (seconds)", 1, 10, 2)
pollutant_options = ["PM2.5", "PM10", "CO", "SO2", "NO2", "O3"]
selected_pollutant = st.sidebar.selectbox("Select Pollutant to Monitor", pollutant_options)

# Simulate AQI readings
def generate_aqi_data():
    return {
        "PM2.5": random.randint(0, 500),
        "PM10": random.randint(0, 500),
        "CO": random.uniform(0.0, 50.0),
        "SO2": random.randint(0, 500),
        "NO2": random.randint(0, 500),
        "O3": random.randint(0, 500),
    }

# Display AQI levels
aqi_levels = {
    "Good": (0, 50),
    "Moderate": (51, 100),
    "Unhealthy for Sensitive Groups": (101, 150),
    "Unhealthy": (151, 200),
    "Very Unhealthy": (201, 300),
    "Hazardous": (301, 500),
}

def get_aqi_category(aqi_value):
    for category, (low, high) in aqi_levels.items():
        if low <= aqi_value <= high:
            return category
    return "Unknown"

# Main UI components
aqi_placeholder = st.empty()

st.write("### AQI Levels")
st.table(aqi_levels)

st.write("### Real-Time AQI Monitor")
while True:
    aqi_data = generate_aqi_data()
    selected_aqi = aqi_data[selected_pollutant]
    category = get_aqi_category(selected_aqi)
    
    with aqi_placeholder.container():
        st.metric(label="Selected Pollutant", value=selected_pollutant)
        st.metric(label="Current AQI", value=selected_aqi, delta=f"Category: {category}")
    
    time.sleep(update_interval)
