#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import db_rw as dbrw

#エラーをブラウザ上で見れるようにする
cgitb.enable()

# HTML is following
print("Content-Type: text/html; charset=Shift_JIS")
print("")

print("<head>")
print('<meta charset="Shift_JIS">')
print("<title>SNS for T5</title>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link rel="stylesheet" href="../css/bootstrap.css">')
print('<script type="text/javascript" src="../js/jquery-3.6.0.js"></script>')
print('<script type="text/javascript" src="../js/bootstrap.js"></script>')
print('</head>')


dbrw.maketimeline(None, "showall")


#print("<p>", str(content), "</p>")




