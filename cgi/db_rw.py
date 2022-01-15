# -*- coding: utf-8 -*-

import csv
import datetime
import pandas as pd
import os
from os import write
from os import makedirs
from datetime import datetime as dt, time

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

    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)


    dt_now = now.strftime('%Y/%m/%d %H:%M:%S')

    return dt_now

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# ユーザーネームごとにcsv形式のデータベースを作成する
def makedb(name="test"):

    global USER_ID

    dirpass = "./db/" + name + "/"
    my_makedirs(dirpass)

    postfilename = "./db/" + name + "/post.csv"
    followfilename = "./db/" + name + "/follow.csv"
    postdata_fst_row = ["UUID", "DATE", "POST"]


    reload_user_id()
    if name in USER_ID:
        pass
    else:
        with open("./db/USER_ID.csv", "a+", newline="") as fb:
            writer = csv.writer(fb)
            writer.writerow([name])
            fb.close()

        with open(postfilename, 'a+', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(postdata_fst_row)
            f.close()

        with open(followfilename, 'a+', newline="") as f:
            writer = csv.writer(f)
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
        name = serch_post(buff_data[i][0])[0]
        time = buff_data[i][1]
        post = buff_data[i][2]

        

        print('<dt class="col-sm-3">', name, "</dt>")
        print('<dd class="col-sm-1">', time, "</dd>")
        print('<dd class="col-sm-8">', post, "</dd>")
    
    print("</dl>")

def serch_post(UUID):
    reload_user_id()

    number_of_users = len(USER_ID)

    for i in USER_ID:
        result = readdb(i, UUID)
        #print(i)
        #print(result)
        if result.empty == False:
            post_author = i
            break
    
    return [post_author, result]



# 投稿データを読み出す
def readdb(db_name, UUID=None, mode=1):     #mode = 1 指定されたpostのみ mode = 2 全部

    filename = "./db/" + db_name + "/post.csv"

    data = pd.read_csv(filename, encoding="Shift_JIS")

    if UUID == None:
        #rdata = to_html_format(db_name, data)
        return data
    else:
        try:
            return data[data["UUID"] == UUID]
        except Exception:
            return -1

# タイムライン作成関数
def maketimeline(username, type="individual"):
    
    #print("loaded", follow_list)
    timeline = pd.DataFrame( columns=['UUID', 'DATE', 'POST'])
    #print(timeline)
    cnt = 0

    if type == "individual":
        follow_list = load_ff(username)
        for i in follow_list:
            timeline = pd.concat([timeline, readdb(i)])
            #print(timeline)
            #timeline[i,1] = dt.strptime(timeline[i,1], '%Y/%m/%d %H:%M:%S')
            cnt += 1

    if type == "showall" and username == None:
        reload_user_id()
        for i in USER_ID:
            timeline = pd.concat([timeline, readdb(i)])
            #print(timeline)
            #timeline[i,1] = dt.strptime(timeline[i,1], '%Y/%m/%d %H:%M:%S')
            cnt += 1
    
    timeline['DATE'] = pd.to_datetime(timeline['DATE'], infer_datetime_format= True)

    timeline.sort_values(by = 'DATE', ascending = False, inplace = True) 
    
    #print(timeline)

    to_html_format(username, timeline)

# FF管理関数 apd:追加 del:削除
def manage_ff(db_name, fname, mode="apd"):

    filename = "./db/" + db_name + "/follow.csv"

    if mode == "apd":
        reload_user_id()
        if fname in USER_ID:
            if fname not in load_ff(db_name):
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
    makedb("test5")
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
    print(load_ff("test"))

    print(serch_post("3bf01a41"))


if __name__ == "__main__":
    main()