import json
import sys
import socket
import requests

#对焦模式
def FocusMode():
    js_setFocusMode = {
         "method": "setFocusMode",
         "params": ["MF"],
         "id": 1,
         "version": "1.0" }

    js_getFocusMode = {
         "method": "getFocusMode",
         "params": [],
         "id": 1,
         "version": "1.0" }

    js_getSupportedFocusMode = {
         "method": "getSupportedFocusMode",
         "params": [],
         "id": 1,
         "version": "1.0" }

    js_getAvailableFocusMode = {
         "method": "getAvailableFocusMode",
         "params": [],
         "id": 1,
         "version": "1.0" }

    try:
        r = None
        r = requests.post("http://192.168.122.1:10000/sony/camera", json.dumps(js_getSupportedFocusMode))
        print('getSupportedFocusMode\n', json.loads(r.content))

    except:
        print("Something wrong here")


if __name__ == '__main__':
    FocusMode()