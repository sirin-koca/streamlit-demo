import streamlit as st
import pandas as pd
import numpy as np

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
# Examples
"""
# Create columns in main
col1, col2, col3 = st.columns(3)

col1.button('Example 1', key='Col1')
col2.button('Example 2', key='Col2')
col3.button('Example 3', key='Col3')

with col1:
    # Pandas df
    st.write("Create a table:")
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
        'third column': [5, 6, 7, 8]
    })
    df

with col2:
    # Create a random table/df
    dataframe = np.random.randn(5, 5)
    st.dataframe(dataframe)

with col3:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
