import streamlit as st
import os
from  PIL import Image
from detail_checking import *
base="Menu program"
def select_items():
#empty lists
    fruits=[]
    vegetables=[]
    snacks=[]
    juices=[]
    #multiselect widget
    ch= st.multiselect('What is your choice',['fruits', 'vegetables','snacks','juices'])
    #submit button
    # if st.button('SUBMIT'):
    if ch:
        #if fruits
        if 'fruits' in ch:
            st.write("FRUITS")
            for i in ['apple', 'Bananas', 'cherries', 'chestnut', 'coconut', 'dates', 'grape_pear_mandarine', 'huckleberry', 'kachi', 'kiwi', 'limes', 'lychee', 'mango', 'pear', 'physalis', 'plums_pears', 'pomegranate', 'raspberries', 'salak', 'strawberries', 'tangelo']:
                agree = st.checkbox(i)
                if agree:
                    fruits.append(i)
        #if vegetables
        if 'vegetables' in ch:
            st.write("VEGETABLES")
            for j in ['beetroot', 'brinjal', 'brocoli rabi', 'capsicum', 'corn', 'cucumber', 'garlic', 'ginger', 'Image_4', 'lettuce', 'onions', 'peas', 'potato', 'pumkin', 'radish', 'soy beans', 'spinach', 'sweet potato', 'tomato', 'turnip']:
                agree1= st.checkbox(j)
                if agree1:
                    vegetables.append(j)
        #if snacks
        if 'snacks' in ch:
            st.write("SNACKS")
            for k in ['adhirasam', 'anarsa', 'bhel puri', 'dhai puri', 'kaalan', 'masala puri', 'pani puri', 'vada pav']:
                agree2= st.checkbox(k)
                if agree2:
                    snacks.append(k)
        #if juices
        if 'juices' in ch:
            st.write("JUICES")
            for m in ['cocount water', 'coffee', 'lemon juice', 'tea']:
                agree3= st.checkbox(m)
                if agree3:
                    juices.append(m)

    passing_value={"fruits":fruits,"vegetables":vegetables,"snacks":snacks,"juices":juices}
    print(passing_value)
    if st.button("Submit"):
        #inserting items into database
        insertitems(st.session_state["username1"],passing_value)
        st.success("Items updated")

                

    
                 

