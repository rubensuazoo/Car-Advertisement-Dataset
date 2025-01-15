import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Car Sales Analysis",
    page_icon="🚗",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

df = load_data()

# Add this after loading the data
st.header('🚗 Used Car Market Analysis')
st.write('Explore trends in the used car market through interactive visualizations')

# Add sidebar filters
st.sidebar.header('Filters')

# Price range filter
price_range = st.sidebar.slider(
    'Select Price Range',
    min_value=int(df['price'].min()),
    max_value=int(df['price'].max()),
    value=(0, 50000)
)

# Filter data based on price range
filtered_df = df[
    (df['price'] >= price_range[0]) & 
    (df['price'] <= price_range[1])
]

# Add this after the filters
# Create two columns for charts
col1, col2 = st.columns(2)

with col1:
    st.subheader('Price Distribution')
    # Histogram with plotly express
    fig_hist = px.histogram(
        filtered_df,
        x='price',
        nbins=50,
        title='Distribution of Car Prices'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.subheader('Price vs Year')
    # Scatter plot with plotly express
    fig_scatter = px.scatter(
        filtered_df,
        x='model_year',
        y='price',
        color='condition',
        title='Car Prices by Year and Condition'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Add checkbox to show additional details
if st.checkbox('Show Vehicle Type Analysis'):
    st.subheader('Price Distribution by Vehicle Type')
    fig_box = px.box(
        filtered_df,
        x='type',
        y='price',
        title='Price Ranges by Vehicle Type'
    )
    st.plotly_chart(fig_box, use_container_width=True)

# Option to show raw data
if st.checkbox('Show Raw Data'):
    st.write(filtered_df)