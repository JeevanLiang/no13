# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 02:28:05 2018

@author: msi-pc
"""
import http.client, urllib.parse, json, uuid
kbhost ="no13.azurewebsites.net"
endpoint_key = "e0238c17-abed-4970-85e5-12115d07b73e"
kb = "c5a268aa-e90c-41f0-8a37-967f765b3623"
method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"

transubscriptionKey = 'fc681557a2714baaaaa91ebc87346e1b'
tranhost = 'api.cognitive.microsofttranslator.com'
tranpath = '/translate?api-version=3.0'


def pretty_print (content):
    return json.loads(content)

def get_answers (path, content):
    try:
        headers = {
                'Authorization': 'EndpointKey ' + endpoint_key,
                'Content-Type': 'application/json',
                'Content-Length': len (content)
                }
        conn = http.client.HTTPSConnection(kbhost)
        conn.request ("POST", path, content, headers)
        response = conn.getresponse ()
        return response.read ()
    except:
        print('information error')


def translate (content,params):
    headers = {
        'Ocp-Apim-Subscription-Key': transubscriptionKey,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    conn = http.client.HTTPSConnection(tranhost)
    conn.request ("POST", tranpath + params, content, headers)
    response = conn.getresponse ()
    return response.read ()


def to_ch(text):
    try :
        requestBody = [{'Text' : text}]
        params="&to=zh-Hans"
        content = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')
        result = translate (content,params)
        output = json.dumps(json.loads(result), indent=4, ensure_ascii=False)
        dic_output=json.loads(output)
        return dic_output[0]["translations"][0]["text"]
    except:
        print('information error')


def findlist_in_kb(keyword):
    try:
        question = {'question': keyword,}
        content = json.dumps(question)
        result = get_answers (method, content)
        return pretty_print(result)["answers"][0]["answer"].split('-')
    except:
        print('infomation error')


def details_kb(que):
    try:
        question = {'question': que,}
        content = json.dumps(question)
        result = get_answers (method, content)
        return pretty_print(result)["answers"][0]["answer"]
    except:
        print('infomation error')

def main():
    print('Enter your keyword:')
    keyword=input()
    while keyword != 'exit':
        lists=findlist_in_kb(keyword)
        details={}
        i=0
        for que in lists:
            details[str(i)]=details_kb(que)
            print("#"*50)
            print(to_ch(que))
            print('----------')
            print(to_ch(details[str(i)]))
            print("#"*50)
            print("\n\n")
            i+=1
        print('Enter your keyword:')
        keyword=input()
    


if __name__=='__main__':
    main()