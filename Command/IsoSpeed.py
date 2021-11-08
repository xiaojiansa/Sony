import SendPost

js_getIsoSpeedRate = {
    "method": "getIsoSpeedRate",
    "params": [],
    "id": 1,
    "version": "1.0"}

js_setIsoSpeedRate = {
    "method": "setIsoSpeedRate",
    "params": ["400"],
    "id": 1,
    "version": "1.0"}

js_getAvailableIsoSpeedRate = {
    "method": "getAvailableIsoSpeedRate",
    "params": [],
    "id": 1,
    "version": "1.0"}

js_getSupportedIsoSpeedRate = {
    "method": "getSupportedIsoSpeedRate",
    "params": [],
    "id": 1,
    "version": "1.0"}


def iso_speed_rate(model, command):
    command_result = {"default": "worry"}
    if command == "getIsoSpeedRate":
        command_result = SendPost.get_property(model, js_getIsoSpeedRate)
    if command == "getAvailableIsoSpeedRate":
        command_result = SendPost.get_property_desc(model, js_getAvailableIsoSpeedRate)
    if command == "getSupportedIsoSpeedRate":
        command_result = SendPost.get_property_desc(model, js_getSupportedIsoSpeedRate)
    return command_result


def iso_speed_rate_set(command, set_value):
    command_result = {"default": "worry"}
    if command == "setIsoSpeedRate":
        js_setIsoSpeedRate["params"] = set_value
        command_result = SendPost.set_property(js_setIsoSpeedRate)
    return command_result
