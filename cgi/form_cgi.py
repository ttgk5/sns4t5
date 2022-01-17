#!usr/bin/python3

import cgi
import cgitb
import db_rw as dbrw

#エラーをブラウザ上で見れるようにする
cgitb.enable()

# HTML is following
print("Content-Type: text/html")    
print("")

form = cgi.FieldStorage()

dbrw.writedb([form["user_name"].value, form["posted_content"].value])

#redirect

print('<head>')
print('<meta charset="utf-8">')
print('<meta http-equiv="refresh" content="2; URL=../cgitest.html">')
print('<title>REDIRECTING....</title>')
print('</head>')