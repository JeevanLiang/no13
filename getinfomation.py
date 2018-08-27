# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 01:50:30 2018

@author: msi-pc
"""

import requests 
import json
url="https://no13-asrbbe6isgzxtim.search.windows.net/indexes/c5a268aa-e90c-41f0-8a37-967f765b3623/docs?api-version=2017-11-11&search=bottle"
response=requests.get(url)
print(response)