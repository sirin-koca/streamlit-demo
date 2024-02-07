import streamlit as st
from datetime import date, timedelta
import streamlit.components.v1 as components

# Example list of AI topics
ai_topics = ['AI',
             'AI Ethics',
             'AI in Education',
             'AI in Finance',
             'AI in Healthcare',
             'Artificial General Intelligence',
             'Artificial Intelligence',
             'Autonomous Vehicles',
             'Computer Vision',
             'Deep Learning',
             'Face Recognition',
             'Generative Artificial Intelligence',
             'Knowledge Graphs',
             'Large Language Models',
             'Machine Learning',
             'Natural Language Processing',
             'Neural Network',
             'Reinforcement Learning',
             'Responsible AI',
             'Robotics',
             'Speech Recognition',
             'Super Intelligence']

# Example list of countries with ISO country codes - which Google uses
country_codes = {
    'Argentina': 'AR',
    'Canada': 'CA',
    'China': 'CN',
    'Croatia': 'HR',
    'England': 'GB',  # Using Great Britain's code for England
    'France': 'FR',
    'Germany': 'DE',
    'Greece': 'GR',
    'India': 'IN',
    'Ireland': 'IE',
    'Italy': 'IT',
    'Japan': 'JP',
    'Mexico': 'MX',
    'Nigeria': 'NG',
    'Poland': 'PL',
    'Portugal': 'PT',
    'Russia': 'RU',
    'Slovenia': 'SI',
    'Spain': 'ES',
    'Turkiye': 'TR',  # Correct ISO code for Turkey
    'UK': 'GB',
    'USA': 'US'}

# User selects a topic from the dropdown
selected_topic = st.selectbox('Select a Topic:', ai_topics)

# Sort countries alphabetically for display
sorted_countries = sorted(country_codes.keys())
selected_country = st.selectbox('Select a Country:', sorted_countries)

# Set default date range to the last year
default_start_date = date.today() - timedelta(days=365)
default_end_date = date.today()

# User selects a date range
start_date = st.date_input('Start date', default_start_date, min_value=date(2000, 1, 1), max_value=date.today())
end_date = st.date_input('End date', default_end_date, min_value=date(2000, 1, 1), max_value=date.today())

# Error handling for invalid date range selection
if start_date > end_date:
    st.error('Error: End date must be after the start date.')
else:
    st.text(' * Please select variables from the list above')


# Function 1
def generate_time_analysis_embed_code(topic: str, country: str, start_date: date, end_date: date) -> str:
    """
    Generates the HTML embed code for a Google Trends widget based on the provided parameters.

    Parameters:
    - topic (str): The selected AI topic.
    - country (str): The selected country, converted to its ISO 3166-1 alpha-2 code.
    - start_date (date): The start date for the trend analysis.
    - end_date (date): The end date for the trend analysis.

    Returns:
    - str: The HTML embed code for the Google Trends widget.
    """
    country_code = country_codes.get(country, 'US')  # Default to 'US' if not found
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    # Handle the URL encoding if it contains spaces or special characters
    encoded_topic = topic.replace(' ', '%20')

    # Note: We should check if the deployment environment supports this.
    embed_code = f"""
    <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3620_RC01/embed_loader.js"></script>
    <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", 
    {{"comparisonItem":[{{"keyword":"{encoded_topic}", "geo":"{country_code}", "time":"{start_date_str} {end_date_str}"}}],
    "category":0, "property":""}}, {{"exploreQuery":"date={start_date_str}%20{end_date_str}&geo={country_code}&q={encoded_topic}",
    "guestPath":"https://trends.google.com:443/trends/embed/"}}); </script>"""
    return embed_code


# It may be better to use a dynamic height based on dynamic content
default_height = 600
dynamic_height = default_height + len(ai_topics) * 2  # Example adjustment

if start_date and end_date:
    google_trends_embed_code = generate_time_analysis_embed_code(selected_topic, selected_country, start_date, end_date)
    components.html(google_trends_embed_code, height=dynamic_height)


# Function 2
def generate_related_topics_embed_code(topic, country, start_date, end_date):
    """
    Generates the HTML embed code for a Google Trends 'related topics' widget based on the provided parameters.

    Parameters:
    - topic (str): The selected AI topic.
    - country (str): The selected country, converted to its ISO 3166-1 alpha-2 code.
    - start_date (date): The start date for the trend analysis.
    - end_date (date): The end date for the trend analysis.

    Returns:
    - str: The HTML embed code for the Google Trends 'related topics' widget.
    :param start_date:
    :param end_date:
    """
    country_code = country_codes.get(country, 'US')  # Default to 'US' if not found
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    # Handle the URL encoding if it contains spaces or special characters
    encoded_topic = topic.replace(' ', '%20')

    embed_code = f"""
    <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3620_RC01/embed_loader.js"></script>
    <script type="text/javascript"> trends.embed.renderExploreWidget("RELATED_QUERIES", 
    {{"comparisonItem":[{{"keyword":"{encoded_topic}", "geo":"{country_code}", 
    "time":"{start_date_str} {end_date_str}"}}],"category":0, "property":""}}, 
    {{"exploreQuery":"date={start_date_str}%20{end_date_str}&geo={country_code}&q={encoded_topic}&hl=no",
    "guestPath":"https://trends.google.com:443/trends/embed/"}}); </script>
    """
    return embed_code


# Generate and display the embed code for the 'related topics' chart
if start_date and end_date:
    related_topics_embed_code = (
        generate_related_topics_embed_code(selected_topic, selected_country, start_date, end_date))
    components.html(related_topics_embed_code, height=600)  # You may need to adjust the height
