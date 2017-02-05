#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, json

meta_en = {
    'author': 'author',
    'composer': 'composer',
    'time_sig': 'time signature',
    'key_sig': 'key signature',
    'pitch': 'pitch',
    'meter': 'meter',
    'topic': 'topic',
    'tune': 'tune',
    'copyright': 'Copyright'
}

meta_en_graces = {
    'author': 'author',
    'composer': 'composer',
    'time_sig': 'time signature',
    'key_sig': 'key signature',
    'pitch': 'pitch',
    'meter': 'meter',
    'topic': 'topic',
    'tune': 'tune',
    'tune_from_en': 'tune from Hymns Old and New 1987',
    'copyright': 'Copyright'
}

meta_es = {
    'author': 'autor',
    'composer': 'compositor',
    'time_sig': 'signatura de compás',
    'key_sig': 'armadura de clave',
    'pitch': 'tono',
    'meter': 'metro',
    'number_in_himnos_1979': 'número en Himnos 1979',
    'number_in_english': 'número en inglés (Hymns Old and New 1987)',
    'topic': 'topic',
    'tune': 'tune',
    'copyright': 'Copyright'
}

meta_de = {
    'author': 'author',
    'composer': 'composer',
    'time_sig': 'time signature',
    'key_sig': 'key signature',
    'pitch': 'pitch',
    'meter': 'Versmaß',
    'alt_meter': 'Versmaß2',
    'topic': 'topic',
    'tune': 'tune',
    'copyright': 'Copyright'
}

def parse_metadata(metadata, translation):
    result = dict()
    for key, value in translation.items():
        try:
            search = re.search(re.escape(value) + r'→ (.*)', metadata, flags=re.MULTILINE).group(1)
            result[key] = search
        except:
            None

    return result

f = open('hymn_data/de.txt', 'r')
hymns = re.split(r'\n\x0c\n', f.read(), flags=re.MULTILINE)
hymns_list = []

for hymn in hymns:
    m = re.match(r'^(\d+): (.*)\n\n(1\..*)\n\n(.*)', hymn, flags=re.DOTALL)
    temp_hymn = list(m.groups())
    temp_hymn[3] = parse_metadata(temp_hymn[3], meta_de)

    hymn_dict = {
    'number': temp_hymn[0],
    'title': temp_hymn[1],
    'text': temp_hymn[2]
    }

    hymn_dict.update(temp_hymn[3])
    hymns_list.append(hymn_dict)

print json.dumps(hymns_list, sort_keys=True)
