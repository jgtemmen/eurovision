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
EV25['']

fig = px.choropleth(EV25[EV25['country'] != 'Australia'],
                    locations='country',
                    locationmode='country names',
                    color='available',
                    color_discrete_map={True: 'steelblue', False: 'lightgray'},
                    scope='europe',
                    fitbounds='locations',
                    hover_name='country',
                    hover_data = 'semi',
                    title='Eurovision 2025 Participants')

fig2 = px.choropleth(EV25[EV25['country'] == 'Australia'],
                    locations='country',
                    locationmode='country names',
                    color='available',
                    color_discrete_map={True: 'steelblue', False: 'lightgray'}, # Define colors
                    center={'lat': -35, 'lon': 141},
                    fitbounds='locations',
                    hover_name='country',
                    hover_data = 'text'
                    )

st.title('Eurovision 2025 Party!!')

st.subheader("Available Countries")

col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)
