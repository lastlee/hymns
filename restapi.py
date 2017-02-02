#!flask/bin/python
# -*- coding: utf-8 -*-

import json
from flask import Flask, jsonify

app = Flask(__name__)

books = {
    'en': json.load(open('hymn_data/hon87.json', 'r')),
    'en_graces': json.load(open('hymn_data/en_graces.json', 'r')),
    'es': json.load(open('hymn_data/himnos16.json', 'r')),
    'de': json.load(open('hymn_data/de.json', 'r'))
}

def search_field(query, key, lang):
    hymns = books[lang]
    query = query.lower()

    for item in hymns:
        try:
            searchable_item = {
                'key': item[key].lower()
            }
        except:
            searchable_item = {
                'key': ''
            }
        if searchable_item['key'] == query:
            yield item

def search(query, lang):
    hymns = books[lang]
    query = query.lower()

    for item in hymns:
        if any(query in v.lower() for v in item.values()):
            yield item

def get_hymn(number, lang):
    hymns = books[lang]

    for item in hymns:
        if item['number'] == str(number):
            return item

def get_all_hymns(lang):
    return books[lang]

def get_hymn_with_key(number, lang, key=None):
    hymns = books[lang]

    for item in hymns:
        if item['number'] == str(number):
            return item[key]

@app.route('/v1.0/<lang>/search/<query>', methods=['GET'])
def handle_search(query, lang):
    return jsonify([hymn for hymn in search(query, lang)])

@app.route('/v1.0/<lang>/search-keys/<key>/<query>', methods=['GET'])
def handle_search_full(lang, key=None, query=None):
    return jsonify([hymn for hymn in search_field(query, key, lang)])

@app.route('/v1.0/<lang>/hymn/<int:number>', methods=['GET'])
def handle_hymn(number, lang):
    return jsonify(get_hymn(number, lang))

@app.route('/v1.0/<lang>/hymn/<int:number>/<key>', methods=['GET'])
def handle_hymn_with_key(number, lang, key=None):
    return jsonify(get_hymn_with_key(number, key, lang))

@app.route('/v1.0/<lang>/all', methods=['GET'])
def handle_get_all(lang):
    return jsonify(get_all_hymns(lang))

if __name__ == '__main__':
    app.run(debug=True)
