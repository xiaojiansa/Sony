import SendPost

js_getShutterSpeed = {
    "method": "getShutterSpeed",
    "params": [],
    "id": 1,
    "version": "1.0"}

js_setShutterSpeed = {
    "method": "setShutterSpeed",
    "params": ["1/4"],
    "id": 1,
    "version": "1.0"}

js_getAvailableShutterSpeed = {
    "method": "getAvailableShutterSpeed",
    "params": [],
    "id": 1,
    "version": "1.0"}

js_getSupportedShutterSpeed = {
    "method": "getSupportedShutterSpeed",
    "params": [],
    "id": 1,
    "version": "1.0"}


def shutter_speed(model, command):
    command_result = {"default": "worry"}
    if command == "getShutterSpeed":
        command_result = SendPost.get_property(model, js_getShutterSpeed)
    if command == "getAvailableShutterSpeed":
        command_result = SendPost.get_property_desc(model, js_getAvailableShutterSpeed)
    if command == "getSupportedShutterSpeed":
        command_result = SendPost.get_property_desc(model, js_getSupportedShutterSpeed)
    return command_result


def shutter_speed_set(command, set_value):
    command_result = {"default": "worry"}
    if command == "setShutterSpeed":
        js_setShutterSpeed["params"] = set_value
        command_result = SendPost.set_property(js_setShutterSpeed)
    return command_result


