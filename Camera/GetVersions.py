import json
import sys
import socket
import requests


def getAvailableApiList():


#
    # js_getVersions = {
    #      "method": "getVersions",
    #      "params": [],
    #      "id": 1,
    #      "version": "1.0" }


    js_getAvailableApiList = {
         "method": "getAvailableApiList",
         "params": [],
         "id": 1,
         "version": "1.0" }



    try:
        r = None
        r = requests.post("http://192.168.122.1:10000/sony/camera", json.dumps(js_getAvailableApiList))
        print('getAvailableApiList\n', json.loads(r.content))

    except:
        print("Something wrong here")


if __name__ == '__main__':
    getAvailableApiList()