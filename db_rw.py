import csv
import datetime
import pandas as pd
from os import write
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

def nowtime():
    dt_now = datetime.datetime.now()
    now = str(dt_now.hour) + ":" + str(dt_now.minute) + ":" + str(dt_now.second)
    return now

# ユーザーネームごとにcsv形式のデータベースを作成する
def makedb(name="test"):

    global USER_ID

    filename = "./db/" + name + ".csv"
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

    filename = "./db/" + db_name + ".csv"

    reload_user_id()
    if db_name in USER_ID:
        pass
    else:
        return 0
   
    with open(filename, 'a+', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(postdata)
        f.close()

#HTMLフォーマットで表現する
def to_html_format(name, data):

    buff_data = str(data.values)

    print(buff_data)

    for i in range(len(buff_data)):
        time = data[i][0]
        post = data[i][1]

        print('<dl class="row">')

        print('<dt class="col-sm-3">', name, "</dt>")
        print('<dt class="col-sm-1">', time, "</dt>")
        print('<dt class="col-sm-8">', post, "</dt>")
    
    print("</dl>")


# 投稿データを読み出す
def readdb(db_name, UUID=None, mode=1):     #mode = 1 指定されたpostのみ mode = 2 全部

    filename = "./db/" + db_name + ".csv"

    data = pd.read_csv(filename)

    if UUID == None:
        #rdata = to_html_format(db_name, data)
        return data
    else:
        return data[data["UUID"] == UUID]
    





def main():
    makedb("test")
    tweet = ["test", "EARTH IS BLUE"]

    makedb("test2")


    writedb(["test2", "MOON IS BRIGHT"])
    writedb(tweet)

    #uuid = "a7aedd3b"

    post = readdb("test")
    print(post, type(post))
    #to_html_format("test", post)


if __name__ == "__main__":
    main()