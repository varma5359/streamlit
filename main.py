import streamlit as st

st.title("My Streamlit App")
st.write("Welcome to my Streamlit application! This is a simple example of how to use Streamlit to create interactive web applications with Python.")
st.header("Features")
st.markdown("- Easy to use and deploy")
st.markdown("You can use various widgets like sliders, buttons, and text inputs to make your app interactive.")
st.markdown("For example, you can use a slider to select a value:")

st.text_input("Enter your name:", "Type here...")
st.number_input("Select a number:", min_value=0, max_value=100, value=50)
st.slider("Select a value:", min_value=0, max_value=100, value=50)
st.text_area("Enter some text:", "Type here...")

st.button("Click me!")
st.checkbox("Check me!")
st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

st.selectbox("Select an option:", ["Option A", "Option B", "Option C"])
st.multiselect("Select multiple options:", ["Option 1", "Option 2", "Option 3"])



import pandas as pd
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
st.dataframe(df)

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)