# coding: UTF-8
from unittest import TestCase
from chipy8.compiler import compile

class TestCompiler(TestCase):

    def test_compile_rca(self):
        opcodes = compile('RCA')
        self.assertEquals(opcodes, [0x00, 0x30])