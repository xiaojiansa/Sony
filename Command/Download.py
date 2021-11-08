import json
import sys
import socket
import requests
import SendPost

js_setCameraFunction_Transfer = {
    "id": 1,
    "method": "Contents Transfer",
    "params": [
        "Remote Shooting"
    ],
    "version": "1.0"
}


def Download():

    js_getStorageInformation = {
         "id": 1,
         "method": "getStorageInformation",
         "params": [],
         "version": "1.0"
        }

    js_setCameraFunction_Transfer = {
        "id": 1,
        "method": "Contents Transfer",
        "params": [
            "Remote Shooting"
        ],
        "version": "1.0"
    }

    js_setCameraFunction_Remote = {
        "id": 1,
        "method": "Remote Shooting",
        "params": [
            "Remote Shooting"
        ],
        "version": "1.0"
    }

    js_getContentCount = {
        "method": "getContentCount",
        "params": [
            {
                "uri": "storage:memoryCard1",
                "target": "all",
                "view": "date"
            }
        ],
        "id": 1,
        "version": "1.2"
    }

    js_getSchemeList = {
        "id": 1,
        "method": "getSchemeList",
        "params": [],
        "version": "1.0"
    }

    try:
        r = None
        # r = requests.post("http://192.168.122.1:10000/sony/camera", json.dumps(js_setCameraFunction_Transfer))
        # print('getStorageInformation\n', json.loads(r.content))

        r = requests.post("http://192.168.122.1:10000/sony/camera", json.dumps(js_getSchemeList))
        print('getSchemeList\n', json.loads(r.content))

    except:
        print("Something wrong here")


if __name__ == '__main__':
    SendPost.get_property(js_setCameraFunction_Transfer)
