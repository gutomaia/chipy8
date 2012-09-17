# coding: UTF-8

def compile(source):
    if source == 'CLS':
        return [0x00, 0xe0]
    elif source == 'RTS':
        return [0x00, 0xee]
    return [0x00, 0x30]