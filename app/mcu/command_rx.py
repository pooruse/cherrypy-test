import protocol_utils

def change_rx_len(data):
    ret = protocol_utils.get_interval_from_index(data[0])
    protocol_utils.rx_len = ret

def dummy(data):
    print("dummy rx")
    rx_dummy = 1

def get_version(data):
    rx_version = data

def get_button(data):
    rx_button = data

def get_servo_status(data):
    rx_servo_status = data[0]

def get_stepper_status(data):
    rx_stepper_status = data[0]

def get_fan_status(data):
    rx_fan_status = data[0]

def get_eeprom_hw_info(data):
    rx_hw_info = data

cmd_dict = {
    1: change_rx_len,
    2: dummy,
    3: get_version,
    4: get_button,
    5: get_servo_status,
    6: get_stepper_status,
    7: get_fan_status,
    8: get_eeprom_hw_info,
} 
