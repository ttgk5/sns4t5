#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import os

from matplotlib.style import use
import db_rw as dbrw
import html_mdset as hmd
from http import cookies

#エラーをブラウザ上で見れるようにする
cgitb.enable()


# Cookie Load
try:
    cookie = cookies.SimpleCookie()

    cookie.load(os.environ["HTTP_COOKIE"])

    username = cookie["LOGINNAME"].value
except Exception:
    username = "Guest"
    
# HTML is following
print("Content-Type: text/html")
print("")

hmd.htheader()
hmd.htnavibar()


maincontent = '''
    <div class="container">

    <!--  プロフィール -->
    <div class="profile">
    <div class="row">
    <div class="col-md-2"></div>

    <!-- アイコン -->
    <div class="col-sm-3 col-md-3" style="background-color:white;">
    <!--アイコン画像-->
    <img class="d-block mx-auto mt-4 mb-4 rounded-circle" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy40UeBc_qdzION5Qr7xvLfzBq8kVyk9unaw&usqp=CAU" alt="">
    </div>

    <!--自己紹介欄-->
    <div class="col-sm-9 col-md-7 mt-5" style="background-color:white;">
    <!--名前と更新ボタン-->
    <h2>''' + username +  '''     <button type="button" class="btn-outline-secondary btn-sm"> 更新</button></h2>
    <!--自己紹介文-->
    <p>nanka tekitouna mojiwo ireru</p>

    <!--投稿数・フォロワー数・フォロー数-->
    <ul>
    <li><span class="profile-stat-count">''' + str(dbrw.num_of_posts(username)) +'''</span> posts</li>
    </ul>
    </div>
    </div>
    </div>


    <!-- 自分の投稿 -->
    <div class="Mypost">
    <div class="row">
    <p class="h4">Mypost</p>

    <!-- iframe-->

    <div class="border border-0">
    <div class="embed-responsive embed-responsive-16by9">
    <iframe class="embed-responsive-item" src="./myposts.py" scrolling="auto" width="1300" height="900" seamless allowfullscreen></iframe>
    </div>
    </div>
    </div>
    </div>

    </div>

'''

print(maincontent)
hmd.htfooter()