import streamlit as st

# 1. Dashboard Title and Objective
# TODO: Add title and description
st.title("Business Performance Dashboard")
st.write("Objective: Provide insights into revenue, customer feedback, and market trends.")

# 2. Columns Layout
# TODO: Display Q1, Q2, Q3 revenue in columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Q1 2025")
    st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2025")
    st.write("Revenue: $1.5M")
with col3:
    st.header("Q3 2025")
    st.write("Revenue: $1.3M")
    
# 3. Tabs
# TODO: Create tabs for Sales Data, Customer Insights, Market Trends

# 4. Expander
# TODO: Add expander for additional info

# 5. Interactivity
# TODO: Add selectbox and slider for revenue adjustment

# 6. Bonus
# TODO: Add bar chart and motivational button
