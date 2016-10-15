#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import json

class DMM:
    def __init__(self, api_id, affiliate_id):
        self.baseurl = 'https://api.dmm.com/affiliate/v3'

        # required parameters
        self.api_id       = api_id
        self.affiliate_id = affiliate_id
        self.site         = 'DMM.R18'

    def search(self, keyword, hits=10, offset=1, sort='rank'):
        url = self.baseurl + '/itemList'

        params = {
            'api_id':       self.api_id,
            'affiliate_id': self.affiliate_id,
            'site':         self.site,
            'keyword':      keyword,
            'hits':         hits,
            'offset':       offset,
            'sort':         sort
        }

        return requests.get(url, params).json()

if __name__ == '__main__':
    import sys
    api_id = sys.argv[1]
    affiliate_id = sys.argv[2]
    query = sys.argv[3]

    dmm = DMM(api_id, affiliate_id)
    items = dmm.search(query, hits=16, offset=1, sort='date')

    for item in items['result']['items']:
        print(item['title'])
        print([genre['name'] for genre in item['iteminfo']['genre']])

