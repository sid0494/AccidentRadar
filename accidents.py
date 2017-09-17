import pandas as pd

pdt_data = pd.read_csv("accident.csv")

data = [tuple(x) for x in pdt_data[['geox', 'geoy']].values]
print len(list(pdt_data))
print len(data), data[:5]