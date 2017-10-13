#!/usr/bin/env python3

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


# A simple plot created by directly querying the db

cnx = mysql.connector.connect(user='issa', database='devecondata')

df = pd.read_sql("select * from data where database_url = 'http://www.rug.nl/ggdc/docs/pwt56_forweb.xls'", con=cnx)

jpn = df[(df['metric'] == 'Component shares of CGDP: Consumption') & (df['region'] == 'JAPAN')]

plt.plot(jpn.year, jpn.value)

plt.show()


a = df[df.metric == 'Expenditure-side real GDP at chained PPPs']
a.pivot(index='year', columns='region', values='value').plot(legend=False)
plt.show()
