import streamlit as st
import pandas as pd
import numpy as np
import time

# Set page config
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://streamlit.io',
        'About': "# This is an *extremely* cool app!"
    })


# Page header - with Markdown syntax inside a multiline command
"""
# Dashboard
"""