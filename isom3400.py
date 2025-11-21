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
tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
with tab1:
    st.write("### Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")

with tab2:
    st.write("### Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for i, feedback in enumerate(customer_feedback, 1):
        st.write(f"{i}. {feedback}")

with tab3:
    st.write("### Market Trends")
    st.bar_chart({"Revenue (in M$)": [1.2, 1.5, 1.3, 1.6]}, height=200)

# 4. Expander
# TODO: Add expander for additional info

# 5. Interactivity
# TODO: Add selectbox and slider for revenue adjustment

# 6. Bonus
# TODO: Add bar chart and motivational button
