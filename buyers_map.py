import streamlit as st
import mysql.connector as sqltor
from streamlit_folium import folium_static
#from folium.features import ClickForLatLng, ClickForMarker, LatLngPopup
from folium.plugins import LocateControl
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
import folium
from streamlit_folium import folium_static
from streamlit_bokeh_events import streamlit_bokeh_events
import folium
from databasecreation import *
from details_checking import *
magicEnabled=False

def get_latlng(cat):
    ret = []
    data = getdata_map()
    print(data)
    for i in data:
        for j in cat:
            try:
                if (j in i[3]):
                    name = i[-1]
                    ret.append([str(name), float(i[1]), float(i[2])])
            except TypeError:
                pass
    return ret

def check(arr, lat, lng, acc=0.1):
    ret = []
    for i in arr:
        t_lat = i[1]
        t_lng = i[2]
        if (t_lat < lat + acc and t_lat > lat - acc and t_lng < lng + acc and t_lng > lng - acc):
            #st.write(i)
            ret.append([i[0],float(t_lat), float(t_lng)])
    return ret

    #print(data)


def start1():
    st.title("Search For shops")
    arg = """
    navigator.geolocation.getCurrentPosition(
    (loc) => {
        document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
    }
    )
    """
    arr = ['fruits', 'vegetables','juices','snacks']
    choice = st.multiselect("Choose shops", arr)
    #st.title("Choose Your Location :")
    loc_button = Button(label="Get Shops",button_type="danger",width=695,height=65)
    loc_button.js_on_event("button_click", CustomJS(code=arg))
    result = streamlit_bokeh_events(
        loc_button,
        events="GET_LOCATION",
        key="get_location",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0)
    #hi

    if result:
        if "GET_LOCATION" in result:
            mat = [result.get("GET_LOCATION")["lat"], result.get("GET_LOCATION")["lon"]]

            lat=mat[0]
            lng=mat[1]

            #st.write(st.session_state)
            cursor.execute("")

            x = (get_latlng(choice))
            #st.write(mat)
            # lng=76.9245683
            # lat=10.9271637
            ret=check(x, lat, lng)
            #st.write(ret)
            names=set([str(i[0]) for i in ret])
            names=list(names)
            if(ret==[]):
                st.write("NO shops found")
            else:

                inp=st.selectbox("Choose shop",names)
                for i in ret:
                    if(inp==i[0]):
                        break
                #st.write(i)
                m=folium.Map(location=[i[1],i[2]],zoom_start=12)
                folium.Marker(location=[i[1],i[2]],popup=i[0]).add_to(m)
                #LocateControl().add_to(m)
                folium_static(m)

