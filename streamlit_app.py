import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#new section for Fruity Vice
streamlit.header('Fruityvice Fruit Advice')
try:
fruit_choice=streamlit.text_input('What fruit would you like to know about?')
if not fruit_choice:
  streamlit.error("Please select a fruit to get information")
else
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
  #normalizing json text
  fruityvice_normalize=pandas.json_normalize(fruityvice_response.json())
  #print as a table
  streamlit.dataframe(fruityvice_normalize)
  
except URLError as e:
  streamlit.error()
  
streamlit.stop()
my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_crsr=my_cnx.cursor()
my_crsr.execute("select * from fruit_load_list")
my_data_row=my_crsr.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
usr_fruit=streamlit.text_input('What fruit would you like to add in this list?')
streamlit.write('The user entered',usr_fruit)
my_crsr.execute("insert into fruit_load_list values ('from streamlit')")
