# coding: UTF-8

def compile(source):
    tokens = source.split()

    token = tokens[0]
    if token == 'RCA':
        return [0x00, 0x30]
    elif token == 'CLS':
        return [0x00, 0xe0]
    elif token == 'RTS':
        return [0x00, 0xee]
    elif token == 'JUMP':
        if tokens[1] == '$200':
            return [0x12, 0x00] #JUMP $200
        else:
            return [0x12, 0x50]