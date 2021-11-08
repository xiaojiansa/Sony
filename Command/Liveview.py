import json
import requests
import SendPost


js_startLiveview = {
    "method": "startLiveview",
    "params": [],
    "id": 1,
    "version": "1.0"}

js_stopLiveview = {
    "method": "stopLiveview",
    "params": [],
    "id": 1,
    "version": "1.0"}


def start_live_view():
    try:
        r = None
        r = requests.post("http://192.168.122.1:10000/sony/camera", json.dumps(js_startLiveview))
        print('startLiveview\n', json.loads(r.content))
        # print(json.loads(r.content)["result"][0])
        p = None
        p = requests.get(json.loads(r.content)["result"][0], stream=True)
        i = 0
        while True:
            i = i + 1
            print(p.raw.read(12))
            temp = p.raw.read(3)
            temp = int.from_bytes(temp, 'big')
            print(temp)
            p.raw.read(121)
            picture_byte = p.raw.read(temp)
            filename = 'D:/imges/' + '%d' % i + '.jpg'
            f = open(filename, 'wb')
            f.write(picture_byte)

        # temp = p.raw.read(2)

        # if(temp == '\xFF\x01'):
        #     print("OK")
    except:
        print("Something wrong here")


def end_live_view():


if __name__ == '__main__':
    start_live_view()