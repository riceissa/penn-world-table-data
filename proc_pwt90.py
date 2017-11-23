#!/usr/bin/env python3

import csv

from devec_sql_common import *


cols = {
        "rgdpe": {
            "units": "2011 international dollar",
            "metric": "Expenditure-side real GDP at chained PPPs",
            "factor": 1e6,
        },
        "rgdpo": {
            "units": "2011 international dollar",
            "metric": "Output-side real GDP at chained PPPs",
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
            "units": "Unitless",
            "metric": "Human capital index, based on years of schooling and returns to education",
        },
        "ccon": {
            "units": "2011 international dollar",
            "metric": "Real consumption of households and government, at current PPPs",
            "factor": 1e6,
        },
        "cda": {
            "units": "2011 international dollar",
            "metric": "Real domestic absorption, (real consumption plus investment), at current PPPs",
            "factor": 1e6,
        },
        "cgdpe": {
            "units": "2011 international dollar",
            "metric": "Expenditure-side real GDP at current PPPs",
            "factor": 1e6,
        },
        "cgdpo": {
            "units": "2011 international dollar",
            "metric": "Output-side real GDP at current PPPs",
            "factor": 1e6,
        },
        "ck": {
            "units": "2011 international dollar",
            "metric": "Capital stock at current PPPs",
            "factor": 1e6,
        },
        "ctfp": {
            "units": "Unitless",
            "metric": "TFP level at current PPPs (USA=1)",
        },
        "cwtfp": {
            "units": "Unitless",
            "metric": "Welfare-relevant TFP levels at current PPPs (USA=1)",
        },
        "rgdpna": {
            "units": "2011 international dollar",
            "metric": "Real GDP at constant 2011 national prices",
            "factor": 1e6,
        },
        "rconna": {
            "units": "2011 international dollar",
            "metric": "Real consumption at constant 2011 national prices",
            "factor": 1e6,
        },
        "rdana": {
            "units": "2011 international dollar",
            "metric": "Real domestic absorption at constant 2011 national prices",
            "factor": 1e6,
        },
        "rkna": {
            "units": "2011 international dollar",
            "metric": "Capital stock at constant 2011 national prices",
            "factor": 1e6,
        },
        "rtfpna": {
            "units": "Unitless",
            "metric": "TFP at constant national prices (2011=1)",
        },
        "rwtfpna": {
            "units": "Unitless",
            "metric": "Welfare-relevant TFP at constant national prices (2011=1)",
        },
        "labsh": {
            "units": "Unitless",
            "metric": "Share of labour compensation in GDP at current national prices",
        },
        "delta": {
            "units": "Unitless",
            "metric": "Average depreciation rate of the capital stock",
        },
        "xr": {
            "units": "Unitless",
            "metric": "Exchange rate, national currency/USD (market+estimated)",
        },
        "pl_con": {
            "units": "Unitless",
            "metric": "Price level of CCON (PPP/XR), price level of USA GDPo in 2011=1",
        },
        "pl_da": {
            "units": "Unitless",
            "metric": "Price level of CDA (PPP/XR), price level of USA GDPo in 2011=1",
        },
        "pl_gdpo": {
            "units": "Unitless",
            "metric": "Price level of CGDPo (PPP/XR), price level of USA GDPo in 2011=1",
        },
        "csh_c": {
            "units": "Unitless",
            "metric": "Share of household consumption at current PPPs",
        },
        "csh_i": {
            "units": "Unitless",
            "metric": "Share of gross capital formation at current PPPs",
        },
        "csh_g": {
            "units": "Unitless",
            "metric": "Share of government consumption at current PPPs",
        },
        "csh_x": {
            "units": "Unitless",
            "metric": "Share of merchandise exports at current PPPs",
        },
        "csh_m": {
            "units": "Unitless",
            "metric": "Share of merchandise imports at current PPPs",
        },
        "csh_r": {
            "units": "Unitless",
            "metric": "Share of residual trade and GDP statistical discrepancy at current PPPs",
        },
        "pl_c": {
            "units": "Unitless",
            "metric": "Price level of household consumption, price level of USA GDPo in 2011=1",
        },
        "pl_i": {
            "units": "Unitless",
            "metric": "Price level of capital formation, price level of USA GDPo in 2011=1",
        },
        "pl_g": {
            "units": "Unitless",
            "metric": "Price level of government consumption, price level of USA GDPo in 2011=1",
        },
        "pl_x": {
            "units": "Unitless",
            "metric": "Price level of exports, price level of USA GDPo in 2011=1",
        },
        "pl_m": {
            "units": "Unitless",
            "metric": "Price level of imports, price level of USA GDPo in 2011=1",
        },
        "pl_k": {
            "units": "Unitless",
            "metric": "Price level of the capital stock, price level of USA in 2011=1",
        },
}


insert_line = "insert into data(region, odate, database_url, data_retrieval_method, metric, units, value, notes) values"
count = 0
first = True

with open("pwt90.csv", newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        data_retrieval_method = ", ".join([v + " = " + row[v]
            for v in ['i_cig', 'i_xm', 'i_xr', 'i_outlier', 'cor_exp', 'statcap']
            if row[v].strip()])
        for col in sorted(row):
            if row[col] and col in cols:
                if first:
                    print(insert_line)
                print("    " + ("" if first else ",") + "(" + ",".join([
                    mysql_quote(region_normalized(row["country"])),  # region
                    mysql_string_date(row["year"]),  # odate
                    mysql_quote("http://www.rug.nl/ggdc/docs/pwt90.xlsx"),  # database_url
                    mysql_quote(data_retrieval_method),  # data_retrieval_method
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
