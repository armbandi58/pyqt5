import serial
import time
import sys

# Normal kapcsolodas
"""
var_serial = serial.Serial('COM10', baudrate=9600)#,timeout=1)

i = 1

def Read_Serial():
    global var_serial
    #var_serial.write()
    asd = var_serial.readline(1000).decode('utf')
    return  asd

while flag_while:
    try:
        inp = input("Do i send the DATAs from SerialPort?\n")

        if inp == 'y':
            print(Read_Serial())
            print(Read_Serial())
    except KeyboardInterrupt as e:
        print(e)
        print("[+] Program leall...")
        flag_while = False
        #raise SystemExit

    print(Read_Serial())"""
    #time.sleep(2)

import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    return ports

def findPort(portsFound):
    comPort = 'None'
    nbr_of_Connection = len(portsFound)
    global found_Ports

    for i in range (0,nbr_of_Connection):
        port = found_Ports[i]
        strPort = str(port)
        if 'STM' in strPort:
            splitPort = strPort.split(' ')
            comPort = (splitPort[0])

    return comPort

found_Ports = getPort()
connectPort = findPort(found_Ports)

if connectPort != 'None':
    print("[+] Kapcsolat el")
    var_serial = serial.Serial(connectPort, baudrate=9600, timeout=1000)
    flag_while = True
else:
    print("[+] Error, nem sikerult a kapcsolat")

while flag_while:
    try:
        print(var_serial.readline(1000).decode('utf'), end = '')
    except:
        print("[+] Progi leall")
        flag_while = False
        raise SystemExit
