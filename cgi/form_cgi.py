#!usr/bin/python3

import cgi
import cgitb

#エラーをブラウザ上で見れるようにする
cgitb.enable()

# HTML is following
print("Content-Type: text/html")    
print("")




form = cgi.FieldStorage()

print("<h1>", form["user_name"].value, "</h1>")