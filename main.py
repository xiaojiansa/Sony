# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import CameraModel
import SonyCommand
import TakePicture
import VideoPlayer
import ModelInit
import GetXml


from sony_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel

import threading
from queue import Queue


class QtWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = CameraModel.CameraModel()  # 初始化相机模型
        self.sony_command = SonyCommand.SonyCommand(self.model)  # 初始化命令对象

        # self.ui.pushButton.clicked.connect(self.video_player)  # evf开始按钮
        self.ui.pushButton.clicked.connect(self.take_picture)  # 拍照按钮

        self.ui.comboBox.currentTextChanged.connect(self.combo_set_f_number)  # 以下三个都是combo的connect
        self.ui.comboBox_2.currentTextChanged.connect(self.combo_set_iso_speed)
        self.ui.comboBox_3.currentTextChanged.connect(self.combo_set_shutter_speed)

        ModelInit.model_init(self.sony_command)  # model初始化

        self.ui.comboBox.addItems(self.model.get_f_number_desc())  # 以下三个都是ui显示
        self.ui.comboBox_2.addItems(self.model.get_iso_speed_desc())
        self.ui.comboBox_3.addItems(self.model.get_shutter_speed_desc())
        self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findText("2.8"))  # 以下三个都是ui初始化
        self.ui.comboBox_2.setCurrentIndex(self.ui.comboBox_2.findText("AUTO"))
        self.ui.comboBox_3.setCurrentIndex(self.ui.comboBox_3.findText("BULB"))

        # self.open_evf = True  # evf开启标志符
        self.picture_queue = Queue(maxsize=3)  # 存放图片的队列 最大容量三个 跨线程使用

    def combo_set_f_number(self, set_value):  # 槽函数
        set_value = ["%s" % set_value]
        self.sony_command.sony_command("setFNumber", set_value)

    def combo_set_iso_speed(self, set_value):  # 槽函数
        set_value = ["%s" % set_value]
        self.sony_command.sony_command("setIsoSpeedRate", set_value)

    def combo_set_shutter_speed(self, set_value):  # 槽函数
        set_value = ["%s" % set_value]
        self.sony_command.sony_command("setIsoSpeedRate", set_value)

    def take_picture(self):  # 槽函数 拍照
        TakePicture.TakePicture().take_picture()

    def video_get(self):  # 从队列获取图片并显示到ui上  B线程函数
        while True:
            picture_byte = self.picture_queue.get()
            img = QImage()
            img.loadFromData(picture_byte)
            w = self.ui.label_4
            w.setPixmap(QPixmap.fromImage(img))
            # w.show()
            # cv2.waitKey(50)


if __name__ == '__main__':
    # 打开wifi，连接相机

    # 测试连接
    for i in range(0, 3):
        if GetXml.get_xml() is False:
            print("连接失败，请重新连接！")
    # 相机初始化、显示ui
    app = QtWidgets.QApplication(sys.argv)
    window = QtWindow()
    window.show()
    # 开启evf，存入队列
    video_player = VideoPlayer.VideoPlayer(window.picture_queue)
    video_thread = threading.Thread(target=video_player.video_player)
    video_thread.setDaemon(True)  # 线程守护
    video_thread.start()
    # 显示evf，队列取出
    get_thread = threading.Thread(target=window.video_get)
    get_thread.setDaemon(True)  # 线程守护
    get_thread.start()
    sys.exit(app.exec_())










