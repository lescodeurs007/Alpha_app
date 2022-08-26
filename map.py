import streamlit as st
from databasecreation import *
from streamlit_option_menu import option_menu
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
import folium
from streamlit_folium import folium_static
from streamlit_bokeh_events import streamlit_bokeh_events
from detail_checking import *
placeholder03=st.empty()
def choose_loc():
    global placeholder03
    with placeholder03.container():
        loc_button = Button(label="Get Location",button_type="danger",width=695,height=65)
        loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
        result = streamlit_bokeh_events(loc_button,events="GET_LOCATION",key="get_location",refresh_on_update=False,override_height=75,debounce_time=0)
    if result:
        if "GET_LOCATION" in result:
            #st.write(result.get("GET_LOCATION")["lon"],type(result.get("GET_LOCATION")["lat"]))
            mat=[result.get("GET_LOCATION")["lat"],result.get("GET_LOCATION")["lon"]]
            #curr_loc=[]
            #with st.echo():
            m = folium.Map(location=[mat[0],mat[1]], zoom_start=16)
            tooltip = "You are Here!"
            a=folium.Marker([mat[0],mat[1]], popup="You are Here!",draggable=True,tooltip=tooltip).add_to(m)
            folium_static(m)
            if st.button("Submit"):
                insertlocation(st.session_state.username1,a.location[0],a.location[1])
                st.session_state["loc"]=True
                #database connection
                #st.write(a.location)


# def choose_category(loc):
#     global placeholder03
#     st.write(loc)
#     with placeholder03.container():
#         st.write("Reached Category")
 
