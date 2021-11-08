import os
import datetime
import urllib.request
import SendPost

js_actHalfPressShutter = {
            "method": "actHalfPressShutter",
            "params": [],
            "id": 1,
            "version": "1.0"}

js_cancelHalfPressShutter = {
    "method": "cancelHalfPressShutter",
    "params": [],
    "id": 1,
    "version": "1.0"}

js_actTkPhoto = {
    "method": "actTakePicture",
    "params": [],
    "id": 1,
    "version": "1.0"
}

#创建目录，并返回该目录
def make_dir(path):
    #去除左右两边的空格
    path = path.strip()
    #判断该文件是否存在，不存在才创建，存在则跳过
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def save_img(path,imglist):
    filename = path + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '.jpg'
    f = open(filename,'wb')
    req = urllib.request.urlopen(imglist)
    buf = req.read()
    f.write(buf)


def take_picture():
    command_result = {"default": "worry"}
    SendPost.take_picture(js_actHalfPressShutter)
    command_result = SendPost.take_picture(js_actTkPhoto)
    SendPost.take_picture(js_cancelHalfPressShutter)

    # imgurl = command_result["result"][0][0]

    # save_img_path = 'D:/imges/' #存储
    # path = make_dir(save_img_path)
    # save_img(save_img_path, imgurl)
    # except:
    #     print("Something wrong here")
    print(command_result["result"][0][0])
    return command_result


if __name__ == '__main__':
    take_picture()