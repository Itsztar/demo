import streamlit as st

st.title("Retail Business Dashboard")
st.header("Manager Input Secion")

st.write("Please enter the monthly sales target and select the region.")
sales_target = st.number_input("Enter Monthly Sales Target (in USD):", min_value = 0, value = 50000, step = 1000)
region = st.selectbox("Select Region:", ["North", "South", "East", "West"])

if st.button("Submit"):
    st.header("Summary")
    st.write(f"The Monthly Sales Target is ${sales_target:,.2f}.")
    st.write(f"The Selected Region is {region}.")

    if sales_target > 100000:
        st.write("Great! You have set an ambitious target!")

    st.success("Dashboard updated successfully")
