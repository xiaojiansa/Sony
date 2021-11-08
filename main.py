# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import socket

# from Command import FocusMode
# from Command import Liveview

from Camera import CameraModel
from Command import FNumber
from Command import IsoSpeed
from Command import ShutterSpeed
from Command import TakePicture


if __name__ == '__main__':
#打开wifi，连接相机

    model = CameraModel.Model()
#相机model初始化，三个属性赋值到model
    # print(FNumber.f_number(model, "getFNumber"))
    # print(model.get_f_number())
    # print(IsoSpeed.iso_speed_rate(model, "getIsoSpeedRate"))
    # print(model.get_iso_speed())
    # print(ShutterSpeed.shutter_speed(model, "getShutterSpeed"))
    # print(model.get_shutter_speed())
    #
    print(FNumber.f_number(model, "getAvailableFNumber"))
    print(model.get_f_number_desc())
    print(IsoSpeed.iso_speed_rate(model, "getAvailableIsoSpeedRate"))
    print(model.get_iso_speed_desc())
    print(ShutterSpeed.shutter_speed(model, "getAvailableShutterSpeed"))
    print(model.get_shutter_speed_desc())

#相机参数设置
    # temp = 4.5
    # temp_1 = ["%s" % temp]
    # print(FNumber.f_number_set("setFNumber", temp))
    # print(IsoSpeed.iso_speed_rate_set("setIsoSpeedRate", temp_2))
    # print(ShutterSpeed.shutter_speed_set("setShutterSpeed", temp_3))


#按钮：拍照
    TakePicture.take_picture()


#按钮：开始evf





