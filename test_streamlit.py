import streamlit as st
from app.data.db import connect_database
from app.data.incidents import get_all_incidents, insert_incident
from app.services.user_service import login_user

# --------------------------
# LOGIN SYSTEM
# --------------------------

st.title("Streamlit Test — Backend Check")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        success, msg = login_user(username, password)

        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error(msg)

    st.stop()


# --------------------------
# MAIN APP AFTER LOGIN
# --------------------------

st.success(f"Logged in as: {st.session_state.username}")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.experimental_rerun()

conn = connect_database()

st.subheader("View Incidents")
if st.button("Load Incidents"):
    df = get_all_incidents(conn)
    st.dataframe(df)

st.subheader("Add Test Incident")
if st.button("Insert Test Incident"):
    new_id = insert_incident(
        conn,
        "2024-02-01",
        "TestType",
        "Medium",
        "Open",
        "Streamlit login test incident",
        st.session_state.username
    )
    st.success(f"Inserted incident ID: {new_id}")