import streamlit as st
import random
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Federated Intelligence – Working Model",
    page_icon="📱",
    layout="wide"
)

st.title("🤖 Federated Intelligence – Demo Working Model")
st.caption("Privacy-Preserving Mobile Computing Simulation")

st.divider()

# --------------------------------------------------
# CONFIGURATION PANEL
# --------------------------------------------------
st.sidebar.header("⚙️ Simulation Configuration")

num_devices = st.sidebar.slider("Number of Mobile Devices", 2, 10, 5)
participation_rate = st.sidebar.slider("Device Participation (%)", 50, 100, 80)
rounds = st.sidebar.slider("Federated Rounds", 1, 5, 3)

start = st.sidebar.button("▶ Start Simulation")

# --------------------------------------------------
# INITIALIZATION
# --------------------------------------------------
if "global_accuracy" not in st.session_state:
    st.session_state.global_accuracy = 50.0

# --------------------------------------------------
# MAIN DEMO
# --------------------------------------------------
if start:
    st.subheader("📱 Local Device Training")

    participating_devices = int(num_devices * participation_rate / 100)
    device_updates = []

    cols = st.columns(2)

    for i in range(participating_devices):
        with cols[i % 2]:
            st.markdown(f"**Device {i+1}**")

            local_accuracy = random.uniform(45, 60)
            progress = st.progress(0)

            for step in range(100):
                time.sleep(0.01)
                progress.progress(step + 1)

            update = random.uniform(1.0, 3.0)
            device_updates.append(update)

            st.success(f"Update Sent: +{update:.2f}")
            st.caption("🔒 Raw data stayed on device")

    st.divider()

    # --------------------------------------------------
    # AGGREGATION
    # --------------------------------------------------
    st.subheader("☁️ Secure Aggregation Server")

    if device_updates:
        aggregated_update = sum(device_updates) / len(device_updates)
        st.session_state.global_accuracy += aggregated_update

        st.metric(
            label="🌍 Global Model Accuracy",
            value=f"{st.session_state.global_accuracy:.2f}%",
            delta=f"+{aggregated_update:.2f}"
        )

        st.success("Model updates aggregated successfully")
    else:
        st.error("No devices participated")

    st.divider()

    # --------------------------------------------------
    # PRIVACY STATUS
    # --------------------------------------------------
    st.subheader("🔐 Privacy Verification")

    st.info("""
    ✔ Raw user data: **NOT SHARED**  
    ✔ Model updates only: **SHARED**  
    ✔ Central data storage: **NOT USED**  
    """)

    st.success("Privacy Preserved via Federated Intelligence")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Academic demo – simulated federated intelligence working model")
