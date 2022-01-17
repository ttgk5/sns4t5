# -*- coding: utf-8 -*-
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

user_name = form["user_name"].value
password = form["user_pass"].value

print(user_name, password)