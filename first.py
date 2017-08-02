#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import json
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

request = urllib2.Request("http://www.iwencai.com/stockpick/cache?token=80fb69160133b88dc8eac0a9ab7892da&p=2&perpage=10&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]")
response = urllib2.urlopen(request)
source_code = response.read()
arr = json.loads(source_code)
final_json = json.dumps(arr, sort_keys=True, indent=4, ensure_ascii=False)

print type(source_code)
print source_code
print source_code.decode("unicode-escape")
print arr
print final_json
exit()

plain_text = str(source_code)

myClassReBuild = json.loads(plain_text)

myClassReBuild2 = str(myClassReBuild["result"]).decode("unicode-escape")
file1 = open("./1.txt", "w")
file1.write(plain_text)
file1.close()
