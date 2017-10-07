#!/usr/bin/env python3

import csv

from util import *


cols = {
        "rgdpe": {
            "units": "2011 US dollars",
            "metric": "Expenditure-side real GDP",
            "factor": 1e6,
        },
        "rgdpo": {
            "units": "2011 US dollars",
            "metric": "Output-side real GDP",
            "factor": 1e6,
        },
        "pop": {
            "units": "People",
            "metric": "Population",
            "factor": 1e6,
        },
        "emp": {
            "units": "People",
            "metric": "Number of persons engaged",
            "factor": 1e6,
        },
        "avh": {
            "units": "Hours",
            "metric": "Average annual hours worked by persons engaged",
        },
        "hc": {
            "units": "Index",
            "metric": "Human capital index",
        },
}


print("""insert into data(region, year, database_url,
         data_retrieval_method, metric, units, value, notes) values""")


with open("pwt90.csv", newline='') as f:
    reader = csv.DictReader(f)
    first = True

    for row in reader:
        for col in sorted(row):
            if row[col] and col in cols:
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(row["country"]),  # region
                    mysql_int(row["year"]),  # year
                    mysql_quote("http://www.rug.nl/ggdc/docs/pwt90.xlsx"),  # database_url
                    mysql_quote(""),  # data_retrieval_method
                    mysql_quote(cols[col]["metric"]),  # metric
                    mysql_quote(cols[col]["units"]),  # units
                    mysql_float(row[col], cols[col].get("factor", 1)),  # value
                    mysql_quote(""),  # notes
                ]) + ")")
                first = False
    print(";")
