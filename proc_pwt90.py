#!/usr/bin/env python3

import csv

from util import *


print("""insert into pwt(region, year, database_url,
         data_retrieval_method, metric, units, value, notes) values""")


with open("pwt90.csv", newline='') as f:
    reader = csv.DictReader(f)
    first = True

    for row in reader:
        for var in sorted(row):
            if row[var] and var not in ["countrycode", "country", "year", "currency_unit"]:
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(row["country"]),  # region
                    mysql_int(row["year"]),  # year
                    mysql_quote("http://www.rug.nl/ggdc/docs/pwt90.xlsx"),  # database_url
                    mysql_quote(""),  # data_retrieval_method
                    mysql_quote(var),  # metric
                    mysql_quote(""),  # units
                    mysql_float(row[var]),  # value
                    mysql_quote(""),  # notes
                ]) + ")")
                first = False
    print(";")
