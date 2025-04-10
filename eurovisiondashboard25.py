# Packages
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st

# Countries
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

semi1 = ['Iceland', 'Poland', 'Slovenia', 'Estonia', 'Ukraine', 'Sweden',
         'Portugal', 'Norway', 'Belgium', 'Azerbaijan', 'San Marino', 'Albania',
         'Netherlands', 'Croatia', 'Cyprus']
semi2 = ['Australia', 'Montenegro', 'Ireland', 'Latvia', 'Armenia', 'Austria', 'Greece',
         'Lithuania', 'Malta', 'Georgia', 'Denmark', 'Czechia', 'Luxembourg', 'Israel',
         'Serbia', 'Finland']
finalists = ['Switzerland', 'France', 'Germany', 'Italy', 'Spain', 'United Kingdom']

ev25_data = {'country': Countries, 'semi': [], "available": [True for i in Countries]}
for i in Countries:
    if i in finalists:
        ev25_data['semi'].append(3)
    elif i in semi1:
        ev25_data['semi'].append(1)
    elif i in semi2:
        ev25_data['semi'].append(2)
    else:
        print(i, "was missed")
EV25 = pd.DataFrame(ev25_data)

# Europe Map (go.Choropleth)
fig_europe = go.Choropleth(
    locations=EV25[EV25['country'] != 'Australia']['country'],
    locationmode='country names',
    z=EV25[EV25['country'] != 'Australia']['available'],
    colorscale=[[0, 'lightgray'], [1, 'blue']],
    projection_scope='europe',
    showlegend=False,
    name=''  # Suppress the trace name
)

# Australia Inset Map (go.Choropleth)
fig_aus = go.Choropleth(
    locations=EV25[EV25['country'] == 'Australia']['country'],
    locationmode='country names',
    z=EV25[EV25['country'] == 'Australia']['available'],
    colorscale=[[0, 'lightgray'], [1, 'blue']],
    projection_scope='asia',
    showlegend=False,
    name=''  # Suppress the trace name
)

# Create subplots
fig = make_subplots(
    rows=1, cols=1,
    specs=[[{'type': 'choropleth'}]],
    geo_scope='europe'
)

fig.add_trace(fig_europe, row=1, col=1)
fig.add_trace(fig_aus, row=1, col=1)

# Update layout for inset map positioning
fig.update_layout(
    geo=dict(
        scope='europe',
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue',
    ),
    geo2=dict(
        scope='asia',
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue',
        center={'lat': -25, 'lon': 135},
        projection_scale=0.3,
        x=0.8,
        y=0.1,
        xanchor='right',
        yanchor='bottom'
    ),
    showlegend=False,
    margin=dict(l=0, r=0, b=0, t=50)
)

st.title('Eurovision 2025 Party!!')
st.subheader("Available Countries")
st.plotly_chart(fig, use_container_width=True)
