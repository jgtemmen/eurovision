import pandas as pd
import plotly.express as px
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

# Main Europe Map
fig = px.choropleth(EV25[EV25['country'] != 'Australia'],
                    locations='country',
                    locationmode='country names',
                    color='available',
                    color_discrete_map={True: 'blue', False: 'lightgray'},
                    scope='europe',
                    fitbounds='locations',
                    hover_data=['semi'],
                    hover_name='country',
                    title='Eurovision 2025')

# Australia Inset Map
fig2 = px.choropleth(EV25[EV25['country'] == 'Australia'],
                    locations='country',
                    locationmode='country names',
                    color='available',
                    color_discrete_map={True: 'blue', False: 'lightgray'},
                    center={'lat': -25, 'lon': 135},
                    fitbounds='locations',
                    hover_data=['semi'],
                    hover_name='country')

# Update layout to add inset map
fig.update_layout(
    geo=dict(
        scope='europe'
    ),
    layout_geo2=dict(  # Changed from geo2=dict to layout_geo2=dict
        scope='asia',
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue',
        center={'lat': -25, 'lon': 135},
        projection_scale=0.4,
        x=0.8,
        y=0.1,
        xanchor='right',
        yanchor='bottom'
    )
)

# Add the trace from fig2 to fig
fig.add_trace(fig2.data[0])

st.title('Eurovision 2025 Party!!')
st.subheader("Available Countries")
st.plotly_chart(fig, use_container_width=True)
