import streamlit as st
import pandas as pd

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------
st.set_page_config(
    page_title="Privacy Tracking Demo",
    page_icon="🔐",
    layout="wide"
)

st.title("🔍 Device Privacy Tracking – Working Model")
st.caption("Simulation of raw data and sensitive information tracking in mobile devices")

st.divider()

# ---------------------------------------
# SIMULATED DEVICE / APP DATA
# ---------------------------------------
data = {
    "Device / App Name": [
        "Instagram",
        "Facebook",
        "X (Twitter)",
        "Snapchat",
        "Location Tracker Service",
        "Fitness App",
        "Camera Service",
        "System Analytics",
        "Music Player"
    ],
    "Tracks Location": [
        "Yes", "Yes", "Yes", "Yes",
        "Yes", "No", "No", "No", "No"
    ],
    "Tracks Personal Info": [
        "Yes", "Yes", "Yes", "Yes",
        "No", "No", "No", "No", "No"
    ],
    "Tracks Usage Data": [
        "Yes", "Yes", "Yes", "Yes",
        "Yes", "Yes", "No", "Yes", "No"
    ],
    "Tracks Raw Data": [
        "Yes", "Yes", "Yes", "Yes",
        "Yes", "No", "No", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# ---------------------------------------
# RISK LEVEL CALCULATION
# ---------------------------------------
def calculate_risk(row):
    if row["Tracks Raw Data"] == "Yes":
        return "High 🔴"
    elif row["Tracks Personal Info"] == "Yes":
        return "Medium 🟠"
    else:
        return "Low 🟢"

df["Privacy Risk Level"] = df.apply(calculate_risk, axis=1)

# ---------------------------------------
# DISPLAY TABLE
# ---------------------------------------
st.subheader("📱 Detected Devices / Applications")
st.dataframe(df, use_container_width=True)

st.divider()

# ---------------------------------------
# RAW DATA TRACKING ALERT
# ---------------------------------------
st.subheader("🚨 Raw Data Tracking Detection")

raw_tracking = df[df["Tracks Raw Data"] == "Yes"]

for device in raw_tracking["Device / App Name"]:
    st.error(f"⚠️ {device} is tracking RAW USER DATA")

st.divider()

# ---------------------------------------
# PRIVACY SUMMARY
# ---------------------------------------
st.subheader("🔐 Privacy Status Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Apps", len(df))
col2.metric("Raw Data Tracking Apps", len(raw_tracking))
col3.metric("Overall Privacy Status", "At Risk 🔴")

st.info("""
✔ This is a simulated privacy monitoring model  
✔ Real-world app names are used for demonstration  
✔ No real user data is accessed  
✔ Shows why privacy-preserving systems are needed
""")

st.caption("Academic demo – simulated privacy tracking working model")
