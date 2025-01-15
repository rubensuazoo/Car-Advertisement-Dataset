# Car Market Analysis Dashboard

## Project Description
An interactive web application for analyzing used car market data. Users can explore car prices, conditions, and other characteristics through interactive visualizations.

## Features
- Interactive price range filtering
- Price distribution histogram
- Price vs Year scatter plot
- Vehicle type analysis (optional view)
- Raw data view option

## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly Express

## Local Setup
1. Clone this repository
2. Create a virtual environment:
   ```python -m venv venv```
3. Activate the virtual environment:
   - Windows: ```venv\Scripts\activate```
   - Unix/MacOS: ```source venv/bin/activate```
4. Install required packages:
   ```pip install -r requirements.txt```
5. Run the application:
   ```streamlit run app.py```

## Usage
- Use the sidebar filters to select price ranges
- Toggle additional visualizations using checkboxes
- Interact with plots (zoom, hover, etc.)