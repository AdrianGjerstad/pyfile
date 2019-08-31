#!/usr/bin/env python3

########################################
# FLAGS
########################################

PLAIN_TEXT = 0b00000000
BINARY_TEXT = 0b00000001

READ = 0b00000010
WRITE = 0b00000100
APPEND = 0b00001000

########################################
# MASKS
########################################

__BINARY_MASK__ = 0b00000001
__IO_MASK__ = 0b00000110
__APPEND_MASK__ = 0b00001000

########################################
# PYFILE
########################################

class PyFile:
    def __init__(self, name, use_flags=PLAIN_TEXT|READ|WRITE|APPEND):
        self.name = name
        self.binary = (use_flags & __BINARY_MASK__) >> 0
        self.io =     (use_flags &   __IO_MASK__  ) >> 1
        self.append = (use_flags & __APPEND_MASK__) >> 3

    def open(self):
        return PyFileBuffer(self.name, self.io, self.binary, self.append)

########################################
# PYFILEBUFFER
########################################

class PyFileBuffer:
    def __init__(self, name, io, b, append):
        textflags = ""

        # Text/Binary Flags
        if b:
            textflags += "b"
        else:
            textflags += "t"

        self.read = None
        self.write = None

        if io & 0b10 and not append:
            self.write = open(name, "w" + textflags)
        elif append:
            self.write = open(name, "a" + textflags)
        if io & 0b1:
            self.read = open(name, "r" + textflags)

        self.name = name
        self.textflags = textflags
        self.b = b

    def __repr__(self):
        return 'PyFile IOBuffer: ' + self.name
