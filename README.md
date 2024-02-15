# README 
## Hello Streamlit 

```
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Simple Streamlit App')

# Description
st.write('This is a simple Streamlit app that generates a random time series data and displays a line chart.')

# Generate random data
data = pd.DataFrame({
  'date': pd.date_range(start='1/1/2022', periods=30),
  'value': np.random.randn(30).cumsum()
})

# Plot data
st.line_chart(data.set_index('date'))

# Show data in a table
st.write('Below is the random data generated:', data)

# Simple interaction: Slider
number = st.slider('Choose a number', 0, 100, 50)
st.write('You selected:', number)

```
