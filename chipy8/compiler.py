# coding: UTF-8

def compile(source):
    if source == 'RCA':
        return [0x00, 0x30]
    elif source == 'CLS':
        return [0x00, 0xe0]
    elif source == 'RTS':
        return [0x00, 0xee]
    return [0x12, 0x00] #JUMP $200