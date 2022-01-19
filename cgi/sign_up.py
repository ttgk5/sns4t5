#!/usr/bin/python3

import cgi
import cgitb
import random
import string
import db_rw as dbrw
import html_mdset as hmd
import makehash

#password 生成
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



#エラーをブラウザ上で見れるようにする
cgitb.enable()

# HTML is following
print("Content-Type: text/html")    
print("")

form = cgi.FieldStorage()
password = get_random_string(5)

hashedpw = makehash.make_hash(password)

dbrw.makedb(form["user_name"].value, hashedpw)

hmd.htheader()
hmd.htnavibar()

hmd.htjumbo_s()
print('<h1>あなたのパスワードは</h1>')
print('<h2>', password, '</h2>')
print('<p> メモしてください 再発行は不可能です </p>')