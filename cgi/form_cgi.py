#!/usr/bin/python3

import cgi
import cgitb
import db_rw as dbrw
import os
import html_mdset
from http import cookies

#エラーをブラウザ上で見れるようにする
cgitb.enable()

cookie = cookies.SimpleCookie()
cookie.load(os.environ["HTTP_COOKIE"])
username = cookie["LOGINNAME"].value


# HTML is following
print("Content-Type: text/html")    
print("")

form = cgi.FieldStorage()

dbrw.writedb([username, form["posted_content"].value])

#redirect

if username != "Guest":
    print('<head>')
    print('<meta charset="utf-8">')
    print('<meta http-equiv="refresh" content="2; URL=../index.html">')
    print('<title>REDIRECTING....</title>')
    print('</head>')

else:
    html_mdset.htheader()
    html_mdset.htnavibar()
    html_mdset.htjumbo_s()
    print("ログインもしくは登録お願いします")
    html_mdset.htjumbo_e()