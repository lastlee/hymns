#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, json
from pprint import pprint

meta_se = {
    'title': 'Title',
    'author': 'Words',
    'composer': 'Music',
    'copyright': 'Copyright'
}

def parse_metadata(metadata, translation):
    result = dict()
    for key, value in translation.items():
        try:
            search = re.search(re.escape(value) + r': (.*)\n', metadata, flags=re.MULTILINE).group(1)
            result[key] = search
        except:
            None

    return result

f = open('hymn_data/se-test.txt', 'r')
hymns = re.split(r'===== No. ', f.read(), flags=re.MULTILINE)
hymns.pop(0)
hymns_list = []

for hymn in hymns:
    #print hymn
    m = re.match(r'^(\d*) =====(.*)\n\n\n(.*)', hymn, re.DOTALL)
    temp_hymn = list(m.groups())

    pprint(temp_hymn)

    #temp_hymn[1] = parse_metadata(temp_hymn[1], meta_se)

    hymn_dict = {
    'number': temp_hymn[0],
    'meta': temp_hymn[1]
    }

    #hymn_dict.update(temp_hymn[1])
    hymns_list.append(hymn_dict)

#print json.dumps(hymns_list, sort_keys=True)
