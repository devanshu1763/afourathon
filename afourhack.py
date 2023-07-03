import streamlit as st
import pandas as pd
import os
import pyrebase
def is_valid_email(email):
    # Basic email validation using a regular expression
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
def is_valid_phone_number(phone_number):
    # Basic phone number validation using a regular expression
    import re
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, phone_number) is not None



st.write(" ")
st.title("welcome to our model")
from streamlit_option_menu import option_menu
with st.sidebar:

   choice=option_menu (
     menu_title="Main menu",
     options=['Home','ADD STUDENT','UPDATE STUDENT','DELETE A STUDENT'],
     
     default_index=0,
     
     

)
firebaseConfig = {
  'apiKey': "AIzaSyBhOxGsRXOUt6lV9O_DpgnsaUgmc5_m2L8",
  'authDomain': "studentdata-905ac.firebaseapp.com",
  'databaseURL': "https://studentdata-905ac-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "studentdata-905ac",
  'storageBucket': "studentdata-905ac.appspot.com",
  'messagingSenderId': "26763425067",
  'appId': "1:26763425067:web:fcba76845a919a5995c16e",
  'measurementId': "G-ZNPNF69DRN"


}
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
import requests


db = firebase.database()
storage=firebase.storage()
if choice=="ADD STUDENT":
     name =st.text_input("enter student name")
     student_id=st.text_input("enter student id")
     student_email =st.text_input("enter student email id")
     if student_email:
        if is_valid_email(student_email):
              st.write("") 
        else:
            st.error("Invalid email address")

     phone_number=st.text_input("enter student phone number")
     if phone_number:
        if is_valid_phone_number(phone_number):
           st.write("") 
        else:
            st.error("Invalid phone number")
     st.write(" ")
     st.write(" ")
     if st.button("submit"):
       import requests
       databaseURL= "https://studentdata-905ac-default-rtdb.europe-west1.firebasedatabase.app"
       user=auth.create_user_with_email_and_password(student_email,student_id)
       data = {
    "name": name,
     "id": student_id,
    "email": student_email,
    "phone" :phone_number
}

# Send a POST request to add the data to the database
       response = requests.post(databaseURL + "/users.json", json=data)
import json 
ctr=0    
if choice=="UPDATE STUDENT":
   databaseURL= "https://studentdata-905ac-default-rtdb.europe-west1.firebasedatabase.app"
   student_email =st.text_input("enter student email id")
   student_id=st.text_input("enter student id")
  
   if st.button("login ") or ctr==1:
       user=auth.sign_in_with_email_and_password(student_email,student_id)
       ctr=1

# Define the URL of the Firebase Authentication API
      

# Define your Firebase project API key
    
# Get user credentials
      
# Create the request payload
      

# Set the API key as a query parameter
    

# Send the POST request
       user_node_url = f'{databaseURL}/users.json?orderBy="email"&equalTo="{student_email}"'
       response = requests.get(user_node_url)

# Check the response status code
       
    # Retrieve the authentication data from the response
       data = response.json()
    # Access the authenticated user's data or perform other actions
       
       
      
       for key, user_data in data.items():
          id=user_data["id"]
          email = user_data["email"]
          name = user_data["name"]
          phone = user_data["phone"]
       st.write("STUDENT EMAIL :",email)
       st.write(" STUDENT ID : ", id)
       st.write("STUDENT NAME:", name)
       st.write(" STUDENT PHONE NUMBER :", phone)
   
   name1 =st.text_input("enter student new name")
     
   phone_number1=st.text_input("enter student new phone number")
   if phone_number1:
     if is_valid_phone_number(phone_number1):
           st.write("") 
     else:
            st.error("Invalid phone number")
     st.write(" ")
       
   if st.button("submit"):
           data = {
    "name": name1,
     "id": student_id,
    "email": student_email,
    "phone" :phone_number1
}             
           response = requests.post(databaseURL + "/users.json", json=data)
      


     
if choice=="DELETE A STUDENT":
     student_id=st.text_input("enter student id")
    

  

    