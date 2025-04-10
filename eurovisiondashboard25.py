# -*- coding: utf-8 -*-
"""EurovisionDashboard25

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z_sMi6yAd2H24D6Ry7sxgKT1kGzUfxtJ
"""

#!pip install streamlit
#!pip install ngrok

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

ev25_data = {'country':Countries,'semi':[],"available":[True for i in Countries]}
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

EV25[EV25['country'] != 'Australia']

fig = go.Choropleth(
    locations=EV25[EV25['country'] != 'Australia']['country'],
    locationmode='country names',
    z=EV25[EV25['country'] != 'Australia']['available'],
    colorscale=[[0, 'lightgray'], [1, 'blue']],
    projection={"scope": 'europe'},
    fitbounds="locations",
    hovertext=EV25[EV25['country'] != 'Australia'].apply(lambda row: f"Semi: {row['semi']}", axis=1),
    text=EV25[EV25['country'] != 'Australia']['country']
)

#fig.show()

fig2 = go.Choropleth(EV25[EV25['country'] == 'Australia'],
                    locations='country',
                    locationmode='country names',
                    z='available',
                    colorscale=[[0, 'lightgray'], [1, 'blue']], # Define colors
                    projection={"center": {'lat': -35, 'lon': 141}},
                    fitbounds='locations',
                    hovertext=EV25[EV25['country'] == 'Australia'].apply(lambda row: f"Semi: {row['semi']}", axis=1),
                    text=EV25[EV25['country'] == 'Australia']['country']
                    )
#fig2.show()

euro_fig = make_subplots(
    rows=1, cols=1,
    specs=[[{'type':'choropleth'}]],
    #subplot_titles=('Eurovision 2025') 
)
euro_fig.add_trace(fig, row=1, col=1)

euro_fig.add_trace(fig2, row=1, col=1)

euro_fig.update_layout(
    geo=dict(
        scope='europe'
    ),
    geo2=dict(
        scope='asia',
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue',
        center={'lat': -25, 'lon': 135},
        projection_scale=0.5,
        x=0.8, y=0.1,
        xanchor='right', yanchor='bottom'
    ))
    
st.title('Eurovision 2025 Party!!')

st.subheader("Available Countries")

st.plotly_chart(euro_fig, use_container_width=True)
