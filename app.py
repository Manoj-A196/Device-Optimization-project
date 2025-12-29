import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Device Optimization for Privacy-Preserving Mobile Computing",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Device Optimization for Privacy-Preserving Mobile Computing")
st.caption("Interactive Working Model | Input → Optimization → Output")

st.divider()

# --------------------------------------------------
# DEVICE INPUT SECTION
# --------------------------------------------------
st.subheader("🔧 Device Input Configuration")

num_devices = st.slider("Number of Mobile Devices", 1, 5, 3)

apps = ["Instagram", "Facebook", "X (Twitter)", "Snapchat", "Google Maps"]

device_inputs = []

for i in range(num_devices):
    st.markdown(f"### 📱 Device {i+1}")

    app = st.selectbox(
        "Select Application",
        apps,
        key=f"app_{i}"
    )

    data_access = st.multiselect(
        "Data Accessed",
        ["Location", "Personal Information", "Usage Data"],
        key=f"data_{i}"
    )

    cpu_usage = st.selectbox(
        "CPU Usage Level",
        ["Low", "Medium", "High"],
        key=f"cpu_{i}"
    )

    network_usage = st.selectbox(
        "Network Usage Level",
        ["Low", "Medium", "High"],
        key=f"net_{i}"
    )

    device_inputs.append({
        "Device": f"Device {i+1}",
        "App": app,
        "Data": data_access,
        "CPU": cpu_usage,
        "Network": network_usage
    })

st.divider()

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def usage_to_num(value):
    return {"Low": 1, "Medium": 2, "High": 3}[value]

def calculate_risk(data, network):
    if "Personal Information" in data or network == "High":
        return 3
    elif "Location" in data:
        return 2
    else:
        return 1

def risk_label(level):
    return {1: "Low 🟢", 2: "Medium 🟠", 3: "High 🔴"}[level]

# --------------------------------------------------
# RUN SIMULATION
# --------------------------------------------------
if st.button("▶ Run Optimization Simulation"):

    centralized_rows = []
    optimized_rows = []
    log_messages = []

    for d in device_inputs:
        # -------- CENTRALIZED PROCESSING --------
        c_cpu = usage_to_num(d["CPU"])
        c_net = usage_to_num(d["Network"])
        c_risk = calculate_risk(d["Data"], d["Network"])

        centralized_rows.append([
            d["Device"],
            d["App"],
            c_cpu,
            c_net,
            risk_label(c_risk)
        ])

        # -------- OPTIMIZED (FEDERATED STYLE) --------
        o_cpu = max(1, c_cpu - 1)
        o_net = 1
        filtered_data = [x for x in d["Data"] if x != "Personal Information"]
        o_risk = calculate_risk(filtered_data, "Low")

        optimized_rows.append([
            d["Device"],
            d["App"],
            o_cpu,
            o_net,
            risk_label(o_risk)
        ])

        log_messages.append(
            f"{d['Device']} → Local processing enabled | Raw data blocked | Optimized update shared"
        )

    # --------------------------------------------------
    # DATAFRAMES
    # --------------------------------------------------
    df_centralized = pd.DataFrame(
        centralized_rows,
        columns=["Device", "App", "CPU Usage", "Network Usage", "Privacy Risk"]
    )

    df_optimized = pd.DataFrame(
        optimized_rows,
        columns=["Device", "App", "CPU Usage", "Network Usage", "Privacy Risk"]
    )

    st.subheader("📊 Centralized vs Optimized Processing")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔴 Centralized Processing")
        st.dataframe(df_centralized, use_container_width=True)

    with col2:
        st.markdown("### 🟢 Optimized (Privacy-Preserving)")
        st.dataframe(df_optimized, use_container_width=True)

    st.divider()

    # --------------------------------------------------
    # PERFORMANCE CHART
    # --------------------------------------------------
    st.subheader("📈 Network Usage Comparison")

    chart_df = pd.DataFrame({
        "Centralized": df_centralized["Network Usage"],
        "Optimized": df_optimized["Network Usage"]
    }, index=df_centralized["Device"])

    st.bar_chart(chart_df)

    st.divider()

    # --------------------------------------------------
    # FEDERATED OPTIMIZATION LOG
    # --------------------------------------------------
    st.subheader("📜 Optimization Process Log")

    for log in log_messages:
        st.code(log)

    st.divider()

    # --------------------------------------------------
    # PRIVACY SUMMARY
    # --------------------------------------------------
    st.subheader("🔐 Privacy Preservation Summary")

    st.success("""
    ✔ Data processed locally on mobile devices  
    ✔ Raw personal information blocked  
    ✔ Reduced network communication  
    ✔ Improved performance and security  
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Academic working model – Device Optimization for Privacy-Preserving Mobile Computing")
