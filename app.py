import streamlit as st
from pages import Dashboard, Datasets, Examples, GoogleTrends, About, \
    Contact  # these are your custom modules for each page

# Set page config
st.set_page_config(
    page_title="AI Topic Explorer",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://streamlit.io',
        'About': "# This is an *extremely* cool app!"
    })

# Define your pages here
PAGES = {
    "Home": Dashboard,
    "Data Analysis": Datasets,
    "GoogleTrends": GoogleTrends,
    "Examples": Examples,
    "About": About,
    "Contact": Contact
}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()
