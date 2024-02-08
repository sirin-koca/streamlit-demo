import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title('Dashboard')
    st.write('This is the Dashboard page.')


# Create columns in main
col1, col2 = st.columns(2)

col1.button('About', key='About')
col2.button('Contact', key='Contact')

with col1:
    # Create a random area-chart
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

with col2:
    # Another random area-chart
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

    st.area_chart(
        chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]
    )
