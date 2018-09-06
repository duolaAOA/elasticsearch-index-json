#!/usr/bin/env python3
# encoding=utf-8

import sys
import json
from urllib.parse import urlparse

import requests

STORIES_ONLY = True
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

def download_and_index_item():
    for item_id in download_topstories():

        url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(item_id)
        response = requests.get(url, headers=headers)
        item = json.loads(response.text)

        if 'kids' in item:
            item.pop('kids')

        if STORIES_ONLY and item['type'] != 'story':
            print("\nskiped item %s" % item['id'])
            return

        if not 'url' in item or not item['url']:
            item['url'] = "http://news.ycombinator.com/item?id={}".format(item['id'])
            item['domain'] = "news.ycombinator.com"
        else:
            u = urlparse(item['url'])
            item['domain'] = u.hostname.replace("www.", "") if u.hostname else ""

        # ES uses milliseconds
        item['time'] = int(item['time']) * 1000
        # from pprint import  pprint
        # pprint(item)

        es_url = "http://localhost:9200/{}/{}/{}".format(item['type'], item['type'], item['id'])
        response = requests.put(es_url, json=(item))
        # pprint(response.text)
        if not response.status_code in [200, 201]:
            print("\nfailed to add item %s" % item['id'])
        else:
            sys.stdout.write('.')
            sys.stdout.flush()


def download_topstories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    top100_ids = json.loads(requests.get(url=url, headers=headers).text)
    print("Got Top 100")

    return top100_ids



if __name__ == '__main__':
    print("Starting")
    download_and_index_item()
    print("over")