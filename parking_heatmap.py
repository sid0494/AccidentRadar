import pandas as pd

pdt_data = pd.read_csv("parking-tickets.csv")
locations = []

data = [tuple(x) for x in pdt_data[['long_', 'lat']].values]

print len(data), data[:5]

