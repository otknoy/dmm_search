#!/usr/bin/env python
from urllib.parse import urljoin
import requests


class DMM:
    def __init__(self, api_id, affiliate_id):
        self.base_url = 'https://api.dmm.com/affiliate/v3/'

        # required parameters
        self.api_id = api_id
        self.affiliate_id = affiliate_id
        self.site = 'DMM.R18'

    def __get(self, endpoint, params):
        url = urljoin(self.base_url, endpoint)
        return requests.get(url, params=params).json()

    def itemList(self, **params):
        params['api_id'] = self.api_id
        params['affiliate_id'] = self.affiliate_id

        params['site'] = 'DMM.R18'

        return self.__get('itemList', params)

    def floorList():
        pass

    def actressSearch():
        pass

    def genreSearch():
        pass

    def makerSearch():
        pass

    def seriesSearch():
        pass

    def authorSearch():
        pass

if __name__ == '__main__':
    import sys
    api_id = sys.argv[1]
    affiliate_id = sys.argv[2]
    query = sys.argv[3]

    dmm = DMM(api_id, affiliate_id)
    items = dmm.itemList(keyword=query, hits=16, offset=1, sort='date')

    for item in items['result']['items']:
        print(item['title'])
        print([genre['name'] for genre in item['iteminfo']['genre']])
