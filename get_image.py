# -*- coding: utf-8 -*- 

import urllib
import urllib3
import os.path
import sys

def download(url):
  img = urllib.urlopen(url)
  localfile = open(os.path.basename(url), 'wb')
  localfile.write(img.read())
  img.close()
  localfile.close()

def get_url_root(url):
  if("http://" in url):
    url_delet_http = url.lstrip("http://")
    if("/" in url_delet_http):
      url_root = "http://" + url_delet_http[0:url_delet_http.find("/")]
      return url_root
  elif("https://" in url):
    url_delet_http = url.lstrip("https://")
    if("/" in url_delet_http):
      url_root = "http://" + url_delet_http[0:url_delet_http.find("/")]
      return url_root
  return 0;
