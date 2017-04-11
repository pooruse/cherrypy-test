import cherrypy
import threading
from app.hello import Root
#from app.mcu import protocol
import time
import os

'''
p = protocol.Proocol()
t1 = time.time()
def mcu_polling():
    while True:
        t2 = time.time()
        if t2 > (t1 + 0.016):
            p.tx_polling()
        p.rx_polling()
th = threading.Thread(target=mcu_polling)
th.start()
'''

app = cherrypy.tree.mount(Root(), '/app')


if __name__=='__main__':

    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8076,
    })

    # Run the application using CherryPy's HTTP Web Server
    cherrypy.quickstart(Root())
