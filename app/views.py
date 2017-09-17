import pandas as pd

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	pdt_data = pd.read_csv("accident.csv")

	results = [tuple(x[:2]) for x in pdt_data[['geox', 'geoy','day_of_week','weather_description','road_class_description']].values if x[0] == float(x[0]) and x[1] == float(x[1]) and x[-1] == 'PARKING LOT']
	x_c = 26.122438
	y_c = -80.137314
	# for r in results:
	# 	print r
	# print x_c, y_c
	return render_template('index.html', title = 'Accident Tracker', results = results, X = x_c, Y = y_c, map_type = 0)