import streamlit as st
import streamlit_authenticator as stauth
import time
from streamlit_option_menu import option_menu
# from streamlit_text_label import label_select
from databasecreation import *
from detail_checking import *
from map import *
from buyers_map import *
from menu import *
k=1
l=1000
def mp():
    st.sidebar.markdown("main page")

def menu():
    #Entering the items
    select_items()

def location():
    st.sidebar.markdown("#location")
    choose_loc()


def buyer():
    # For consumers to identify the the location of shops
    start1()

def login():
    #will be called to login the user

    credentials=logincheck()

    authenticator = stauth.Authenticate(credentials,"sales_dashboard", "123",cookie_expiry_days=0)

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")
    if authentication_status:
        st.session_state.username1=username
        placeholder01.empty()
        placeholder02.empty()
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")

        temp1=checking_lat_long(st.session_state["username1"])
        #st.write(temp1) --> checking value of temp1
        if temp1==1:
            st.session_state["loc"]=True
            page_names_to_funcs = {
                "Main Page": mp,
                "Menu": menu,
            }
        if temp1==0:
            st.session_state["loc"] = False
            page_names_to_funcs = {
                "Main Page": mp,
                "Location": location,
                "Menu": menu,
            }


        selected_page = st.sidebar.selectbox("Select an option", page_names_to_funcs.keys())
        page_names_to_funcs[selected_page]()




def signup():
    #will be called for new user to create account
    st.title("Create New Account:")
    shop_name=st.text_input("Enter Shop Name:")
    full_name=st.text_input("Enter Your Full Name:")
    phone_num=st.text_input("Enter Your Phone Number:")
    password1=st.text_input("Enter Your Password:",type="password")
    password2=st.text_input("Re-enter Your Password:",type="password")
    if st.button("Sign Up"):
        if password1 != password2 :
            st.warning("The passwords do no match")
        if len(str(phone_num))!=10:
            st.warning("Invalid phone number")
        else:
            if signup_check(shop_name, full_name, phone_num, password1)==0:
                st.error("Account already exists go to login page")
            else:
                #inserting data into the database
                st.success("Account successfully created. Go to login menu to login")

def create_page():
    selected2=None
    try:
        if mycon.is_connected():
            pass
        else:
            mycon.close()
            mysqlconnection()
    except:
        mysqlconnection()
    global placeholder01,placeholder02
    placeholder01=st.empty()
    placeholder02=st.empty()
    with placeholder01.container():
        selected=option_menu(
                menu_title="APP NAME",
                # options=["buyers","login","sign up"],
                options=["buyers", "seller"],
                icons=["circle-fill","circle"],
                menu_icon="cast",
                default_index=0,
                orientation="horizontal",
                key=1,

        )


    # the conditions for different buttons
    if selected=="buyers":
        buyer()
    if selected=="seller":
        with placeholder02.container():
            selected2 = option_menu(
                menu_title="Seller",
                options=["login", "sign up"],
                icons=["circle-fill", "circle"],
                menu_icon="cast",
                default_index=0,
                orientation="horizontal",
                key=2,
            )
            st.text("Dummy User Id:\nUser_name:9876543210 password:1111")
        if selected2 == "login":
            login()
        if selected2 == "sign up":
            signup()

create_page() #when this file is called this function will be run first
