import protocol_utils
import serial
import command_tx as tx
import command_rx as rx

class Protocol:
    '''
    midware of serial port and protocol,
    create a serial port object and provide it to 
    protocol_rx and protocol_tx constructor
    '''

    
    
    def __init__(self):
        self.rx_status = 0
        self.uart = serial.Serial("/dev/ttymxc1", 115200)
    
    def rx_polling(self):
        # check uart data size in input buffer
        ret = self.uart.inWaiting()
        # check head
        if self.rx_status == 0:
            
            # nothing in uart input buffer
            if ret < 1:
                return
            
            self.head = self.uart.read(1)
            if ord(self.head) == protocol_utils.MCU_HEAD:
                self.rx_status = 1
                
            return
        else:
            if ret >= (protocol_utils.rx_len - 1):
                data = self.uart.read(protocol_utils.rx_len - 1)
            else:
                return

        self.rx_status = 0

        data = self.head + data
        data = map(ord, data)
        print("rx:",map(hex,data))
        cks = protocol_utils.get_checksum(data[0:-1])
        if  data[-1] != cks:
            return

        # cut head and tail(checksum)
        data = data[1:-1]
        while True:
            l = data[0]
            if l == 0xFF:
                break
            
            cmd = data[1]
            if cmd in rx.cmd_dict:
                if rx.cmd_dict[cmd]:
                    # run functions in dectionary
                    rx.cmd_dict[cmd](data[2:l+1])
                    
            if data:
                break
            else:
                data = data[l+1:]

                
    next_tx_len = 0
    def tx_polling(self):

        # check empty
        if len(protocol_utils.tx_buf) == 0:
            return

        if self.next_tx_len != 0:
            protocol_utils.tx_len = self.next_tx_len
            self.next_tx_len = 0
        
        send_buf = []
        send_buf.append(0xC2)
        tx_remain = protocol_utils.tx_len - 2
        status = 0
        
        while True:
            # insert package as much as possible
            if status == 0:
                cmd_len = self.get_first_cmd_len()
                if cmd_len == 0:
                    status = 2
                elif cmd_len <= (tx_remain - 3):
                    send_buf = send_buf + self.get_buf()
                    tx_remain = tx_remain - cmd_len
                else:
                    status = 1
            
            # insert package as much as possible
            elif status == 1:
                if cmd_len <= protocol_utils.tx_len -2:
                    if len(protocol_utils.tx_buf) <= (protocol_utils.tx_len - 2 + tx_remain):
                        send_buf = send_buf + self.get_buf()
                        status = 3
                    else:
                        status = 2
                else:
                    if len(protocol_utils.tx_buf) <= (protocol_utils.tx_len - 2):
                        status = 3
                    else:
                        status = 2
                        

            # change tx len
            elif status == 2:
                ret = protocol_utils.get_interval(len(protocol_utils.tx_buf) + 2)
                if ret != protocol_utils.tx_len:
                    self.next_tx_len = ret
                    ret = protocol_utils.get_interval_index(ret)
                    tmp_buf = [protocol_utils.CMD_TX_CHANGE_LENGTH, ret]
                    change_tx_buf = tx.package(tmp_buf)
                    send_buf = sned_buf + change_tx_buf
                status = 3
                
            # send buf
            elif status == 3:
                
                if len(send_buf) < (protocol_utils.tx_len - 1):
                    send_buf.append(0xFF)
                    
                send_buf = send_buf + [0] * (protocol_utils.tx_len - len(send_buf) - 1)
                send_buf.append(protocol_utils.get_checksum(send_buf))
                print("tx:",map(hex,send_buf))
                self.uart.write(bytearray(send_buf))
                break

    def get_buf(self):
        l = protocol_utils.tx_buf[0]
        tmp = protocol_utils.tx_buf[0:l+1]
        protocol_utils.tx_buf = protocol_utils.tx_buf[1+l:]
        return tmp
    
    def get_first_cmd_len(self):
        if protocol_utils.tx_buf:
            return protocol_utils.tx_buf[0]
        else:
            return 0
            

