import streamlit as st

st.title("Python Data Structure")

st.header("We are creating list")

#Creating a list
fruits=['apple','banana','cherry']
st.write("Original list: ", fruits)

#Adding an item to the list
fruits.append('orange')
st.write("List after adding an item: ", fruits)

#Add an item using text input
new_fruit=st.text_input("Enter fruits name","")
if st.button("Add Fruits"):
    if new_fruit:
        fruits.append(new_fruit)
        st.write(fruits)
