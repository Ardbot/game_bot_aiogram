from bot.machine import config_printer
from bot.machine.serial_printer import write_port


def _position():
    position = "Позиция:" + " X" + str(config_printer.XPOS) + " Y" + str(config_printer.YPOS) + " Z" + str(
    config_printer.ZPOS)
    return position

    # config_printer.XPOS = gcode['X']

    # return position


def forward():
    """Вперёд"""
    if config_printer.MAX_Y > config_printer.YPOS >= 0:
        config_printer.YPOS = config_printer.YPOS + config_printer.STEP
        write_port("G0 Y" + str(config_printer.YPOS))
        return _position()
    elif config_printer.YPOS > config_printer.MAX_Y:
        config_printer.YPOS = config_printer.MAX_Y
        print(config_printer.YPOS)
        return "Y max"
    elif config_printer.YPOS < 0:
        config_printer.YPOS = 0
        print(config_printer.YPOS)
        return "Y min"


def back():
    """Назад"""
    if config_printer.MAX_Y >= config_printer.YPOS > 0:
        config_printer.YPOS = config_printer.YPOS - config_printer.STEP
        write_port("G0 Y" + str(config_printer.YPOS))
        return _position()
    elif config_printer.YPOS > config_printer.MAX_Y:
        config_printer.YPOS = config_printer.MAX_Y
        print(config_printer.YPOS)
        return "Y max"
    elif config_printer.YPOS < 0:
        config_printer.YPOS = 0
        print(config_printer.YPOS)
        return "Y min"


def right():
    """Вправо"""
    if config_printer.MAX_X > config_printer.XPOS >= 0:
        config_printer.XPOS = config_printer.XPOS + config_printer.STEP
        write_port("G0 X" + str(config_printer.XPOS))
        return _position()
    elif config_printer.XPOS > config_printer.MAX_X:
        config_printer.XPOS = config_printer.MAX_X
        print(config_printer.XPOS)
        return "X max"
    elif config_printer.XPOS < 0:
        config_printer.XPOS = 0
        print(config_printer.XPOS)
        return "X min"


def left():
    """Влево"""
    if config_printer.MAX_X > config_printer.XPOS > 0:
        config_printer.XPOS = config_printer.XPOS - config_printer.STEP
        write_port("G0 X" + str(config_printer.XPOS))
        return _position()
    elif config_printer.XPOS > config_printer.MAX_X:
        config_printer.XPOS = config_printer.MAX_X
        print(config_printer.XPOS)
        return "X max"
    elif config_printer.XPOS < 0:
        config_printer.XPOS = 0
        print(config_printer.XPOS)
        return "X min"


def up():
    """ Вверх """
    if config_printer.MAX_Z > config_printer.ZPOS >= 0:
        config_printer.ZPOS = config_printer.ZPOS + config_printer.STEPZ
        write_port("G0 Z" + str(config_printer.ZPOS))
        print(config_printer.ZPOS)
        return _position()
    elif config_printer.ZPOS > config_printer.MAX_Z:
        config_printer.ZPOS = config_printer.MAX_Z
        print(config_printer.XPOS)
        return "Z max"
    elif config_printer.ZPOS < 0:
        config_printer.ZPOS = 0
        print(config_printer.XPOS)
        return "Z min"


def home():
    """Домой"""
    print("Домой")
    msg = write_port("G28")


def this_answer(answer = "No data"):
    """ Ждать определенный ответ """
    i=0
    # if anr != answer or i < 10:
    #     read_port()
    #
    # # i = 0
    # # while i < 10 or msg == '':
    # #     i++
    #
    # return msg

    #
    # def extruder(temp):
    #     t = ser.write(str.encode("M302 S245\r\n", encoding='utf-8'))  # запрос температуры экструдера
