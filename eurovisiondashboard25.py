# -*- coding: utf-8 -*-
#Packages
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st

#Countries
Countries = ['Switzerland',
          'Albania',
          'Armenia',
          'Australia',
          'Austria',
          'Azerbaijan',
          'Belgium',
          'Croatia',
          'Czechia',
          'Cyprus',
          'Denmark',
          'Estonia',
          'Finland',
          'France',
          'Georgia',
          'Germany',
          'Greece',
          'Iceland',
          'Ireland',
          'Israel',
          'Italy',
          'Latvia',
          'Lithuania',
          'Luxembourg',
          'Malta',
          'Montenegro',
          'Netherlands',
          'Norway',
          'Poland',
          'Portugal',
          'San Marino',
          'Serbia',
          'Slovenia',
          'Spain',
          'Sweden',
          'Ukraine',
          'United Kingdom'
          ]

semi1 = ['Iceland','Poland','Slovenia','Estonia','Ukraine','Sweden',
           'Portugal','Norway','Belgium','Azerbaijan','San Marino','Albania',
           'Netherlands','Croatia','Cyprus']
semi2 = ['Australia','Montenegro','Ireland','Latvia','Armenia','Austria','Greece',
           'Lithuania','Malta','Georgia','Denmark','Czechia','Luxembourg','Israel',
           'Serbia','Finland']
finalists = ['Switzerland','France','Germany','Italy','Spain','United Kingdom']

ev25_data = {'country':Countries,'semi':[],
             "available":[True for i in Countries],
            "text":["" for i in Countries]}
for i in Countries:
    if i in finalists:
        ev25_data['semi'].append(3)
    elif i in semi1:
        ev25_data['semi'].append(1)
    elif i in semi2:
        ev25_data['semi'].append(2)
    else:
      print(i,"was missed")
EV25 = pd.DataFrame(ev25_data)

#Add Changes here
guest_list = {'country':[],'name':[]}
def select_country(country,name):
          EV25.loc[EV25['country'] == country,'text'] = name
          EV25.loc[EV25['country'] == country,'available'] = False
          guest_list['country'].append(country)
          guest_list['name'].append(name)
          
select_country("Estonia","Victor")
select_country("Australia","Alizée")
select_country("Iceland","John")
select_country("Netherlands","Salomon")
select_country("Ireland","Paolo")
select_country("France","Hazal")
select_country("Spain","Gulce")
select_country("Lithuania","Thomas")


fig = px.choropleth(EV25[EV25['country'] != 'Australia'],
                    locations='country',
                    locationmode='country names',
                    color='available',
                    color_discrete_map={True: 'steelblue', False: 'gray'},
                    center={'lat':50 , 'lon':20 },
                    hover_name='country',
                    title='Eurovision 2025 Participants')

fig.update_geos(projection_scale=4)

fig2 = px.choropleth(EV25[EV25['country'] == 'Australia'],
                    locations='country',
                    locationmode='country names',
                    color='available',
                    color_discrete_map={True: 'steelblue', False: 'gray'}, # Define colors
                    center={'lat': -35, 'lon': 141},
                    fitbounds='locations',
                    hover_name='country',
                    )

st.title('Eurovision 2025 Party!!')

st.subheader("Available Countries")

col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)
st.table(guest_list)
