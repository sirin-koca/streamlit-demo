# import necessary libraries
import streamlit as st
from pages import Dashboard as pd
import plotly.express as px

# Setting the title and layout of the app
st.set_page_config(page_title="AI Research Trends Dashboard", layout="wide")
st.title("AI Research Trends Dashboard")

# Add a sidebar for user input
st.sidebar.markdown("_DEMO "
                    "// Bachelor Thesis_")
st.sidebar.markdown("# AiTrend :. ")
st.sidebar.markdown("# DASHBOARD :.")
st.sidebar.header("User Input")

# Upload CSV file
uploaded_file = st.sidebar.file_uploader("Upload CSV", type="csv")

# Error handling for file upload
if uploaded_file is None:
    st.warning("Please upload a CSV file to proceed.")
    st.stop()
if uploaded_file is not None:
    # Try to read the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

# Display the DataFrame in a tab
# Inject custom CSS with st.markdown
st.markdown("""
    <style>
    /* Add custom styles here */
    .stTabs {
        /* Custom styles for tab buttons */
        font-size: 1.5em;  /* Increase font size */
        font-weight: bold; /* Make font bold */
    }
    </style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Data Overview", "Data Analysis"])

with tab1:
    st.subheader("Uploaded DataFrame")
    st.dataframe(df)

with tab2:
    # Select columns for chart visualization
    st.sidebar.subheader("Visualization Settings")

    # Select type of chart
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line", "Bar", "Area", "Scatter"])

    # Filter columns based on data type
    if chart_type in ["Line", "Area", "Scatter"]:
        valid_columns = df.select_dtypes(include=['float', 'int']).columns
    else:  # For bar chart, categorical data can be used
        valid_columns = df.columns

    selected_columns = st.sidebar.multiselect("Select Columns for Chart", valid_columns)

    # Select X-axis column
    x_axis_column = st.sidebar.selectbox("Select X-axis Column", valid_columns)

    # Check if any columns are selected
    if selected_columns:
        st.subheader("Chart Visualization")

        # Create a chart using Plotly
        if chart_type == "Line":
            fig = px.line(df, x=x_axis_column, y=selected_columns)
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_axis_column, y=selected_columns)
        elif chart_type == "Area":
            fig = px.area(df, x=x_axis_column, y=selected_columns)
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_axis_column, y=selected_columns)

        # Display the chart
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Select columns to visualize data.")
