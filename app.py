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
st.caption("Input → Processing → Output (Working Demo Model)")

st.divider()

# --------------------------------------------------
# FIXED DEVICES (NO SLIDER)
# --------------------------------------------------
st.subheader("🔧 Mobile Device Inputs")

devices = [
    {"Device": "Device 1", "App": "Instagram"},
    {"Device": "Device 2", "App": "Facebook"},
    {"Device": "Device 3", "App": "Google Maps"}
]

device_inputs = []

for i, d in enumerate(devices):
    st.markdown(f"### 📱 {d['Device']} – {d['App']}")

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
        "Device": d["Device"],
        "App": d["App"],
        "Data": data_access,
        "CPU": cpu_usage,
        "Network": network_usage
    })

st.divider()

# --------------------------------------------------
# HELPER FUNCTIONS (IMPORTANT)
# --------------------------------------------------
def to_numeric(value):
    return {"Low": 1, "Medium": 2, "High": 3}[value]

def risk_level(data, network):
    if "Personal Information" in data or network == "High":
        return "High 🔴"
    elif "Location" in data:
        return "Medium 🟠"
    else:
        return "Low 🟢"

# --------------------------------------------------
# RUN OPTIMIZATION
# --------------------------------------------------
if st.button("▶ Run Device Optimization"):

    centralized_rows = []
    optimized_rows = []

    for d in device_inputs:
        # ---------- CENTRALIZED ----------
        c_cpu = to_numeric(d["CPU"])
        c_net = to_numeric(d["Network"])
        c_risk = risk_level(d["Data"], d["Network"])

        centralized_rows.append({
            "Device": d["Device"],
            "CPU": c_cpu,
            "Network": c_net,
            "Privacy Risk": c_risk
        })

        # ---------- OPTIMIZED ----------
        o_cpu = max(1, c_cpu - 1)
        o_net = 1
        filtered_data = [x for x in d["Data"] if x != "Personal Information"]
        o_risk = risk_level(filtered_data, "Low")

        optimized_rows.append({
            "Device": d["Device"],
            "CPU": o_cpu,
            "Network": o_net,
            "Privacy Risk": o_risk
        })

    # --------------------------------------------------
    # DATAFRAMES
    # --------------------------------------------------
    df_c = pd.DataFrame(centralized_rows)
    df_o = pd.DataFrame(optimized_rows)

    st.subheader("📊 Processing Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔴 Centralized")
        st.dataframe(df_c, use_container_width=True)

    with col2:
        st.markdown("### 🟢 Optimized")
        st.dataframe(df_o, use_container_width=True)

    st.divider()

    # --------------------------------------------------
    # BAR GRAPH (GUARANTEED VISIBLE)
    # --------------------------------------------------
    st.subheader("📈 Network Usage Comparison (Before vs After)")

    graph_df = pd.DataFrame({
        "Centralized": df_c["Network"].values,
        "Optimized": df_o["Network"].values
    }, index=df_c["Device"])

    st.bar_chart(graph_df)

    st.caption("1 = Low, 2 = Medium, 3 = High")

    st.divider()

    # --------------------------------------------------
    # PRIVACY SUMMARY
    # --------------------------------------------------
    st.subheader("🔐 Privacy Preservation Result")

    st.success("""
    ✔ Raw personal data blocked  
    ✔ Data processed locally  
    ✔ Network usage reduced  
    ✔ Device performance optimized  
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Academic working model – Device Optimization for Privacy-Preserving Mobile Computing")
