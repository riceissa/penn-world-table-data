#!/usr/bin/env python3


def mysql_quote(x):
    '''
    Quote the string x using MySQL quoting rules. If x is the empty string,
    return "NULL". Probably not safe against maliciously formed strings, but
    whatever; our input is fixed and from a basically trustable source..
    '''
    if not x:
        return "NULL"
    x = x.replace("\\", "\\\\")
    x = x.replace("'", "''")
    x = x.replace("\n", "\\n")
    return "'{}'".format(x)


def mysql_number(x, typeconv=lambda x: x):
    if not x:
        return "NULL"
    x = x.strip()
    x = x.replace(",", "")
    x = x.replace("%", "")
    return str(typeconv(x))


def mysql_int(x):
    return mysql_number(x, typeconv=int)


def mysql_float(x):
    return mysql_number(x, typeconv=float)
