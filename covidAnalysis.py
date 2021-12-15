#installing lybrabries
#folium is use to vizualise the covid cases.
#ploty use to plot dynamic plots or we can say to create interactive plots.
In [2]:
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import math
import random
from datetime import timedelta # used in coustam date format
import warnings
warnings.filterwarnings('ignore') #to ignore the warnings
#color pallette
cnf = '#393e46'
dth = '#ff2e63'
rec = '#21bf73'
act = '#fe9801'
In [ ]:
In [3]:
#Data set Preparation
In [4]:
df = pd.read_csv("c19.csv",parse_dates=['Date'])
In [5]:
df['Province/State'] = df['Province/State'].fillna("")
df
country_daywise = pd.read_csv("country_daywise.csv")
countrywise = pd.read_csv("countrywise.csv")
daywise = pd.read_csv("daywise.csv")
In [7]:
country_daywise.head()
In [8]:
countrywise.head()
In [9]:
daywise.head()
In [10]:
TRACKING CORONA VIRUS
11
#confirmed || recovered || deaths per day
In [11]:
confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()
recovered = df.groupby('Date').sum()['Recovered'].reset_index()
deaths = df.groupby('Date').sum()['Deaths'].reset_index()
In [12]:
confirmed.head()
In [13]:
recovered.head()
In [14]:
deaths.head()
In [15]:
# checking null valuse in "df"
In [16]:
df.isnull().sum()
In [17]:
#SCATTER GRAPH --- imported from plotly.graph_objects
In [18]:
fig = go.Figure()
fig.add_trace(go.Scatter(x = confirmed['Date'], y=confirmed['Confirmed'],
mode='lines+markers', name = 'Confirmed', line = dict(color = "Orange", width=2)))
fig.add_trace(go.Scatter(x = recovered['Date'], y=recovered['Recovered'],
mode='lines+markers', name = 'Recovered', line = dict(color = "Green", width=2)))
fig.add_trace(go.Scatter(x = deaths['Date'], y=deaths['Deaths'],
mode='lines+markers', name = 'Deaths', line = dict(color = "Red", width=2)))
fig.update_layout(title='WORLDWIDE COVID CASES', xaxis_tickfont_size = 14, yaxis =
dict(title = "Number Of Cases"))
fig.show()
In [19]:
#CASE DENSITY ANIMATION ON WORLD MAP
In [20]:
df.info()
<class 'pandas.core.frame.DataFrame'> RangeIndex: 191620 entries, 0 to 191619
Data columns (total 9 columns): # Column Non-Null Count Dtype --- ------ -----
--------- ----- 0 Date 191620 non-null datetime64[ns] 1 Province/State 191620
non-null object 2 Country 191620 non-null object 3 Lat 191620 non-null float64
4 Long 191620 non-null float64 5 Confirmed 191620 non-null int64 6 Recovered
191620 non-null int64 7 Deaths 191620 non-null int64 8 Active 191620 non-null
int64 dtypes: datetime64[ns](1), float64(2), int64(4), object(2) memory usage:
13.2+ MB
In [21]:
#as u see date is in datetime format so convert into string format
In [22]:
df['Date'] = df['Date'].astype(str)
In [23]:
#so date is converted into string format
In [24]:
# plotting the density map using --> import plotly.express as px
TRACKING CORONA VIRUS
12
In [25]:
fid = px.density_mapbox(df, lat = 'Lat', lon='Long', hover_name='Country',
 hover_data=['Confirmed', 'Recovered', 'Deaths'],
animation_frame='Date',
 color_continuous_scale='Portland', radius=10, zoom=0,
height=700)
fid.update_layout(title = "WorldWide Covid Cases Analysics")
fid.update_layout(mapbox_style = 'open-street-map', mapbox_center_lon=0)
fid.show()
In [26]:
#convert date to its original format
In [27]:
#CASES OVER THE TIME WITH AREA PLOT
In [28]:
df['Date'] = pd.to_datetime(df['Date'])
df.info()
<class 'pandas.core.frame.DataFrame'> RangeIndex: 191620 entries, 0 to 191619
Data columns (total 9 columns): # Column Non-Null Count Dtype --- ------ -----
--------- ----- 0 Date 191620 non-null datetime64[ns] 1 Province/State 191620
non-null object 2 Country 191620 non-null object 3 Lat 191620 non-null float64
4 Long 191620 non-null float64 5 Confirmed 191620 non-null int64 6 Recovered
191620 non-null int64 7 Deaths 191620 non-null int64 8 Active 191620 non-null
int64 dtypes: datetime64[ns](1), float64(2), int64(4), object(2) memory usage:
13.2+ MB
In [29]:
#TREE MAP using --> import plotly.express as px
In [30]:
t = df.groupby('Date')['Confirmed', 'Deaths', 'Recovered',
'Active'].sum().reset_index()
t = t[t['Date']==max(t['Date'])].reset_index(drop = True) 
# getting latest data only
t=t.melt(id_vars = 'Date', value_vars = ['Active', 'Deaths', 'Recovered']) 
# melt plots
fig=px.treemap(t, path=['variable'], values = 'value', height=250, width=800,
color_discrete_sequence=[act, rec, dth])
fig.data[0].textinfo = 'label+text+value'
fig.show()
In [31]:
t = df.groupby('Date')['Recovered', 'Deaths', 'Active'].sum().reset_index();
t = t.melt(id_vars = 'Date', value_vars = ['Recovered', 'Deaths', 'Active'],
var_name = 'Case', value_name = 'Count')
t
In [32]:
#confirmed cases with choropleth map
In [33]:
country_daywise.head():
In [34]:
TRACKING CORONA VIRUS
13
f = px.choropleth(country_daywise, locations='Country', locationmode='country
names', color = np.log(country_daywise['Confirmed']),
 hover_name = 'Country', animation_frame=country_daywise['Date'],
 title='Cases over time',
color_continuous_scale=px.colors.sequential.Inferno)
f.update(layout_coloraxis_showscale=True)
f.show()
In [35]:
#DEATHS AND RECOVERIES PER 100 CASES useing --> import plotly.express as px
In [36]:
daywise.tail()
In [37]:
fc = px.bar(daywise, x='Date', y='Confirmed', color_discrete_sequence=[act])
fd = px.bar(daywise, x='Date', y='Deaths', color_discrete_sequence=[dth])
f = make_subplots(rows=1, cols=2, shared_xaxes=False,
horizontal_spacing=0.1,subplot_titles=('Confired cases', 'Deaths cases'))
# adding "fc" and "fd" into figure canvas "f"
f.add_trace(fc['data'][0], row=1, col=1)
f.add_trace(fd['data'][0], row=1, col=2)
f.update_layout(height=400)
f.show()
In [38]:
#conecting to the jovian
In [39]:
# conformed and death cases
In [40]:
daywise
In [41]:
# per 100 cases using --> import plotly.express as px
In [42]:
f1 = px.line(daywise, x='Date', y = 'Deaths / 100 Cases',
color_discrete_sequence=[dth])
f2 = px.line(daywise, x='Date', y = 'Recovered / 100 Cases',
color_discrete_sequence=[rec])
f3 = px.line(daywise, x='Date', y = 'Deaths / 100 Recovered',
color_discrete_sequence=[rec])
f = make_subplots(rows = 1, cols = 3, shared_xaxes=False,
horizontal_spacing=0.2,subplot_titles=('Deaths / 100 cases', 'Recovered / 100
cases', 'Deaths / 100 Recovered'))
f.add_trace(f1['data'][0], row=1, col=1)
f.add_trace(f2['data'][0], row=1, col=2)
f.add_trace(f3['data'][0], row=1, col=3)
f.update_layout(height = 400)
f.show()
TRACKING CORONA VIRUS
14
In [43]:
#New cases and No. of countries
In [44]:
fc = px.line(daywise, x='Date', y = 'Confirmed', color_discrete_sequence=[act])
fd = px.line(daywise, x='Date', y = 'No. of Countries',
color_discrete_sequence=[dth])
f = make_subplots(rows = 1, cols = 2, shared_xaxes=False, horizontal_spacing=0.1,
 subplot_titles=('No. of New Cases Per Day', 'No. of Countries'))
f.add_trace(fc['data'][0], row = 1, col = 1)
f.add_trace(fd['data'][0], row = 1, col = 2)
f.show()
In [45]:
#top 15 countries case analysis
In [46]:
top = 15
fc = px.bar(countrywise.sort_values('Confirmed').tail(top), x = 'Confirmed',
y='Country', text = 'Confirmed', orientation='h', color_discrete_sequence=[cnf])
fd = px.bar(countrywise.sort_values('Deaths').tail(top), x = 'Deaths',
y='Country', text = 'Deaths', orientation='h', color_discrete_sequence=[dth])
fa = px.bar(countrywise.sort_values('Active').tail(top), x = 'Active',
y='Country', text = 'Active', orientation='h', color_discrete_sequence=[act])
fnc = px.bar(countrywise.sort_values('New Cases').tail(top), x = 'New Cases',
y='Country', text = 'New Cases', orientation='h', color_discrete_sequence=[act])
f = make_subplots(rows = 5 , cols = 2, shared_xaxes=False, horizontal_spacing=
0.14, vertical_spacing=0.1, subplot_titles=('Confirmed Cases', 'Deaths Reported',
'Active Cases', 'New Cases'))
f.add_trace(fc['data'][0], row = 1, col = 1)
f.add_trace(fd['data'][0], row = 1, col = 2)
 
f.add_trace(fa['data'][0], row = 2, col = 1)
f.add_trace(fnc['data'][0], row = 2, col = 2)
 
f.update_layout(height = 4000)
f.show()
In [47]:
# bar plot
In [48]:
#top confiremd cases
In [49]:
#f = px.bar(country_daywise, x = 'Date', y ='Confirmed', color = 'Country',
height=600, title = 'Confired', color_discrete_sequence=px.colors.cyclical.mygbm)
#f.show()
TRACKING CORONA VIRUS
15
In [50]:
#top death cases
In [51]:
#f = px.bar(country_daywise, x = 'Date', y ='Deaths', color = 'Country',
height=600, title = 'Deaths', color_discrete_sequence=px.colors.cyclical.mygbm)
#f.show()
In [52]:
#top recovery cases
In [53]:
#f = px.bar(country_daywise, x = 'Date', y ='Recovered', color = 'Country',
height=600, title = 'Recovered', color_discrete_sequence=px.colors.cyclical.mygbm)
#f.show()
In [54]:
# covid - 19 vs other similar epidemics
In [55]:
country_daywise
In [56]:
epidemics = pd.DataFrame({
 'epidemic' : ['COVID19', 'SARS', 'EBOLA', 'MERS', 'H1N1'],
 'start_year' : [2019, 2002, 2013, 2012, 2009],
 'end_year' : [2021, 2004, 2016, 2020, 2010],
 'confirmed' : [country_daywise['Confirmed'].sum(), 8422, 28446, 2519,
6724149],
 'deaths' : [country_daywise['Deaths'].sum(), 813, 11323, 866, 19654]
})
epidemics['mortality'] = round((epidemics['deaths']/epidemics['confirmed'])*100,2)
epidemics.head()
In [57]:
temp = epidemics.melt(id_vars='epidemic', value_vars=['confirmed', 'deaths',
'mortality'], var_name='Case', value_name='Value')
temp
In [58]:
fig = px.bar(temp, x = 'epidemic', y='Value', color='epidemic', text='Value',
facet_col='Case', color_discrete_sequence=px.colors.qualitative.Bold)
fig.update_traces(textposition = 'outside')
fig.update_layout(uniformtext_minsize = 8, uniformtext_mode = 'hide')
fig.update_yaxes(showticklabels = False)
fig.layout.yaxis2.update(matches = None)
fig.layout.yaxis3.update(matches = None)
fig.show()
In [59]:
pip install jovian --upgrade
Requirement already up-to-date: jovian in
c:\users\thimothy\anaconda3\lib\site-packages (0.2.41)Note: you may need to
restart the kernel to use updated packages. Requirement already satisfied,
skipping upgrade: click in c:\users\thimothy\anaconda3\lib\site-packages (from
jovian) (7.1.2) Requirement already satisfied, skipping upgrade: requests in
c:\users\thimothy\anaconda3\lib\site-packages (from jovian) (2.24.0)
Requirement already satisfied, skipping upgrade: pyyaml in
c:\users\thimothy\anaconda3\lib\site-packages (from jovian) (5.3.1)
Requirement already satisfied, skipping upgrade: uuid in
c:\users\thimothy\anaconda3\lib\site-packages (from jovian) (1.30) Requirement
already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
TRACKING CORONA VIRUS
16
in c:\users\thimothy\anaconda3\lib\site-packages (from requests->jovian)
(1.25.9) Requirement already satisfied, skipping upgrade: idna<3,>=2.5 in
c:\users\thimothy\anaconda3\lib\site-packages (from requests->jovian) (2.10)
Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in
c:\users\thimothy\anaconda3\lib\site-packages (from requests->jovian)
(2020.6.20) Requirement already satisfied, skipping upgrade: chardet<4,>=3.0.2
in c:\users\thimothy\anaconda3\lib\site-packages (from requests->jovian)
(3.0.4)
In [60]:
import jovian
In [61]:
jovian.commit()
[jovian] Updating notebook "thomas02032001/minifinal" on https://jovian.ai/
[jovian] Committed successfully! https://jovian.ai/thomas02032001/minifinal
'https://jovian.ai/thomas02032001/minifinal'
