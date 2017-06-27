# !/usr/bin/python
# -*- coding: utf-8 -*-# __user__

import urllib.request
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Chrome/51.0.2704 (Windows NT 10.0; Win64; x64)'
headers = {'User-Agent': user_agent}
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    pattern = re.compile('<div class="author clearfix">.*?<a.*?<img.*?<h2>(.*?)</h2>'
                         + '.*?<div class="articleGender (.*?)Icon">'
                         + '.*?</a>.*?<div class="content">.*?<span>(.*?)</span>'
                         + '.*?</div>(.*?)<i class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        if item[2] == "woman":
            sex = "女"
        else:
            sex = "男"
        haveImg = re.search("img", item[3])
        if not haveImg:
            print("用户名："+item[0]+"(%s)" % sex, "\n发表内容："+item[2], "\n好笑数："+item[4]+"\n")
except urllib.request.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)