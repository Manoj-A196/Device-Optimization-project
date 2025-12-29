import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Device Optimization Demo",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Device Optimization for Privacy-Preserving Mobile Computing")
st.caption("Input → Optimization → Output (Working Demo Model)")

st.divider()

# --------------------------------------------------
# USER INPUT SECTION
# --------------------------------------------------
st.subheader("🔧 Device / App Input Configuration")

app_name = st.selectbox(
    "Select Mobile Application",
    ["Instagram", "Facebook", "X (Twitter)", "Snapchat", "Google Maps", "Music Player"]
)

data_access = st.multiselect(
    "Select Data Accessed by App",
    ["Location", "Personal Information", "Usage Data"]
)

cpu_usage = st.selectbox(
    "CPU Usage Level",
    ["Low", "Medium", "High"]
)

network_usage = st.selectbox(
    "Network Usage Level",
    ["Low", "Medium", "High"]
)

st.divider()

# --------------------------------------------------
# RISK CALCULATION FUNCTION
# --------------------------------------------------
def calculate_risk(data, cpu, network):
    if "Personal Information" in data or network == "High":
        return "High 🔴"
    elif "Location" in data:
        return "Medium 🟠"
    else:
        return "Low 🟢"

# --------------------------------------------------
# OPTIMIZATION BUTTON
# --------------------------------------------------
if st.button("⚙️ Optimize Device"):
    st.subheader("📊 System Processing & Output")

    # Before optimization
    before_risk = calculate_risk(data_access, cpu_usage, network_usage)

    st.markdown("### 🔴 Before Optimization")
    st.write(f"**App Name:** {app_name}")
    st.write(f"**Privacy Risk:** {before_risk}")
    st.write(f"**CPU Usage:** {cpu_usage}")
    st.write(f"**Network Usage:** {network_usage}")

    st.divider()

    # --------------------------------------------------
    # OPTIMIZATION LOGIC
    # --------------------------------------------------
    optimized_cpu = "Low" if cpu_usage != "Low" else "Low"
    optimized_network = "Low"

    optimized_data = [
        d for d in data_access if d != "Personal Information"
    ]

    after_risk = calculate_risk(optimized_data, optimized_cpu, optimized_network)

    # After optimization
    st.markdown("### 🟢 After Optimization")
    st.write(f"**Optimized CPU Usage:** {optimized_cpu}")
    st.write(f"**Optimized Network Usage:** {optimized_network}")
    st.write(f"**Blocked Raw Data:** Personal Information")
    st.write(f"**Privacy Risk:** {after_risk}")

    st.success("Device optimized successfully with privacy preservation")

    st.divider()

    # --------------------------------------------------
    # PRIVACY CONFIRMATION
    # --------------------------------------------------
    st.subheader("🔐 Privacy Preservation Status")

    st.info("""
    ✔ Raw personal data blocked  
    ✔ Data processed locally on device  
    ✔ Reduced network communication  
    ✔ Improved performance and security  
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Interactive working model – academic demonstration")
