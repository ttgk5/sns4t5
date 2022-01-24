#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import db_rw as dbrw
import html_mdset
import makehash

#エラーをブラウザ上で見れるようにする
cgitb.enable()

# HTML is following
print("Content-Type: text/html")    
print("")

html_mdset.htheader()
html_mdset.htnavibar()

form = cgi.FieldStorage()

user_name = form["user_name"].value
password = form["user_pass"].value

dbrw.reload_user_id()
userlist = dbrw.USER_ID

#hash計算
hashedpw = makehash.make_hash(password)

if user_name in userlist:
    if dbrw.password_search(hashedpw):
        print("Set-Cookie: LOGINNAME=", user_name)
        print('<head>')
        print('<meta charset="utf-8">')
        print('<meta http-equiv="refresh" content="2; URL=../cookietest.html">')
        print('<title>REDIRECTING....</title>')
        print('</head>')
    else:
        html_mdset.htjumbo_s()
        print("ID若しくはパスワードが違っています")
        html_mdset.htjumbo_e()
else:
    html_mdset.htjumbo_s()
    print("ID若しくはパスワードが違っています")
    html_mdset.htjumbo_e()

print(user_name, password)