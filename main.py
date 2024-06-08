import streamlit as st
from streamlit_modal import Modal
import datetime
import pandas as pd
def rotate_string(oriStr):
    y,m,d=oriStr.split("-")
    newStr = d+"-"+m+"-"+y
    return(newStr)
# name = ""
st.set_page_config(
    page_title="Self-Control",
    page_icon="logo.png",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.image("logo.png",width=200)
modal = Modal(key="Demo Key",title="**Challenge Result**")
def add_count(dt):
    t_date = rotate_string(str(datetime.date.today()))
    # t_date = "26-06-2024"
    i = 0
    data = pd.read_csv(dt)
    for i in range(len(data)):
        if t_date == data.at[i, data.columns[0]]:
            data.at[i,data.columns[1]] = data.at[i,data.columns[1]]+1
            # print((data.at[0, data.columns[1]]))
            data.to_csv(dt, index=False)
            break
def today_count(dt):
    t_date = rotate_string(str(datetime.date.today()))
    # t_date = "26-06-2024"
    i=0
    t_count = 0
    data = pd.read_csv(dt)
    for i in range(len(data)):
        if t_date == data.at[i, data.columns[0]]:
            t_count = int(data.at[i, data.columns[1]])
            break
    return t_count
def calc_percent(dt):
    t_date = rotate_string(str(datetime.date.today()))
    # t_date = "26-06-2024"
    data = pd.read_csv(dt)
    i=0
    count_day=0
    count_t = 0
    for i in range(len(data)):
        if t_date == data.at[i, data.columns[0]]:
            break
        if data.at[i, data.columns[1]] != 0:
            count_t += 1
        count_day += 1
        # Calculate the percentage
    if count_day == 0:
        return 0
    else:
        perc = (count_t / count_day) * 100
        return perc
# print(calc_percent("harsh.csv"))
passw = ""

st.write("# Self Control :santa:")
st.write("## Enter password ")
passw = st.text_input(label="**Enter password**")
st.button(label = "Submit")
# st.write(passw)
if passw == st.secrets["pass_arun"]:
    with modal.container():
        perc = round(calc_percent("arun.csv"),2)
        if perc == 0:
            emoji = ":face_vomiting:"
        elif perc>0 and perc<10:
            emoji = ":nauseated_face:"
        elif perc>=10 and perc<20:
            emoji = ":cry:"
        elif perc>=20 and perc<30:
            emoji = ":worried:"
        elif perc>=30 and perc<40:
            emoji = ":cry:"
        elif perc>=40 and perc<50:
            emoji = ":angry:"
        elif perc>=50 and perc<60:
            emoji = ":mechanical_arm:"
        elif perc>=60 and perc<70:
            emoji = ":smile:"
        elif perc>70 and perc<80:
            emoji = ":innocent:"
        elif perc>=80 and perc<90:
            emoji = ":satisfied:"
        elif perc>=90 and perc<100:
            emoji = ":sunglasses:"
        else:
            emoji = ":star-struck:"
        st.write("Percentage : "+str(100-perc)+"%  "+emoji)
        st.write("today's count : "+str(today_count("arun.csv")))
        ar_press = st.button(label = "**Add**",key="arun")
        if ar_press:
            add_count('arun.csv')
elif passw ==st.secrets["pass_harsh"]:
    with modal.container():
        perc = round(calc_percent("harsh.csv"), 2)
        if perc == 0:
            emoji = ":face_vomiting:"
        elif perc > 0 and perc < 10:
            emoji = ":nauseated_face:"
        elif perc >= 10 and perc < 20:
            emoji = ":cry:"
        elif perc >= 20 and perc < 30:
            emoji = ":worried:"
        elif perc >= 30 and perc < 40:
            emoji = ":cry:"
        elif perc >= 40 and perc < 50:
            emoji = ":angry:"
        elif perc >= 50 and perc < 60:
            emoji = ":mechanical_arm:"
        elif perc >= 60 and perc < 70:
            emoji = ":smile:"
        elif perc > 70 and perc < 80:
            emoji = ":innocent:"
        elif perc >= 80 and perc < 90:
            emoji = ":satisfied:"
        elif perc >= 90 and perc < 100:
            emoji = ":sunglasses:"
        else:
            emoji = ":star-struck:"
        st.write("Percentage : "+str(perc)+"%"+emoji)
        st.write("today's count : " + str(today_count("harsh.csv")))
        hs_press = st.button(label="**Add**",key = "harsh")
        if hs_press:
            add_count('harsh.csv')
elif passw == "":
    st.write("")
else :
    st.write("Wrong password")
