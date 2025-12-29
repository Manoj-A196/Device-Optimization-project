import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Federated Intelligence – Concept Explainer",
    page_icon="📱",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "users" not in st.session_state:
    st.session_state.users = {}   # stores registered users

if "page" not in st.session_state:
    st.session_state.page = "Login"

# --------------------------------------------------
# AUTHENTICATION PAGES
# --------------------------------------------------
def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users:
            if st.session_state.users[username] == password:
                st.session_state.authenticated = True
                st.session_state.page = "Introduction"
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Incorrect password")
        else:
            st.error("User not registered")

    st.markdown("Don't have an account?")
    if st.button("Register Now"):
        st.session_state.page = "Register"
        st.rerun()


def register_page():
    st.title("📝 Register")

    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if not new_user or not new_pass:
            st.error("All fields are required")
        elif new_user in st.session_state.users:
            st.error("Username already exists")
        elif new_pass != confirm_pass:
            st.error("Passwords do not match")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("Registration successful")
            st.session_state.page = "Login"
            st.rerun()

    if st.button("Back to Login"):
        st.session_state.page = "Login"
        st.rerun()


def logout():
    st.session_state.authenticated = False
    st.session_state.page = "Login"
    st.rerun()

# --------------------------------------------------
# MAIN CONTENT PAGES
# --------------------------------------------------
def introduction():
    st.title("📱 Federated Intelligence for Privacy-Preserving Mobile Computing")

    st.markdown("""
    The rapid growth of mobile applications has resulted in the generation of
    large volumes of sensitive user data such as personal information, location
    details, and usage patterns.

    Traditional mobile computing systems rely on **centralized cloud processing**,
    which introduces serious concerns related to data privacy and security.

    **Federated Intelligence** enables decentralized computation where data
    remains on user devices.
    """)

    st.success("✔ Raw user data never leaves the mobile device")


def problem_statement():
    st.title("⚠ Problem Statement")

    st.markdown("""
    Modern mobile applications transmit sensitive user data to centralized cloud
    servers for processing, increasing the risk of data breaches and unauthorized
    access.

    Existing architectures struggle to balance intelligent processing with
    strong privacy guarantees.
    """)

    st.warning("A decentralized and privacy-preserving approach is required.")


def federated_flow():
    st.title("🔄 Federated Intelligence Workflow")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Process Steps")
        st.markdown("""
        1. Data generated on mobile devices  
        2. Local computation performed  
        3. Model updates shared  
        4. Secure aggregation  
        5. Global model distribution  
        """)

    with col2:
        st.subheader("Privacy Benefits")
        st.markdown("""
        - No raw data sharing  
        - Reduced security risks  
        - Enhanced user trust  
        """)


def architecture():
    st.title("🏗 System Architecture")

    st.image(
        "assets/architecture.png",
        caption="Federated Mobile Computing Architecture",
        use_column_width=True
    )

    st.markdown("""
    - **Mobile Layer:** Local data processing  
    - **Network Layer:** Secure communication  
    - **Cloud Layer:** Aggregation and coordination  
    - **Optimization Layer:** Performance and scalability  
    """)


def modules():
    st.title("📦 Module Explanation")

    with st.expander("Module 1 – Federated Mobile Computing Framework"):
        st.write("""
        Mobile devices perform local computation using private data.
        Only model updates are shared for collaborative intelligence.
        """)

    with st.expander("Module 2 – Privacy Preservation and Optimization"):
        st.write("""
        Privacy is preserved by keeping raw data on devices.
        Optimization techniques reduce communication overhead.
        """)

    with st.expander("Module 3 – Security and Performance Management"):
        st.write("""
        Secure authentication and encrypted communication
        ensure reliable and efficient system operation.
        """)


def conclusion():
    st.title("✅ Conclusion")

    st.markdown("""
    Federated intelligence provides an effective solution for
    privacy-preserving mobile computing by eliminating centralized
    data collection.

    The approach improves security, scalability, and user trust
    while maintaining efficient system performance.
    """)


# --------------------------------------------------
# ROUTING LOGIC
# --------------------------------------------------
if not st.session_state.authenticated:
    if st.session_state.page == "Login":
        login_page()
    elif st.session_state.page == "Register":
        register_page()
else:
    st.sidebar.title("📘 Navigation")
    choice = st.sidebar.radio(
        "Select Section",
        [
            "Introduction",
            "Problem Statement",
            "Federated Intelligence Flow",
            "System Architecture",
            "Module Explanation",
            "Conclusion"
        ]
    )

    st.sidebar.button("🚪 Logout", on_click=logout)

    if choice == "Introduction":
        introduction()
    elif choice == "Problem Statement":
        problem_statement()
    elif choice == "Federated Intelligence Flow":
        federated_flow()
    elif choice == "System Architecture":
        architecture()
    elif choice == "Module Explanation":
        modules()
    elif choice == "Conclusion":
        conclusion()
