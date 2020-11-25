from flask import Flask,render_template,request 
import pandas as pd
import psycopg2
conn = psycopg2.connect("dbname=monstars user=jadkins")
cur=conn.cursor()


app = Flask(__name__)
app.debug=True

@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/nycMap_private/', methods=['GET'])
def nycMapPage():
	return render_template('nyc_map_private.html')

@app.route('/nycMap_full/', methods=['GET'])
def nycMapPage2():
	return render_template('nyc_map_full.html')

@app.route('/nycMap_shared/', methods=['GET'])
def nycMapPage3():
	return render_template('nyc_map_shared.html')

@app.route('/nycMap_hotels/', methods=['GET'])
def nycMapPage4():
	return render_template('nyc_map_hotel.html')

@app.route('/party/', methods=['GET'])
def nycMapPage5():
	return render_template('party_in_NY.html')

@app.route('/other_figs/', methods=['GET'])
def nycMapPage6():
	return render_template('other_figs.html')

@app.route('/bar_count/', methods=['GET'])
def nycMapPage7():
	return render_template('map_nyc.html')






@app.route('/data/dots', methods=['GET','POST'])
def createDots():
	df = pd.read_sql_query('select id,latitude,longitude,price from "ab_nyc_2019" where room_type = \'Private room\' and price > 0 order by price ',con=conn)
	
	json = df.to_json()
	return json

@app.route('/data/dots2', methods=['GET','POST'])
def createDots2():
	df = pd.read_sql_query('select id,latitude,longitude,price from "ab_nyc_2019" where room_type = \'Entire home/apt\' and price > 0 order by price ',con=conn)
	
	json = df.to_json()
	return json

@app.route('/data/dots3', methods=['GET','POST'])
def createDots3():
	df = pd.read_sql_query('select id,latitude,longitude,price from "ab_nyc_2019"  where room_type = \'Shared room\' and price > 0 order by price',con=conn)
	
	json = df.to_json()
	return json

@app.route('/data/dots4', methods=['GET','POST'])
def createDots4():
	df = pd.read_sql_query('select ean_hotel_id as id,latitude,longitude,avg_rate as price from "new_york_hotels" where avg_rate > 0 order by avg_rate',con=conn)
	
	json = df.to_json()
	return json




if __name__ == "main":
	app.run()


