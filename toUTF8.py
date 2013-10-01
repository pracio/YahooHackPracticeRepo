#-*- coding:utf8 -*-
import json
import sys
import collections
import codecs

# def convert(data):
#     if isinstance(data, basestring):
#         return data.decode('unicode-escape')
#     elif isinstance(data, collections.Mapping):
#         return dict(map(convert, data.iteritems()))
#     elif isinstance(data, collections.Iterable):
#         return type(data)(map(convert, data))
#     else:
#         return data

# data = ""

with codecs.open(sys.argv[1],'r') as r:
    data = r.read()
    data = json.loads(data)
    age = data["result"]["records"][0]["Age"]
    print age==u'成年'