import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact Me"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.write("Hi, I'm a developer passionate about building awesome projects!")

# About Me Page
elif page == "About Me":
    st.title("About Me")
    st.write("I am a Python developer specializing in building web applications with Streamlit.")

# Projects Page
elif page == "Projects":
    st.title("Projects")
    projects = [
        {"name": "E-Commerce Website", "description": "An online marketplace with payment integration."},
        {"name": "Portfolio Website", "description": "A personal portfolio built with Streamlit."},
        {"name": "Blog Platform", "description": "A blog with user authentication and comments."}
    ]
    for project in projects:
        st.subheader(project["name"])
        st.write(project["description"])

# Contact Page
elif page == "Contact Me":
    st.title("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thank you! Your message has been sent.")
