import json
import sys
import socket
import requests
from Camera import CameraModel
import ErrorTable

CameraHost = "http://192.168.122.1:10000/sony/camera"

js_setCameraFunction_Transfer = {
    "id": 1,
    "method": "Contents Transfer",
    "params": [
        "Remote Shooting"
    ],
    "version": "1.0"
}


def get_property(model, command_js):
    try:
        r = None
        r = requests.post(CameraHost, json.dumps(command_js))
        camera_response = json.loads(r.content)
        if "error" in camera_response:
            return {"error": ErrorTable.err_table(camera_response["error"][0])}
        else:
            if command_js["method"] == "getFNumber":
                model.set_f_number(camera_response["result"][0])
            if command_js["method"] == "getIsoSpeedRate":
                model.set_iso_speed(camera_response["result"][0])
            if command_js["method"] == "getShutterSpeed":
                model.set_shutter_speed(camera_response["result"][0])
            # if command_js["method"] == "actTakePicture":
            #     print(camera_response["result"])
            #     model.set_shutter_speed(camera_response["result"][0])
            return {"result": "ok"}
    except:
        return {"link_error": "lost link"}


def get_property_desc(model, command_js):
    try:
        r = None
        r = requests.post(CameraHost, json.dumps(command_js))
        camera_response = json.loads(r.content)
        if "error" in camera_response:
            return {"error": ErrorTable.err_table(camera_response["error"][0])}
        else:
            if command_js["method"] == "getAvailableFNumber":
                model.set_f_number_desc(camera_response["result"][1])
            if command_js["method"] == "getAvailableIsoSpeedRate":
                model.set_iso_speed_desc(camera_response["result"][1])
            if command_js["method"] == "getAvailableShutterSpeed":
                model.set_shutter_speed_desc(camera_response["result"][1])
            return {"result": "ok"}
    except:
        print("Something wrong here")


def set_property(command_js):
    try:
        r = None
        r = requests.post(CameraHost, json.dumps(command_js))
        camera_response = json.loads(r.content)
        if "error" in camera_response:
            return {"error": ErrorTable.err_table(camera_response["error"][0])}
        else:
            return {"result": "ok"}
    except:
        print("Something wrong here")


def take_picture(command_js):
    try:
        r = None
        r = requests.post(CameraHost, json.dumps(command_js))
        camera_response = json.loads(r.content)
        if "error" in camera_response:
            return {"error": ErrorTable.err_table(camera_response["error"][0])}
        else:
            return camera_response
    except:
        print("Something wrong here")


if __name__ == '__main__':
    get_property(js_setCameraFunction_Transfer)
