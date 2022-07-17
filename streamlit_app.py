import streamlit
import pandas
import requests

streamlit.title('My Parents\' New Healthy Diner')

streamlit.header('\N{bowl with spoon} Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🍓 Avocado Toast')

streamlit.header('🍉 Build ur Own Fruit Smoothie 🍎')

fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list=fruit_list.set_index('Fruit')

#multi select for the user to pick their fruits
fruits_selected=streamlit.multiselect("Pick ur Fruits",list(fruit_list.index),['Apple','Banana'])
fruits_show=fruit_list.loc[fruits_selected]
#streamlit.multiselect("Pick ur Fruits",list(fruit_list.Fruit))
streamlit.dataframe(fruits_show)

fruity_vice _response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruity_vice_response)
