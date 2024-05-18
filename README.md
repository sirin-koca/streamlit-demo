Yes, I understand. Let's present the information in a more academic and diplomatic style.

### Lessons Learned
Throughout the course of this project, we encountered several significant challenges that provided valuable learning experiences. One major challenge was handling the large dataset, which included around 9,000 records in the AI topic list. This caused performance issues, particularly with the sunburst chart visualization. From this, we learned the importance of optimizing data handling and considering performance implications early in the development process.

Another key lesson was managing the dual role of our supervisor, who acted as both client and internal guide. While this offered unique insights and expectations from a client perspective, it sometimes left us needing more direct technical support. This experience underscored the necessity for clear communication and effective expectation management in future projects.

Moreover, our project emphasized the value of strong collaboration and efficient time management within the team. Regular check-ins and clear task delegation were crucial in meeting our tight deadlines and ensuring the project's progress.

### Technical Testing Roadmap
Given the streamlined nature of our application, a focused approach to testing is essential:
- **Functionality Testing**: This involves ensuring that all features, such as topic search, paper search, and the hierarchical topic tree, perform as intended without any issues.
- **Performance Testing**: Special attention should be given to features handling large datasets, like the sunburst chart. We recommend using tools such as JMeter to simulate high load conditions and identify performance bottlenecks.
- **Usability Testing**: It is crucial to ensure that the application is user-friendly. This involves refining the user interface based on feedback from our user testing questionnaire to enhance the overall user experience.

### Future Scalability
To ensure the future scalability of the application:
- **Database Optimization**: Implement indexing and optimize queries to handle large datasets more efficiently.
- **Cloud Infrastructure**: Consider migrating to a cloud platform, such as AWS or Google Cloud, to leverage scalable resources and ensure the application can handle increased loads.
- **Modular Design**: Structure the application in a modular manner, allowing for the easy addition of new features and datasets without extensive rework.
- **User Management**: Plan for enhanced user role management to accommodate future user expansion and varying access levels.
- **Continuous Deployment**: Set up Continuous Integration and Continuous Deployment (CI/CD) pipelines to facilitate smooth and efficient updates and deployments.

### User Manual
The user manual should provide clear and concise instructions to ensure users can easily install, run, and utilize the application:
- **Installation Instructions**:
  1. Install necessary dependencies using `pip install -r requirements.txt`.
  2. Set up the database by running the provided SQL scripts.
- **Running the Application**:
  1. Navigate to the application directory.
  2. Start the application with `streamlit run Home.py`.
- **Using the Features**:
  - **Topic Search**: Detailed instructions on how to search for AI topics within the application.
  - **Paper Search**: Guidance on searching for academic papers using various criteria.
  - **Sunburst Chart**: Explanation of how to navigate and interpret the hierarchical topic tree visualization.
- **Troubleshooting**:
  - Common issues (e.g., performance slowdowns) and their solutions.
  - Contact information for further support and assistance.

These sections should be refined and incorporated into the final report, ensuring they are presented in an academic and professional manner. Let me know if there's a specific section you would like to start with or need further refinement.




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
