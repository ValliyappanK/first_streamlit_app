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

#function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
  #normalizing json text
  fruityvice_normalize=pandas.json_normalize(fruityvice_response.json())
  #print as a table
  return fruityvice_normalize
  
#new section for Fruity Vice
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice=streamlit.text_input('What fruit would you like to know about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    value_from_function=get_fruityvice_data(fruit_choice)
    #print as a table
    streamlit.dataframe(value_from_function)
  
except URLError as e:
  streamlit.error()
  
streamlit.header("The fruit load list contains:")
#snowflake functions:
def get_fruit_load_list():
  with my_cnx.cursor() as my_crsr:
    my_crsr.execute("select * from fruit_load_list")
    return my_crsr.fetchall()

#add a button and def for fruit load list:
if streamlit.button('Get fruit load list'):
  my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data=get_fruit_load_list()
  streamlit.dataframe(my_data)
  
streamlit.stop()  
usr_fruit=streamlit.text_input('What fruit would you like to add in this list?')
streamlit.write('The user entered',usr_fruit)
my_crsr.execute("insert into fruit_load_list values ('from streamlit')")
