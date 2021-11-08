import SendPost

js_getFNumber = {
      "method": "getFNumber",
      "params": [],
      "id": 1,
      "version": "1.0"
    }
js_setFNumber = {
        "method": "setFNumber",
        "params": ["2.8"],
        "id": 1,
        "version": "1.0"
    }
js_getAvailableFNumber = {
        "method": "getAvailableFNumber",
        "params": [],
        "id": 1,
        "version": "1.0"}
js_getSupportedFNumber = {
        "method": "getSupportedFNumber",
        "params": [],
        "id": 1,
        "version": "1.0"}


def f_number(model, command):
    command_result = {"default": "worry"}
    if command == "getFNumber":
        command_result = SendPost.get_property(model, js_getFNumber)
    if command == "getAvailableFNumber":
        command_result = SendPost.get_property_desc(model, js_getAvailableFNumber)
    if command == "getSupportedFNumber":
        command_result = SendPost.get_property_desc(model, js_getSupportedFNumber)
    return command_result


def f_number_set(command, set_value):
    command_result = {"default": "worry"}
    if command == "setFNumber":
        js_setFNumber["params"] = set_value
        print(js_setFNumber)
        command_result = SendPost.set_property(js_setFNumber)
    return command_result