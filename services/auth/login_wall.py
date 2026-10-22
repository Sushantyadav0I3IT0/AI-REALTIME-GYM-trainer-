import streamlit as st
from services.persistence.exercise_repository import get_or_create_user


def render_login_wall():

    user_id = st.session_state.get("user_id")
    if isinstance(user_id, int):
        return True

    username = st.session_state.get("username", "").strip()
    if user_id is not None and username:
        user = get_or_create_user(username)
        st.session_state["user_id"] = user["id"]
        return True

    st.title("🏋️‍♂️ AI Real-time GYM Trainer")
    st.markdown("### Welcome! Please enter a username to start.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "Name(unique)",
            placeholder="unique name e.g. princekhunt"
        )

        submit_button = st.form_submit_button(
            "Start Session",
            width="stretch"
        )

    if submit_button:

        username = username.strip()
        if not username:
            st.error("Name cannot be empty")
            return False

        st.session_state["username"] = username
        user = get_or_create_user(username)
        st.session_state["user_id"] = user["id"]

        st.rerun()

    return False