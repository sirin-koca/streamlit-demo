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

# Start page load
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'...and now we\'re done!'

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# Page header - with Markdown syntax inside a multiline command
"""
# DataViz Examples
"""

# Create columns in main
col1, col2, col3 = st.columns(3)

col1.button('About', key='About')
col2.button('Contact', key='Contact')
col3.button('Help', key='Help')

with col1:
    # Pandas df
    st.write("My first attempt at using data to create a table:")
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
        'third column': [5, 6, 7, 8]
    })
    df
    ###########
    # st.write("My first attempt at using data to create a table:")
    # st.write(pd.DataFrame({
    #     'first column': [1, 2, 3, 4],
    #     'second column': [10, 20, 30, 40],
    #     'third column': [5, 6, 7, 8]
    # }))

with col2:
    # Create a random table/df
    dataframe = np.random.randn(5, 5)
    st.dataframe(dataframe)

with col3:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# Create a random area-chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

# Another random area-chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

st.area_chart(
    chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]
)
