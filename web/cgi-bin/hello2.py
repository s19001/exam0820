#!/usr/bin/env python3
# 挨拶

import cgi

print("Content-Type: text/html")
print("")

aisatu = ["hello", "howdy", "gday", "bonjour", "guten tag"]

form = cgi.FieldStorage()

if (not 'n' in form):
    print("""
        <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        </head>
        <body>
        <form>
        <h1>世界の挨拶</h1>
        <p>0, アメリカ</p>
        <p>1, アメリカ２</p>
        <p>2, オーストラリア</p>
        <p>3, フランス</p>
        <p>4, ドイツ</p>
        <input type="text" name="n">
        <input type="submit" value="挨拶">
        </form>
        </body>
    """)
else:
    n = form.getvalue("n", "0")
    hello = aisatu[int(n)]
    print("<h1>", hello, "</h1>")

