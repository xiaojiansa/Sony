import SonyCommand
import CameraModel
import requests
import datetime
import threading


class TakePicture:
    def __init__(self):
        self.model = CameraModel.CameraModel()  # 临时用
        self.sony_command = SonyCommand.SonyCommand(self.model)

    def take_picture(self):
        take_picture_thread = threading.Thread(target=self.take_picture_do)
        take_picture_thread.start()

    def take_picture_do(self):
        self.sony_command.sony_command("actTakePicture")
        img_url = self.sony_command.model.get_picture_url()
        req = requests.get(img_url)
        buf = req.content
        filename = 'D:/imges/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '.jpg'
        f = open(filename, 'wb')
        f.write(buf)
