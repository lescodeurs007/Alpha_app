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
            for file in os.listdir(base+'\\fruits'):
                if file.endswith(".jpg"):
                    image=Image.open(os.path.join(base+"\\fruits", file))
                    st.image(image,width=100)
                    f=os.path.join(base+"\\fruits", file)
                    agree = st.checkbox(f[86:-4])
                if agree:
                    fruits.append(f[86:-4])
        #if vegetables
        if 'vegetables' in ch:
            st.write("VEGETABLES")
            for file1 in os.listdir(base+'Vegtables'):
                if file1.endswith(".jpg"):
                    image1=Image.open(os.path.join(base+'Vegtables', file1))
                    st.image(image1,width=100)
                    f1=os.path.join(base+'Vegtables', file1)
                    agree1= st.checkbox(f1[89:-4])
                if agree1:
                    vegetables.append(f1[89:-4])
        #if snacks
        if 'snacks' in ch:
            for file2 in os.listdir(base+'snacks'):
                if file2.endswith(".jpg"):
                    image2=Image.open(os.path.join(base+'snacks', file2))
                    st.image(image2,width=100)
                    f2=os.path.join(base+'snacks', file2)
                    agree2= st.checkbox(f2[86:-4])
                if agree2:
                    snacks.append(f2[86:-4])
        #if juices
        if 'juices' in ch:
            for file3 in os.listdir(base+'juices'):
                if file3.endswith(".jpg"):
                    image3=Image.open(os.path.join(base+'juices', file3))
                    st.image(image3,width=100)
                    f3=os.path.join(base+'juices', file3)
                    agree3= st.checkbox(f3[86:-4])
                if agree3:
                    juices.append(f3[86:-4])

    passing_value={"fruits":fruits,"vegetables":vegetables,"snacks":snacks,"juices":juices}
    print(passing_value)
    if st.button("Submit"):
        #inserting items into database
        insertitems(st.session_state["username1"],passing_value)
        st.success("Items updated")

                

    
                 

