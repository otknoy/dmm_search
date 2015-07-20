#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import time
from xml.etree import ElementTree

class DMM:
    def __init__(self, api_id, affiliate_id):
        self.baseurl = 'http://affiliate-api.dmm.com'

        self.params                 = {}
        self.params['api_id']       = api_id
        self.params['affiliate_id'] = affiliate_id

        self.params['operation'] = 'ItemList'
        self.params['version']   = '2.00'
        self.params['site']      = 'DMM.co.jp'
        self.params['service']   = 'digital'
        self.params['floor']     = 'videoa'

    def search(self, keyword, hits=10, offset=1, sort='rank'):
        self.params['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.params['keyword']   = keyword.encode('euc-jp')
        self.params['hits']      = hits
        self.params['offset']    = offset
        self.params['sort']      = sort

        url = self.baseurl + '/?' + urllib.parse.urlencode(self.params)
        xml = urllib.request.urlopen(url).read().decode('euc-jp')
        return self._parse_xml(xml)

    def _remove_first_line(self, text):
        lines = text.split("\n")
        return "\n".join(lines[1:])

    def _parse_xml(self, xml):
        root_elem = ElementTree.fromstring(xml)
        elems = root_elem.findall('.//item')

        items = []
        for  e in elems:
            item = {}
            item['content_id']    = e.find('content_id').text
            item['title']         = e.find('title').text
            item['url']           = e.find('URL').text
            item['affiliate_url'] = e.find('affiliateURL').text
            item['image_url']     = e.find('imageURL/small').text
            item['price']         = e.find('prices/price').text
            item['date']          = e.find('date').text
            item['keywords']      = [k.text for k in e.findall('iteminfo/keyword/name')]
            item['actresses']     = [k.text for k in e.findall('iteminfo/actress/name')][0:-1:3]

            items.append(item)

        return items


if __name__ == '__main__':
    import sys
    api_id = sys.argv[1]
    affiliate_id = sys.argv[2]
    query = sys.argv[3]

    dmm = DMM(api_id, affiliate_id)
    items = dmm.search(query, hits=5, offset=1, sort='date')

    for item in items:
        print(item)

