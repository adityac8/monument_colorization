## -*- coding: utf-8 -*-
#"""
#Created on Sat Jul 14 16:57:09 2018
#
#@author: adityac8
#"""
#
#import requests
#import mechanize
#from lxml import html
#import sys
#import urlparse
#import time
#
#def grab(website):
#    res=requests.get(website)
#    body=html.fromstring(res.text)
#
#    img = body.xpath('//img/@src')
#    print body
#    if not img:
#       raise Exception("No images found")
#
#    img = [urlparse.urljoin(res.url,url) for url in img]
#
#    print("Found {} images".format(len(img)))
#
#    for url in img:
#        r=requests.get(url)
#        f=open('images/%s'%url.split('/')[-1],'w')
#        f.write(r.content)
#        f.close()
#
#website='http://www.nmis.isti.cnr.it/falchi/pisaDataset/'
#links=[]
#br=mechanize.Browser()
#br.set_handle_robots(False)
#res=br.open(website)
#grab(website)

## imports 

import urllib2
import re
import os
from urlparse import urlsplit, urlparse
from posixpath import basename

## function that prcesses url, if there are any spaces it replaces with '%20' ##
def makeFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def process_url(raw_url):
    return raw_url[:-1].replace(' ','%20') if ' ' in raw_url[-1] else raw_url.replace(' ','%20')
 
def grab(url,directory):
    baseurl='http://www.nmis.isti.cnr.it/falchi/pisaDataset/'
    url=baseurl+url
    dirnam=basename(urlparse(url).path)
    urlcontent=urllib2.urlopen(url).read()
    imgurls=re.findall('img .*?src="(.*?)"',urlcontent)
    for imgurl in imgurls:
        try:
            imgurl=process_url(imgurl)
            imgdata=urllib2.urlopen(imgurl).read()
            filname=basename(urlsplit(imgurl)[2])
            output=open(directory+'/'+filname,'wb')
            output.write(imgdata)
            output.close()
            os.remove(dirnam)
        except:
            pass
        
urls=['Pisa-Basilica%20San%20Piero',
      'Pisa-Battistero',
      'Pisa-Campo%20Santo_Exterior',
      'Pisa-Campo%20Santo_Field',
      'Pisa-Campo%20Santo_Portico',
      'Pisa-Certosa',
      'Pisa-Chiesa%20della%20Spina',
      'Pisa-Duomo',
      'Pisa-Guelph%20Tower',
      'Pisa-Leaning%20Tower',
      'Pisa-Palazzo%20Carovana',
      'Pisa-Palazzo%20Orologio']

for i in range(len(urls)):
    makeFolder(str(i))
    grab(urls[i],str(i))
