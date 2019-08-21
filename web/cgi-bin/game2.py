#!/usr/bin/env python3

import cgi

# ヘッダの出力
print("Content-Type: text/html")
print("")

# 送信されたフォームデータを取得する
form = cgi.FieldStorage()

# フォームにv1にv2のデータが含まれるか
if (not 'v1' in form) or (not 'v2' in form):
    # 含まれないのでフォームを表示
    print("""
        <form>
        <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        </head>
        <h1>足して58になるように計算せよ</h1>
        <input type="text" name="v1">+
        <input type="text" name="v2">
        <input type="submit" value="計算">
        </form>
    """)
else:
    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")
    try:
        a1 = int(v1) + int(v2)
    except:
        a1 = 0
    if a1 == 58:
        print("<h1>True</h1>")
    else:
        print("<h1>", "False", a1, "</h1>")
