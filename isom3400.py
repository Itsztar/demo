import streamlit as st

# Set up the dashboard layout
st.title("Retail Business Dashboard")
st.header("Manager Input Section")

# Q1: Enter monthly sales target
sales_target = st.number_input(
    "Enter Monthly Sales Target (in USD):", 
    min_value=0, 
    value=50000,
    step=1000
)

# Q2: Select region
region = st.selectbox(
    "Select Region:",
    ["North", "South", "East", "West"]
)

# Submit button
if st.button("Submit"):
    # Q4 & Q5: Display summary message and entered values
    st.write("### Summary")
    st.write(f"Sales Target: ${sales_target:,.2f}")
    st.write(f"Selected Region: {region}")
    
    # Q6: Show success message
    st.success("Dashboard updated successfully")
    
    # Challenge Extension: Extra logic for high targets
    if sales_target > 100000:
        st.write("Great! You have set an ambitious target!")
