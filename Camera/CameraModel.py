import copy


class Model:
    def __init__(self):
        self.FNumber = 0
        self.IsoSpeed = 0
        self.ShutterSpeed = 0
        self.FNumberDesc = []
        self.IsoSpeedDesc = []
        self.ShutterSpeedDesc = []

    def set_f_number(self,FNumber):
        self.FNumber = FNumber

    def set_iso_speed(self,IsoSpeed):
        self.IsoSpeed = IsoSpeed

    def set_shutter_speed(self,ShutterSpeed):
        self.ShutterSpeed = ShutterSpeed

    def get_f_number(self):
        return self.FNumber

    def get_iso_speed(self):
        return self.IsoSpeed

    def get_shutter_speed(self):
        return self.ShutterSpeed

#Desc
    def set_f_number_desc(self,FNumberDesc):
        self.FNumberDesc = FNumberDesc[:]

    def set_iso_speed_desc(self,IsoSpeedDesc):
        self.IsoSpeedDesc = IsoSpeedDesc[:]

    def set_shutter_speed_desc(self,ShutterSpeedDesc):
        self.ShutterSpeedDesc = ShutterSpeedDesc[:]

    def get_f_number_desc(self):
        return self.FNumberDesc

    def get_iso_speed_desc(self):
        return self.IsoSpeedDesc

    def get_shutter_speed_desc(self):
        return self.ShutterSpeedDesc

