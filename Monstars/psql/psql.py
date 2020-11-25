import os
import plotly.express as px
import plotly.offline as po
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import psycopg2
conn = psycopg2.connect("dbname=monstars user=bweisman")
cur=conn.cursor()

#barplot of airbnbs for each neighborhood
#vs
#barplot of hotels for each neighborhood

df=pd.read_sql_query('select avg_rate from "new_york_hotels" where city = %s;', con=conn, params={"New York"})
df2=pd.read_sql_query('select price from ab_nyc_2019 where room_type= %s;', con=conn, params={"Entire home/apt"})

#cur.execute("select latitude,longitude,price from ab_nyc_2019 limit 10;")
#t=cur.fetchall()

#fig1=df.plot.bar(rot=0)
fig2=df2.plot.bar(rot=0)

#plt.savefig('/var/www/Monstars/static/fig1.png')
plt.savefig('/var/www/Monstars/static/fig2.png')

if not os.path.exists("images"):
	os.mkdir("images")
#fig1.plot()
fig2.plot()
`
#fig1.savefig('/images/fig1.png')
#print(df)
#print(df2)
plt.show()
conn.close()
cur.close()
