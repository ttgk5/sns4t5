# -*- coding: utf-8 -*-

import csv
import datetime
import pandas as pd
import os
from os import write
from os import makedirs

import uuid

#ユーザーID読み込み

USER_ID = []

def reload_user_id():
    global USER_ID

    USER_ID = []
    with open("./db/USER_ID.csv") as r:
        USER_ID_buf = r.readlines()

        for x in USER_ID_buf:
            USER_ID.append(x.replace("\n", ""))
        
        #print(USER_ID, len(USER_ID), type(USER_ID))
        r.close()

def load_ff(username):

    FF = []
    filename = "./db/" + username + "/follow.csv"

    with open(filename) as r:
        FF_buf = r.readlines()

        for x in FF_buf:
            FF.append(x.replace("\n", ""))
        
        #print(USER_ID, len(USER_ID), type(USER_ID))
        r.close()
    return FF

def nowtime():
    dt_now = datetime.datetime.now()
    now = str(dt_now.hour) + ":" + str(dt_now.minute) + ":" + str(dt_now.second)
    return now

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# ユーザーネームごとにcsv形式のデータベースを作成する
def makedb(name="test"):

    global USER_ID

    dirpass = "./db/" + name + "/"
    my_makedirs(dirpass)

    filename = "./db/" + name + "/post.csv"
    fst_row = ["UUID", "DATE", "POST"]

    reload_user_id()
    if name in USER_ID:
        pass
    else:
        with open("./db/USER_ID.csv", "a+", newline="") as fb:
            writer = csv.writer(fb)
            writer.writerow([name])
            fb.close()

        with open(filename, 'a+', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(fst_row)
            f.close()

# 投稿データをデータベースに書き込む 
def writedb(postdata):
    date = nowtime()

    db_name = postdata[0]
    postdata.pop(0)
    postdata.insert(0, str(uuid.uuid4())[:8])
    postdata.insert(1, date)

    filename = "./db/" + db_name + "/post.csv"

    reload_user_id()
    if db_name in USER_ID:
        pass
    else:
        return 0
   
    with open(filename, 'a+', newline="", encoding="Shift_JIS") as f:
        writer = csv.writer(f)
        writer.writerow(postdata)
        f.close()

#HTMLフォーマットで表現する
def to_html_format(name, dfdata):

    buff_data = dfdata.values.tolist()

    #print(buff_data)

    print('<dl class="row">')
    for i in range(len(buff_data)):
        time = buff_data[i][1]
        post = buff_data[i][2]

        

        print('<dt class="col-sm-3">', name, "</dt>")
        print('<dd class="col-sm-1">', time, "</dd>")
        print('<dd class="col-sm-8">', post, "</dd>")
    
    print("</dl>")


# 投稿データを読み出す
def readdb(db_name, UUID=None, mode=1):     #mode = 1 指定されたpostのみ mode = 2 全部

    filename = "./db/" + db_name + "/post.csv"

    data = pd.read_csv(filename, encoding="Shift_JIS")

    if UUID == None:
        rdata = to_html_format(db_name, data)
        return rdata
    else:
        return data[data["UUID"] == UUID]

# タイムライン作成関数
def maketimeline(username):
    follow_list = load_ff(username)
    timeline = []

    for i in follow_list:
        timeline.append(readdb(i))

# FF管理関数 apd:追加 del:削除
def manage_ff(db_name, fname, mode="apd"):

    filename = "./db/" + db_name + "/follow.csv"

    if mode == "apd":
        reload_user_id()
        if fname in USER_ID:
            with open(filename, 'a+', newline="", encoding="Shift_JIS") as f:
                writer = csv.writer(f)
                writer.writerow([fname])
                f.close()
        else:
            return -1
    
    if mode == "del":
        cnt = 0
        ff = load_ff(db_name)

        for x in ff:
            cnt += 1
            if x == fname:
                ff.pop(cnt - 1)
        
        os.remove(filename)
        with open(filename, 'a+', newline="", encoding="Shift_JIS") as f:
            writer = csv.writer(f)
            print(ff)
            writer.writerows([ff])
            f.close()


        

def main():
    makedb("test")
    tweet = ["test", "EARTH IS BLUE"]

    makedb("test2")
    manage_ff("test5", "test")
    manage_ff("test5", "test2")


    writedb(["test2", "MOON IS BRIGHT"])
    writedb(tweet)

    #uuid = "a7aedd3b"

    #post = readdb("test")
    #print(post, type(post))

    makedb("test5")
    #manage_ff("test", "test2")
    manage_ff("test", "test5", "apd")
    #to_html_format("test", post)

    maketimeline("test5")


if __name__ == "__main__":
    main()