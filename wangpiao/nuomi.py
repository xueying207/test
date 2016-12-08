#!/usr/bin/python
#    -*- coding: utf8 -*-
import urllib
import httplib2
import sys
import re
import os
import time
class Download(object):

    def __init__(self, disableSSL=False):
        self.url = 'http://t66y.com/thread0806.php?fid=16&search=&page=%s'
        self.header = None
        self.http = httplib2.Http(disable_ssl_certificate_validation=disableSSL)
        self.status = ''
        self.values = None
        self.auth = False
        self.result = []
        self.download = []

    def getPageInfo(self, page='1'):
        self.result=[]
        self.header = {'Content-type': 'text/html'}
        response, content = self.http.request(self.url %page, 'GET', headers=self.header)
        data=content.decode('gbk', 'ignore').encode('utf-8', 'ignore')
        for x in data.splitlines():
            if x.strip().startswith('<h3>'):
                m = re.match(r'.*<h3><a href="(.*\.html)" target=.*">(.*)</a></h3>', x)
                if m:
                    #parse out font tag
                    q = re.match(r'.*<font.*>(.*)</font.*', m.group(2))
                    if q:
                        self.result.append([str(m.group(1)), q.group(1)])
                    else:
                        self.result.append([str(m.group(1)), m.group(2)])
        return self.result

    def getPic(self):
        if not os.path.isdir('pics'):
            os.mkdir('pics')

        for url, desc in self.download:
            self.url='http://t66y.com/%s' %url
            response, content = self.http.request(self.url, 'GET', headers=self.header)
            for x in content.split("type='image'"):
                x=x.strip()
                link=re.search(r"onclick.*open.*input src='(.*)'$", x)
                if not link:
                    continue
                target_dir=os.path.join('pics', desc)
                if not os.path.isdir(target_dir):
                    os.mkdir(target_dir)
                http=httplib2.Http()
                rr, cc = http.request(link.group(1), 'GET')
                filename = os.path.join( target_dir, link.group(1).split('/')[-1])
                if os.path.isfile(filename):
                    filename='.'.join(filename.split('.')[:-1])+'-'+str(time.time())+'-.'+filename.split('.')[-1]
                open(filename, 'wb').write(cc)
                print link.group(1), filename

    def searchTag(self):
        tags=['原创','外拍', 'P]']
        for url, desc in self.result:
            for tag in tags:
                if tag in desc:
                    self.download.append([url, desc])

if __name__=='__main__':
    for x in xrange(1, 20):
        try:
            test=Download()
            test.getPageInfo(str(x))
            test.searchTag()
            test.getPic()
        except:
            pass
