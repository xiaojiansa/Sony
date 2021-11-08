import json
import sys
import socket
import requests


def getMethodTypes():


#
    js_getMethodTypes = {
        "method": "getMethodTypes",
        "params": ["1.0"],
        "id": 1,
        "version": "1.0"}

    js_getVersions = {
     "method": "getVersions",
     "params": [],
     "id": 1,
     "version": "1.1" }



    try:
        r = None
        r = requests.post("http://192.168.122.1:10000/sony/avContent", json.dumps(js_getMethodTypes))
        print('getVersions\n', json.loads(r.content))

    except:
        print("Something wrong here")


if __name__ == '__main__':
    getMethodTypes()