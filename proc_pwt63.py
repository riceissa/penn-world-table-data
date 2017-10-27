#!/usr/bin/env python3

import csv
import sys

from util import *


cols = {
        "ppp": {
            "units": "Unitless",
            "metric": "Purchasing Power Parity over GDP (US=1)",
        },
        "cgdp": {
            "units": "international dollar",
            "metric": "Real Gross Domestic Product per Capita, current price",
        },
        "cc": {
            "units": "Unitless",
            "metric": "Consumption Share of Real Gross Domestic Product per Capita, current price",
        },
        "cg": {
            "units": "Unitless",
            "metric": "Government Share of Real Gross Domestic Product per Capita, current price",
        },
        "ci": {
            "units": "Unitless",
            "metric": "Investment Share of Real Gross Domestic Product per Capita, current price",
        },
        "p": {
            "units": "Unitless",
            "metric": "Price Level of Gross Domestic Product (US=100)",
        },
        "pc": {
            "units": "PPP over consumption / XRAT",
            "metric": "Price Level of Consumption",
        },
        "pg": {
            "units": "PPP over government consumption / XRAT",
            "metric": "Price Level of Government",
        },
        "pi": {
            "units": "PPP over investment / XRAT",
            "metric": "Price Level of Investment",
        },
        "openc": {
            "units": "Unitless",
            "metric": "Openness in Current Prices",
        },
        "cgnp": {
            "units": "Unitless",
            "metric": "Ratio of GNP to GDP",
        },
        "y": {
            "units": "Unitless",
            "metric": "Real Gross Domestic Product per Capita Relative to the United States (G-K method, current price) (US=100)",
        },
        "yEKS": {
            "units": "Unitless",
            "metric": "Real Gross Domestic Product per Capita Relative to the United States (EKS method, current price) (US=100)",
        },
        "yCPDW": {
            "units": "Unitless",
            "metric": "Real Gross Domestic Product per Capita Relative to the United States (weighted CPD method, current price) (US=100)",
        },
        "rgdpl": {
            "units": "international dollar",
            "metric": "Real GDP per capita (Constant Prices: Laspeyres), derived from growth rates of c, g, i",
        },
        "rgdpl2": {
            "units": "international dollar",
            "metric": "Real GDP per capita (Constant Prices: Laspeyres), derived from growth rates of domestic absorption",
        },
        "rgdpch": {
            "units": "international dollar",
            "metric": "Real GDP per capita (Constant Prices: Chain series)",
        },
        "rgdpeqa": {
            "units": "international dollar per person",
            "metric": "Real GDP Chain per equivalent adult",
        },
        "rgdpwok": {
            "units": "international dollar per person",
            "metric": "Real GDP Chain per worker",
        },
        "rgdpl2wok": {
            "units": "international dollar per person",
            "metric": "Real GDP Laspeyres2 per worker",
        },
        "rgdpl2pe": {
            "units": "international dollar per person",
            "metric": "Real GDP Laspeyres2 person engaged",
        },
        "rgdpl2te": {
            "units": "international dollar per person",
            "metric": "Real GDP Laspeyres2 per person counted in total employment",
        },
        "rgdpl2th": {
            "units": "international dollar per hour",
            "metric": "Real GDP Laspeyres2 per hour worked by employees",
        },
        "rgdptt": {
            "units": "international dollar",
            "metric": "Real Gross Domestic Income (RGDPL adjusted for Terms of Trade changes)",
        },
        "openk": {
            "units": "Unitless",
            "metric": "Openness in Constant Prices",
        },
        "kc": {
            "units": "Unitless",
            "metric": "Consumption Share of Real GDP per capita (RGDPL)",
        },
        "kg": {
            "units": "Unitless",
            "metric": "Government Share of Real GDP per capita (RGDPL)",
        },
        "ki": {
            "units": "Unitless",
            "metric": "Investment Share of Real GDP per capita (RGDPL)",
        },
        "grgdpch": {
            "units": "Unitless",
            "metric": "growth rate of Real GDP Chain per capita (RGDPCH)",
        },
        "grgdpl2": {
            "units": "Unitless",
            "metric": "growth rate of Real GDP Laspeyres2 per capita (RGDPL2)",
        },
}


insert_line = "insert into data(region, odate, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

with open("pwt63_w_country_names.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        for col in sorted(row):
            if row[col] and col in cols:
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(row["country"]),  # region
                    mysql_string_date(row["year"]),  # odate
                    mysql_quote("http://www.rug.nl/ggdc/docs/pwt63_nov182009version.zip"),  # database_url
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
