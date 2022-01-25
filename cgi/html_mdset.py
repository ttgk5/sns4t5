
from pandas import concat


def htheader():
    print("<head>")
    print('<meta charset="Shift_JIS">')
    print("<title>SNS for T5</title>")
    print('<meta name="viewport" content="width=device-width, initial-scale=1">')
    print('<link rel="stylesheet" href="../css/bootstrap.css">')
    print('<script type="text/javascript" src="../js/jquery-3.6.0.js"></script>')
    print('<script type="text/javascript" src="../js/bootstrap.js"></script>')
    print('</head>')

def htnavibar():
    content = '''
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
        <a class="navbar-brand" href="index.html">
        <img src="/gazou/T5-removebg-preview.png" alt="t5sns" width="70" height="70">
        </a>


        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#t5nav" aria-controls="t5nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-start" id="t5nav">
        <ul class="navbar-nav mr-auto">
        <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="mypage.py">My Page</a>
        </li>
        </ul>
        </div>
        <div class="collapse navbar-collapse navbar-light" id="t5nav">
        <ul class="navbar-nav">
        <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="../login.html">log in</a>
        </li>
        </ul>
        </div>
        <div class="collapse navbar-collapse navbar-light" id="t5nav">
        <ul class="navbar-nav">
        <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="logout.py">log out</a>
        </li>
        </ul>
        </div>
        <div class="collapse navbar-collapse navbar-light" id="t5nav">
        <ul class="navbar-nav">
        <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="../touroku.html">登録</a>
        </li>
        </ul>
        </div>
        <script>
        // 連想配列に格納
        function getCookieArray(){
        var arr = new Array();
        if(document.cookie != ''){
        var tmp = document.cookie.split('; ');
        for(var i=0;i<tmp.length;i++){
        var data = tmp[i].split('=');
        arr[data[0]] = decodeURIComponent(data[1]);
        }
        }
        return arr;
        }

        // keyを指定して取得
        // 「 key1=val1; key2=val2; key3=val3; ・・・ 」というCookie情報が保存されているとする
        var arr = getCookieArray();
        var value = arr['LOGINNAME'];
        // key1の値：val1
        document.write("hello ", value, "!")
        </script>


        </div>
        </nav>           
    '''
    print(content)
                  
def htjumbo_s():
    print('<div class="container"><div class="bg-light p-3 p-sm-5 my-4 rounded"><div class="text-center">')

def htjumbo_e():
    print('</div></div></div>')

def htfooter():
    content = '''
            <!--フッター-->
            <div class="container-fulid">

            <footer class="background-color:lightslategray text-center">

            <!-- Copyright -->
            <div class="text-center p-3" style="background-color:lightslategray;">
            <span class="text-muted"> t5sns</span>
            </div>
            </div>
            </footer>

            </body>

            </html>
    
    '''
    print(content)