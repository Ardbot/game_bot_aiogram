import time, threading

import serial
import serial.tools.list_ports


def list_ports():
    """ Возвращает список доступных портов """
    ports = serial.tools.list_ports.comports()
    list_p = ''
    for port, desc, hwid in sorted(ports):  # port, desc, hwid
        list_p = f"{list_p}{desc}\n"
    return list_p


if __name__ == '__main__':
    print(list_ports())

