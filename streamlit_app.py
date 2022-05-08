import streamlit
import pandas

streamlit.title('My Parents\' New Healthy Diner')

streamlit.header('\N{bowl with spoon} Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🍓 Avocado Toast')

streamlit.header('🍉 Build ur Own Fruit Smoothie 🍎')

fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruit_list)
