#!usr/bin/python3

import cgi
import cgitb
import db_rw as dbrw

#エラーをブラウザ上で見れるようにする
cgitb.enable()

# HTML is following
print("Content-Type: text/html;charset=UTF-8"")
print("")

content = dbrw.readdb("test")


print(type(content))
print("<p>", str(content.values[0]), "</p>")
print("<p>", str(content.values[1]), "</p>")



