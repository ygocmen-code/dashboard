#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Contents of ~/my_app/streamlit_app.py

import streamlit as st
import pymssql as pymssql
import pandas as pd
import datetime
import datetime as dt
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from bokeh.plotting import figure

import streamlit as st
#import pyodbc




#[db_credentials]

# Verbose version

import streamlit as st

#DB Connect



conn = pymssql.connect(**st.secrets.db_config)

query="""SELECT k.Yil , k.Ay, k.Gun, k.BolgeId, k.BrutGelirTL , k.NetGelirTL, k.ToplamCezaTL, k.ToplamIndirimTL, k.SurusBasinaNetGelirTL,
       k.ScooterBasinaNetGelirTL, k.SurusKariEksiAmortismanTL, k.SurusKariArtiAmortismanTL, k.ScooterBasinaGunlukCiro,
       k.ScooterBasinaGunlukCiroOrt, k.ScooterBasinaHaftalikCiro, k.ScooterBasinaHaftalikCiroOrt, k.ScooterBasinaAylikCiro,
       k.ScooterBasinaAylikCiroOrt,k.ToplamScooterSayisi, k.SurusSayisi , k.SurucuSayisi, k.SurucuBasinaSurusSayisi, k.SurucuBasinaMesafeKM,
       k.ScooterBasinaMesafeKM , k.SurucuBasinaSureDakika,bolge.BolgeAcilisTarihi, bolge.BolgeAdi, k.ScooterBasinaSureDakika , k.ToplamSureDakika, k.SurucuBasinaNetGelirTL,
       k.KayitTarihi FROM tKPIData k INNER JOIN tBolgeler bolge ON k.BolgeId = bolge.KayitId"""


datab = pd.read_sql_query(sql=query,con=conn)

st.set_page_config(
    page_title = "Growth KPI",
    layout = "wide")



datab = pd.read_sql_query(sql=query,con=conn)

#data["fark"] = (data["verisetinin_oluşturulma_tarihi"]- data["KayitTarihi"]).dt.days

import plotly.express as px
import plotly.graph_objects as go


import plotly.express as px
import plotly.graph_objects as go
import re
import PIL

from PIL import Image
img= Image.open('binbindaire.png')
st.image(img)


def plot():
    
    datab = pd.read_sql_query(sql=query,con=conn)
    
    clist = datab["BolgeAdi"].unique().tolist()
    
    cities = st.multiselect("Select city", clist)
    
    st.header("Number of Rides {}".format(", ".join(cities)))

    dfs = {city: datab[datab["BolgeAdi"] == city] for city in cities}

    fig = go.Figure()
    
    for city, datab in dfs.items():
        
        fig = fig.add_trace(go.Scatter(x=datab["Ay"], y=datab["SurusSayisi"], name=city))

    st.plotly_chart(fig)
    
plot()



#st.title("Metrics")

#metric =st.multiselect("Select metric.",["GR","NOM", "TYYTD", "LYYTD", "LYGR","Weekly", "Monthly", "Annual"])
#st.header("Metrik seçiniz.")

#st.title("KPIs")

#metric_two =st.multiselect("Select KPIs metric.", ["Ridership", "Rides", "Riders" ]) 

def main_page():
    st.markdown("# BinBin Growth KPI")
    #st.sidebar.markdown("# BinBin Growth KPI")

def page2():
    st.markdown("# Usage")
    st.sidebar.markdown("# Usage")
    st.area_chart(data=datab["SurusSayisi"], width=0, height=0, use_container_width=True)
    st.line_chart(datab["SurucuSayisi"])
    #st.bar_chart(datab["SurusSayisi"])

def page3():
    st.markdown("# Revenue ")
    st.sidebar.markdown("# Revenue")



page_names_to_funcs = {
    "Home": main_page,
    "Usage": page2,
    "Revenue":page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


st.title("KPI: Rides")


st.subheader("Number of Rides Per Year")
st.write(datab.pivot_table('SurusSayisi', ['Yil'], aggfunc='sum').reset_index())
#st.subheader("Number of Rides Per Mounth")
#st.write(datab.pivot_table('SurusSayisi', ['Ay'], aggfunc='sum').reset_index())
#st.subheader("Number of Rides Per Days")
#st.write(datab.pivot_table('SurusSayisi', ['Gun'], aggfunc='sum').reset_index())
#Bar Chart

st.subheader("Number of Rides Monthly")

from bokeh.plotting import figure

y = datab["SurusSayisi"]

x = datab["Ay"]

p = figure(
     title='Number of Rides Per Month',
     y_axis_label='Number of Rides',
     x_axis_label='Month')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

#Line Chart

#st.line_chart(datab["SurucuSayisi"])

import matplotlib.pyplot as plt
import seaborn as sns

st.subheader("Number of Rider Per Month")

fig , ax = plt.subplots()

sns.scatterplot(data = datab,x="SurucuSayisi", y = "Ay", ax = ax)
st.pyplot(fig)

#st.title("Growth KPI Dashboard : Rider")

#st.subheader("Rider")



#st.markdown("## Key Metrics")
