# coding: UTF-8
from unittest import TestCase
from chipy8.compiler import compile

class TestCompiler(TestCase):

    def test_compile_rca(self):
        opcodes = compile('RCA')
        self.assertEquals(opcodes, [0x00, 0x30])

    def test_compile_cls(self):
        opcodes = compile('CLS')
        self.assertEquals(opcodes, [0x00, 0xe0])

    def test_compile_rts(self):
        opcodes = compile('RTS')
        self.assertEquals(opcodes, [0x00, 0xee])

    def test_compile_jump_200(self):
        opcodes = compile('JUMP $200')
        self.assertEquals(opcodes, [0x12, 0x00])

    def test_compile_jump_250(self):
        opcodes = compile('JUMP $250')
        self.assertEquals(opcodes, [0x12, 0x50])