import streamlit as st
import matplotlib.pyplot as plt


st.title("Data Visualization")

data={
    "Apple":30,
    "Banana":40,
    "Cheery":45
}

#Display dictionary
st.write(data)

#update dictionary
key=st.text_input("Enter a key","")
value=st.text_input("Enter a value","")
if st.button("Update Dictionary"):
    if key and value:
        data[key]=int(value)
        st.write(data)


#  Plot a bar chart
st.header("Bar chart of fruits inventory")
fig, ax=plt.subplots()
ax.bar(data.keys(),data.values())
ax.set_xlabel("Fruit")
ax.set_ylabel("Quantity")
st.pyplot(fig)
