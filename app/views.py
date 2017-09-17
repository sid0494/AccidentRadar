import pandas as pd

from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index', methods = ['POST', 'GET'])
def index():
	form_data = request.form
	print form_data
	pdt_data = pd.read_csv("accident.csv")

	results = [tuple(x) for x in pdt_data[['geox', 'geoy','day_of_week','weather_description','road_class_description']].values if x[0] == float(x[0]) and x[1] == float(x[1])]

	if form_data.get('day', 'All') != "All":
		results = [r for r in results if r[2] == form_data.get('day', 'All')]
	if form_data.get('weather', 'All') != "All":
		results = [r for r in results if r[3] == form_data.get('weather', 'All')]
	if form_data.get('road', 'All') != "All":
		results = [r for r in results if r[4] == form_data.get('road', 'All')]

	x_c = 26.1224 #sum([x[0] for x in results])/len(results)
	y_c = -80.1373 #sum([x[1] for x in results])/len(results)
	# for r in results:
	print len(results)
	# 	print r
	# print x_c, y_c
	return render_template('index.html', title = 'Accident Tracker', results = results, X = x_c, Y = y_c)