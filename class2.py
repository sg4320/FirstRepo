import pandas as pd

names = ['alan','bob','charlie','don']
ages = [22,33,44,55]
cities = ['nyc','miami','houston','los angeles']

mydata = zip(names,ages,cities)
mydata

mydf = pd.DataFrame(data=mydata)