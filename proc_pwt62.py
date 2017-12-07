#!/usr/bin/env python3

import csv
import sys

from devec_sql_common import *

print_insert_header()


cols = {
        "PPP": {
            "units": "Unitless",
            "metric": "Purchasing Power Parity over GDP (US=1)",
        },
        "cgdp": {
            "units": "international dollar",
            "metric": "Real Gross Domestic Product per Capita",
        },
        "cc": {
            "units": "Unitless",
            "metric": "Consumption Share of CGPD",
        },
        "cg": {
            "units": "Unitless",
            "metric": "Government Share of CGDP",
        },
        "ci": {
            "units": "Unitless",
            "metric": "Investment Share of CGDP",
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
            "metric": "CGDP Relative to the United States",
        },
        "rgdpl": {
            "units": "international dollar",
            "metric": "Real GDP per capita (Constant Prices: Laspeyres), derived from growth rates of c, g, i",
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
            "metric": "Consumption Share of RGDPL",
        },
        "kg": {
            "units": "Unitless",
            "metric": "Government Share of RGDPL",
        },
        "ki": {
            "units": "Unitless",
            "metric": "Investment Share of RGDPL",
        },
        "grgdpch": {
            "units": "Unitless",
            "metric": "growth rate of Real GDP Chain per capita (RGDPCH)",
        },
}


insert_line = "insert into data(region, odate, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

with open("pwt62_data.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        for col in sorted(row):
            if row[col] and col in cols and row[col] != "na":
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + uniq_join([
                    mysql_quote(region_normalized(row["country"])),  # region
                    mysql_string_date(row["year"]),  # odate
                    mysql_quote("http://www.rug.nl/ggdc/docs/pwt62_data.xlsx"),  # database_url
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


print_insert_footer()
