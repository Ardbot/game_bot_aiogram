""" Работа с COM PORT """
import threading
import time

import requests
import serial
import serial.tools.list_ports

from bot import config_bot
from bot.machine import config_printer

ser = serial.Serial()
ser.port = config_printer.PORT
ser.baudrate = config_printer.BAUDRATE


def list_ports():
    """ Возвращает список доступных портов """
    ports = serial.tools.list_ports.comports()
    list_p = ''
    for port, desc, hwid in sorted(ports):  # port, desc, hwid
        list_p = f"{list_p}{desc}\n"
    return list_p


def open_port():
    """ Подключение к порту """
    if ser.is_open:
        print(ser.is_open)  # True
        return f"{ser.port} open"
    else:
        try:
            ser.open()
            # read_port()
            time.sleep(0.1)
            # print(ser.inWaiting())    # Размер данных в буфере
            ser.reset_input_buffer()  # Удалить из буфера Принимаемые с принтера данные (echo)
            # print(ser.inWaiting())
            port_poll() # сканирую буфер
            return f"Connection to {ser.port}"
        except serial.SerialException as e:
            return f"Error connection to {ser.port}.\n\n {list_ports()}. Err: {e}"


def close_port():
    """ Закрыть порт """
    if ser.is_open:
        try:
            #ser.reset_output_buffer()  # Удалить из буфера отправляемые данные
            ser.close()
            return f"{ser.port} close"
        except serial.SerialException as e:
            return f"Error close {ser.port}\n{e}"
    else:
        return f"{ser.port} not open"


def write_port(code):
    """ Отправляем данные в порт и получаем ответ"""
    if ser.is_open:
        try:
            _gcode = str(code) + "\r\n"  # Добавляем символы перевода
            ser.write(str.encode(_gcode, encoding='utf-8'))  # Отправляем значения в сериал порт
            time.sleep(0.1)
            msg = read_port()  # Ответ
            return msg
        except serial.SerialException as e:
            return f"Error write to {ser.port}.\nErr: {e}"
    else:
        msg = f"{ser.port} not open\n/open_port"
        return msg


def read_port():
    """ Считываем данные с COM PORT """
    if ser.is_open:
        try:
            msg = b''  # Массив данных
            while ser.inWaiting() > 0:
                msg += ser.readline()
            else:
                msg = str(msg, 'UTF-8')  # Конвертируем байты в строку
                if msg == '':
                    return "No data"
                else:
                    return msg
        except serial.SerialException as e:
            return f"Error read to {ser.port}.\nErr: {e}"
    else:
        msg = f"{ser.port} not open\n/open_port"
        return msg


def converter(gcode):
    """ Конвертирует строку с координатами в словарь """
    gcode = gcode[:27]
    gcode = gcode.split(" ")
    coord = {}
    for i in gcode:
        k = i[0]  # Ключ
        v = i[2:]  # Значение
        coord.update({k: v})  # Добавляем пару в словарь
    # print(coord)
    return coord


async def console(code):
    """ Консоль для ввода gcode """
    msg = write_port(code)
    return msg

def msg_adm(msg):
    r = requests.get(f'https://api.telegram.org/bot{config_bot.TOKEN}/sendMessage?chat_id={config_bot.ADMIN}&text={msg}')
    # r.status_code
    msg = r.text
    return msg


def port_poll():
    """ Опрос порта """
    if ser.is_open:
        if ser.inWaiting() > 0:
            msg = read_port()
            print(msg)
            msg_adm(msg)    # Отправка сообщений админу (принудительная)
        threading.Timer(1, port_poll).start()
    else:
        msg_adm(f'Disconnection {ser.port}\n/open_port')




