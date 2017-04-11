PROTOCOL_LEN0 = 8
PROTOCOL_LEN1 = 16
PROTOCOL_LEN2 = 32
PROTOCOL_LEN3 = 64
PROTOCOL_LEN4 = 128
PROTOCOL_LEN5 = 256
PROTOCOL_LEN6 = 512
PROTOCOL_LEN7 = 1024
PROTOCOL_LEN8 = 2048
SMARC_HEAD = 0xC2
MCU_HEAD = 0xC1

CMD_TX_CHANGE_LENGTH = 1
CMD_TX_DUMMY = 2
CMD_TX_MCU_RESET = 3
CMD_TX_GET_VERSION = 4
CMD_TX_BUTTON_CONTROL = 5
CMD_TX_SERVO_HW_ENABLE = 6
CMD_TX_SERVO_SW_ENABLE = 7
CMD_TX_SERVO_MOVE = 8
CMD_TX_SERVO_MOVE_STEPS = 9
CMD_TX_SERVO_CANCEL_MOVE = 10
CMD_TX_SERVO_HOME = 11
CMD_TX_SERVO_CALIBRATION = 12
CMD_TX_AUTOTUNE = 13
CMD_TX_BUZZER_CONTROL = 14
CMD_TX_STEPPER_MOVE = 15
CMD_TX_STEPPER_CANCEL_MOVE = 16
CMD_TX_FAN_SET_DUTY = 17
CMD_TX_EEPROM_GET_HW_INFO = 18
CMD_TX_LCD_CLEAR = 19
CMD_TX_LCD_SET_FONT_ADDR = 20
CMD_TX_LCD_WRITE = 21
CMD_TX_LCD_CREATE_BAR = 22
CMD_TX_LCD_SET_BAR = 23
CMD_TX_LCD_RESERVE = 24
CMD_TX_LCD_DRAW = 25
CMD_TX_LCD_SEL_LINE = 26

CMD_RX_CHANGE_LENGTH = 1
CMD_RX_DUMMY = 2
CMD_RX_GET_VERSION = 3
CMD_RX_BUTTON = 4
CMD_RX_SERVO_STATUS = 5
CMD_RX_STEPPER_READY = 6
CMD_RX_FAN_STATUS = 7
CMD_RX_EEPROM_HW_INFO = 8

SERVO_DIR_UP = 0
SERVO_DIR_DOWN = 1

BUZZER_STOP = 0
BUZZER_MUSIC = 1
BUZZER_BEEPS = 2

FAN_OK = 0
FAN_FAIL = 1

LCD_LINE_OFF = 8

rx_dummy = 0
rx_version = ''
rx_button = []
rx_servo_status = None
rx_stepper_status = None
rx_fan_status = FAN_OK
rx_hw_info = None

tx_buf = []
tx_len = 8
rx_len = 8


def get_interval(l):
    if l <= PROTOCOL_LEN0:
        tmp = PROTOCOL_LEN0
    elif l <= PROTOCOL_LEN1:
        tmp = PROTOCOL_LEN1
    elif l <= PROTOCOL_LEN2:
        tmp = PROTOCOL_LEN2
    elif l <= PROTOCOL_LEN3:
        tmp = PROTOCOL_LEN3
    elif l <= PROTOCOL_LEN4:
        tmp = PROTOCOL_LEN4
    elif l <= PROTOCOL_LEN5:
        tmp = PROTOCOL_LEN5
    elif l <= PROTOCOL_LEN6:
        tmp = PROTOCOL_LEN6
    else:
        tmp = PROTOCOL_LEN7

    return tmp

def get_interval_index(l):
    if l <= PROTOCOL_LEN0:
        tmp = 0
    elif l <= PROTOCOL_LEN1:
        tmp = 1
    elif l <= PROTOCOL_LEN2:
        tmp = 2
    elif l <= PROTOCOL_LEN3:
        tmp = 3
    elif l <= PROTOCOL_LEN4:
        tmp = 4
    elif l <= PROTOCOL_LEN5:
        tmp = 5
    elif l <= PROTOCOL_LEN6:
        tmp = 6
    else:
        tmp = 7
        
    return tmp

def get_interval_from_index(index):
    if index == 1:
        tmp = PROTOCOL_LEN1
    elif index == 2:
        tmp = PROTOCOL_LEN2
    elif index == 3:
        tmp = PROTOCOL_LEN3
    elif index == 4:
        tmp = PROTOCOL_LEN4
    elif index == 5:
        tmp = PROTOCOL_LEN5
    elif index == 6:
        tmp = PROTOCOL_LEN6
    elif index == 7:
        tmp = PROTOCOL_LEN7
    elif index == 8:
        tmp = PROTOCOL_LEN8
    else:
        tmp = PROTOCOL_LEN0
        
    return tmp

def get_checksum(data):
    return sum(data) & 255
