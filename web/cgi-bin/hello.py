#!/usr/bin/env python3
# 挨拶

import random

print("Content-Type: text/html")
print("")

aisatu = ["hello", "howdy", "gday", "bonjour", "guten tag"]
hello = random.choice(aisatu)

print("""
    <html>
    <head><title>hello</title></head>
    <body>
        <h1>{oha}</h1>
    </body>
    </html>
    """.format(oha=hello))
