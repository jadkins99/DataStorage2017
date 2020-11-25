#!/usr/bin/env python
# coding: utf-8

# In[25]:


get_ipython().system('pip install folium')
import folium
from folium.plugins import HeatMap
from IPython.display import IFrame
import pandas as pd
import pandas as MyPandas
import os


# In[23]:


def embed_map(map, filename):
    map.save(filename)
    return IFrame(filename, width = '100%', height= '500pz')


# In[53]:


m= folium.Map (location=[40.7128,-74.0060], control_scale=True, zoom_start=12)
m


nyc = [40.7400, -73.985880]

default_zoom = 10


# In[26]:




df_party = pd.read_csv(r'C:\Users\Danie\OneDrive\Documents\party_in_nyc.csv')

df_party.head()


# In[27]:


df_party['count'] = 1

df_party[['Latitude', 'Longitude','count']].groupby(['Latitude', 'Longitude']).sum().sort_values(by='count',ascending=False)


# In[40]:


from folium.plugins import HeatMap


# In[61]:


party_in_NY = folium.Map (location=nyc, control_scale=True, zoom_start=default_zoom)
HeatMap(df_party[['Latitude', 'Longitude','count']].groupby(['Latitude', 'Longitude']).sum().reset_index().values.tolist(),radius=10).add_to(party_in_NY);
party_in_NY


# In[48]:


df_party['Created Date'] = pd.to_datetime(df_party['Created Date'], format='%Y-%m-%d %H:%M:%S')
df_party['hour'] = df_party['Created Date'].dt.hour


# In[50]:


df_party_hour_list = []

for hour in df_party['hour'].sort_values().unique():
    df_party_hour_list.append(df_party.loc[df_party['hour'] == hour, ['Latitude', 'Longitude', 'count']].groupby(['Latitude', 'Longitude']).sum().reset_index().values.tolist())


# In[68]:


from folium.plugins import HeatMapWithTime
party_in_NY = folium.Map (location=nyc, control_scale=True, zoom_start=default_zoom)
HeatMapWithTime(df_party_hour_list,radius=11, gradient={0.1: 'blue', 0.5: 'lime', 0.7: 'orange', 1: 'red'}, min_opacity=0.4, max_opacity=0.8, use_local_extrema=True).add_to(party_in_NY)

# display base map with HeatMapWithTime


party_in_NY


# In[1]:






party_in_NY.save('party_in_NY.html')



# In[ ]:




