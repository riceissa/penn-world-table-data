#!/usr/bin/env python3

import csv
import pycountry
import sys

from util import *

# These are the countries that pycountry does not have under alpha3
mycountry = {
        "GER": "Germany",
        "ROM": "Romania",
        "ZAR": "Zaire",
        "CH2": "China Version 2",
}

cols = {
        "tcgdp": {
            "units": "international dollar",
            "metric": "Total PPP Converted GDP, G-K method, at current prices",
            "factor": 1e6,
        },
        "cgdp": {
            "units": "international dollar",
            "metric": "PPP Converted GDP Per Capita, G-K method, at current prices",
        },
        "cgdp2": {
            "units": "international dollar",
            "metric": "PPP Converted GDP Per Capita,  average GEKS-CPDW, at current prices",
        },
        "cda2": {
            "units": "international dollar",
            "metric": "PPP Converted Domestic Absorption Per Capita, average GEKS-CPDW, at current prices",
        },
        "cc": {
            "units": "Unitless",
            "metric": "Consumption Share of PPP Converted GDP Per Capita at current prices [cgdp], (%)",
        },
        "cg": {
            "units": "Unitless",
            "metric": "Government Consumption Share of PPP Converted GDP Per Capita at current prices [cgdp], (%)",
        },
        "ci": {
            "units": "Unitless",
            "metric": "Investment Share of PPP Converted GDP Per Capita at current prices [cgdp], (%)",
        },
        "p": {
            "units": "Unitless",
            "metric": "Price Level of GDP, G-K method (US = 100)",
        },
        "p2": {
            "units": "Unitless",
            "metric": "Price Level of GDP, average of GEKS-CPDW (US = 100)",
        },
        "pc": {
            "units": "PPP over consumption / XRAT",
            "metric": "Price Level of Consumption",
        },
        "pg": {
            "units": "PPP over government consumption / XRAT",
            "metric": "Price Level of Government Consumption",
        },
        "pi": {
            "units": "PPP over investment / XRAT",
            "metric": "Price Level of Investment",
        },
        "openc": {
            "units": "Unitless",
            "metric": "Openness at Current Prices (%)",
        },
        "cgnp": {
            "units": "Unitless",
            "metric": "Ratio of GNP to GDP (%)",
        },
        "y": {
            "units": "Unitless",
            "metric": "PPP Converted GDP Per Capita Relative to the United States, G-K method, at current prices, [cgdp](US = 100)",
        },
        "y2": {
            "units": "Unitless",
            "metric": "PPP Converted GDP Per Capita Relative to the United States, average GEKS-CPDW, at current prices, [cgdp2](US = 100)",
        },
        "rgdpl": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Per Capita (Laspeyres), derived from growth rates of c, g, i, at 2005 constant prices",
        },
        "rgdpl2": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Per Capita (Laspeyres), derived from growth rates of domestic absorption, at 2005 constant prices",
        },
        "rgdpch": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Per Capita (Chain Series), at 2005 constant prices",
        },
        "kc": {
            "units": "Unitless",
            "metric": "Consumption Share of PPP Converted GDP Per Capita at 2005 constant prices [rgdpl]",
        },
        "kg": {
            "units": "Unitless",
            "metric": "Government Consumption Share of PPP Converted GDP Per Capita at 2005 constant prices [rgdpl]",
        },
        "ki": {
            "units": "Unitless",
            "metric": "Investment Share of PPP Converted GDP Per Capita at 2005 constant prices [rgdpl]",
        },
        "openk": {
            "units": "Unitless",
            "metric": "Openness at 2005 constant prices (%)",
        },
        "rgdpeqa": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Chain per equivalent adult at 2005 constant prices",
        },
        "rgdpwok": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Chain per worker at 2005 constant prices",
        },
        "rgdpl2wok": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Laspeyres per worker at 2005 constant prices",
        },
        "rgdpl2pe": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Laspeyres person engaged at 2005 constant prices",
        },
        "rgdpl2te": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Laspeyres per person counted in total employment at 2005 constant prices",
        },
        "rgdpl2th": {
            "units": "2005 international dollar",
            "metric": "PPP Converted GDP Laspeyres per hour worked by employees at 2005 constant prices",
        },
        "rgdptt": {
            "units": "2005 international dollar",
            "metric": "PPP Converted Gross Domestic Income (RGDPL adjusted for Terms of Trade changes) at 2005 constant prices",
        },
}


insert_line = "insert into data(region, year, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

with open("pwt71_wo_country_names_wo_g_vars.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            # Older versions of pycountry use "alpha3" while newer ones use
            # "alpha_3", so check which one to use
            if "alpha3" in list(pycountry.countries)[0].__dir__():
                country = pycountry.countries.get(alpha3=row["isocode"]).name
            else:
                country = pycountry.countries.get(alpha_3=row["isocode"]).name
        except KeyError:
            country = mycountry[row["isocode"]]
        for col in sorted(row):
            if row[col] and col in cols:
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(country),  # region
                    mysql_int(row["year"]),  # year
                    mysql_quote("http://www.rug.nl/ggdc/docs/pwt71_11302012version.zip"),  # database_url
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
