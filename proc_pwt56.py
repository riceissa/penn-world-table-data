#!/usr/bin/env python3

import csv
import sys

from util import *


# Variable explanations at
# http://www.rug.nl/ggdc/docs/pwt56appendix.pdf
cols = {
        ""
        "POP": {
            "units": "People",
            "metric": "Population",
        },
        "RGDPCH": {
            "units": "?",
            "metric": "Chain-index: Real gross domestic product",
        },
        "RGDPL": {
            "units": "?",
            "metric": "Real gross domestic product",
        },
        "c": {
            "units": "Unitless",
            "metric": "Real shares of components of RGDPL: Comsumption",
        },
        "i": {
            "units": "Unitless",
            "metric": "Real shares of components of RGDPL: Investment",
        },
        "g": {
            "units": "Unitless",
            "metric": "Real shares of components of RGDPL: Government",
        },
        "RGDPTT": {
            "units": "?",
            "metric": "Terms of trade movement",
        },
        "Y": {
            "units": "Unitless",
            "metric": "Gross domestic product relative to US=100",
        },
        "CGDP": {
            "units": "international dollar",
            "metric": "Gross domestic product in current-year international prices",
        },
        "cc": {
            "units": "Unitless",
            "metric": "Component shares of CGDP: Consumption",
        },
        "ci": {
            "units": "Unitless",
            "metric": "Component shares of CGDP: Investment",
        },
        "cg": {
            "units": "Unitless",
            "metric": "Component shares of CGDP: Government",
        },
        "P": {
            "units": "?",
            "metric": "Price levels (PPP/Exchange Rate): Gross domestic product",
        },
        "PC": {
            "units": "Unitless",
            "metric": "Price levels (PPP/Exchange Rate): Components: Consumption",
        },
        "PI": {
            "units": "Unitless",
            "metric": "Price levels (PPP/Exchange Rate): Components: Investment",
        },
        "PG": {
            "units": "Unitless",
            "metric": "Price levels (PPP/Exchange Rate): Components: Government",
        },
        "XR": {
            "units": "?",
            "metric": "Exchange rates",
        },
        "RGDPEA": {
            "units": "Unitless",
            "metric": "Price levels (PPP/Exchange Rate): Components: Consumption",
        },
        "RGDPW": {
            "units": "? per person",
            "metric": "Real GDP chain per worker",
        },
        "KAPW": {
            "units": "? per person",
            "metric": "Capital stock per worker",
        },
        "KDUR": {
            "units": "Unitless",
            "metric": "Producers durables: % of capital stock",
        },
        "KNRES": {
            "units": "Unitless",
            "metric": "Non residential construction: % of capital stock",
        },
        "KOTHER": {
            "units": "Unitless",
            "metric": "Other construction: % of capital stock",
        },
        "KRES": {
            "units": "Unitless",
            "metric": "Residential construction: % of capital stock",
        },
        "KTRANP": {
            "units": "Unitless",
            "metric": "Transport equipment: % of capital stock",
        },
        "OPEN": {
            "units": "?",
            "metric": "Openness: (exports + imports)/(CGDP)",
        },
        "RGNP": {
            "units": "Unitless",
            "metric": "Real Gross National Product (% of CGDP)",
        },
        "IPRI": {
            "units": "Unitless",
            "metric": "Gross Domestic Private Investment (% of gross domestic investment)",
        },
        "STLIV": {
            "units": "Unitless",
            "metric": "Standard of Living: Private and public consumption less defense spending as a percent of RGDPL",
        },
}


insert_line = "insert into data(region, year, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

with open("pwt56_forweb.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        for col in sorted(row):
            if row[col] and col in cols and row[col] != "na":
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(row["Country"]),  # region
                    mysql_int(row["Year"]),  # year
                    mysql_quote("http://www.rug.nl/ggdc/docs/pwt56_forweb.xls"),  # database_url
                    mysql_quote(""),  # data_retrieval_method
                    mysql_quote(cols[col]["metric"]),  # metric
                    mysql_quote(cols[col]["units"]),  # units
                    mysql_float(row[col], cols[col].get("factor", 1)),  # value
                    mysql_quote(""),  # notes
                ]) + ")")
                first = False
                count += 1
                if count > 5000:
                    count = 0
                    first = True
                    print(";")
    if not first:
        print(";")
