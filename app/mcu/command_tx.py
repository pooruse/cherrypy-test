import protocol_utils
import struct

def insert_buf(data):
    protocol_utils.tx_buf = protocol_utils.tx_buf + data

def package(data):
    tmp = [len(data)]
    tmp = tmp + data
    return tmp

def dummy():
    print("dummy tx")
    protocol_utils.rx_dummy = 0
    tmp_buf = package([protocol_utils.CMD_TX_DUMMY])
    insert_buf(tmp_buf)

def mcu_reset():
    tmp_buf = package([protocol_utils.CMD_TX_MCU_RESET, 0xAA])
    insert_buf(tmp_buf)

def get_version():
    protocol_utils.rx_version = ''
    tmp_buf = package([protocol_utils.CMD_TX_GET_VERSION])
    insert_buf(tmp_buf)

# en = 0  disable gpio send package
# en = 1  enable gpio send package
def button_control(en):
    tmp_buf = package([protocol_utils.CMD_TX_BUTTON_CONTROL, en])
    insert_buf(tmp_buf)
    
# en = 0  disable gpio send package
# en = 1  enable gpio send package
def servo_hw_enable(en):
    tmp_buf = package([protocol_utils.CMD_TX_SERVO_HW_ENABLE, en])
    insert_buf(tmp_buf)

# en = 0  disable gpio send package
# en = 1  enable gpio send package
def servo_sw_enable(en):
    tmp_buf = package([protocol_utils.CMD_TX_SERVO_SW_ENABLE, en])
    insert_buf(tmp_buf)

# direction: SERVO_DIR_UP, SERVO_DIR_DOWN
# speed: unit: um/s    
# distance: unit: um
def servo_move(direction, speed, distance):
    protocol_utils.rx_servo_status = None
    tmp_buf = struct.pack("<BBII", protocol_utils.CMD_TX_SERVO_MOVE, direction, speed, distance)
    insert_buf(list(tmp_buf))

# direction: SERVO_DIR_UP, SERVO_DIR_DOWN
# freq: pwm frequency
# steps: number of steps
def servo_move_steps(direction, freq, steps):
    protocol_utils.rx_servo_status = None
    tmp_buf = struct.pack("<BBII", protocol_utils.CMD_TX_SERVO_MOVE_STEPS, direction, freq, steps)
    insert_buf(list(tmp_buf))

def servo_cancel_move():
    tmp_buf = package([protocol_utils.CMD_TX_SERVO_CANCEL_MOVE])
    insert_buf(tmp_buf)

def servo_home(en):
    protocol_utils.rx_servo_status = None
    tmp_buf = package([protocol_utils.CMD_TX_SERVO_HOME, en])
    insert_buf(tmp_buf)

# lower_bound: 
# speed: unit: um/s
# upper bound:
#
#  0|]]]]]]] <- this is platform 
#  1|
#  2|        <- set uupper bound here
#  3|
#  4|        <- set lower bound here
#
#  calibration fail: no vat is detected
#  0|     
#  1|
#  2|
#  3|
#  4|]]]]]] 
#
#  calibration fail: something exist between vat and platform
#  0|     
#  1|
#  2|]]]]]] 
#  3|
#  4|
#
#  success
#  0|     
#  1|
#  2|
#  3|]]]]]] 
#  4|
def servo_calibration(lower_bound, speed, upper_bound):
    rx_servo_status = None
    tmp_buf = struct.pack("<BIII",
                          protocol_utils.CMD_TX_SERVO_CALIBRATION,
                          lower_bound,
                          speed,
                          upper_bound)
    
    insert_buf(list(tmp_buf))


def servo_autotune():
    rx_servo_status = None
    tmp_buf = package([protocol_utils.CMD_TX_SERVO_AUTOTUNE])
    insert_buf(tmp_buf)


def buzzer_control(mode, index):
    tmp_buf = struct.pack("<BBI", protocol_utils.CMD_TX_BUZZER_CONTROL, mode, index)
    insert_buf(list(tmp_buf))

# direction: SERVO_DIR_UP, SERVO_DIR_DOWN
# freq: pwm frequency
# steps: number of steps
def stepper_move(direction, freq, steps):
    rx_stepper_status = None
    tmp_buf = struct.pack("<BBII", protocol_utils.CMD_TX_STEPPER_MOVE, direction, freq, steps)
    insert_buf(list(tmp_buf))
    
def stepper_cancel_move():
    tmp_buf = package([protocol_utils.CMD_TX_STEPPER_CANCEL_MOVE])
    insert_buf(tmp_buf)

def fan_set_duty(duty):
    tmp_buf = package([protocol_utils.CMD_TX_STEPPER_CANCEL_MOVE, duty])
    insert_buf(tmp_buf)

def get_hw_info():
    tmp_buf = package([protocol_utils.CMD_TX_EEPROM_GET_HW_INFO])
    insert_buf(tmp_buf)

def lcd_clear():
    tmp_buf = package([protocol_utils.CMD_TX_LCD_CLEAR])
    insert_buf(tmp_buf)

def lcd_set_font_addr(x, y):
    tmp_buf = package([protocol_utils.CMD_TX_LCD_SET_FONT_ADDR, x, y])
    insert_buf(tmp_buf)

def lcd_write(text):
    l = len(text) + 1
    insert_buf(l)
    insert_buf(protocol_utils.CMD_TX_LCD_WRITE)
    insert_buf(map(ord, s))
    
def lcd_create_bar():
    tmp_buf = package([protocol_utils.CMD_TX_LCD_CREATE_BAR])
    insert_buf(tmp_buf)

def lcd_set_bar(percentage):
    tmp_buf = package([protocol_utils.CMD_TX_LCD_CREATE_BAR, percentage])
    insert_buf(tmp_buf)

def lcd_reserve():
    tmp_buf = package([protocol_utils.CMD_TX_LCD_RESERVE])
    insert_buf(tmp_buf)

def lcd_draw():
    tmp_buf = package([protocol_utils.CMD_TX_LCD_DRAW])
    insert_buf(tmp_buf)
    
def lcd_select_line(line):
    tmp_buf = package([protocol_utils.CMD_TX_LCD_SELECT_LINE, line])
    insert_buf(tmp_buf)        


    


