#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import os
import db_rw as dbrw
import html_mdset
from http import cookies

cookie = cookies.SimpleCookie()

cookie.load(os.environ["HTTP_COOKIE"])
username = cookie["LOGINNAME"].value

#エラーをブラウザ上で見れるようにする
cgitb.enable()

# HTML is following
print("Content-Type: text/html")
print("Set-Cookie: LOGINNAME=Guest; Path=/; ")
print("")


dbrw.reload_user_id()
userlist = dbrw.USER_ID




print('<head>')
print('<meta charset="utf-8">')
print('<meta http-equiv="refresh" content="2; URL=../index.html">')
print('<title>REDIRECTING....</title>')
print('</head>')


#print(user_name, password)