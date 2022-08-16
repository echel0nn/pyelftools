#-------------------------------------------------------------------------------
# elftools: common/py3compat.py
#
# Python 2/3 compatibility code
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------
import sys
PY3 = sys.version_info[0] == 3
assert PY3, '''\
Python 2 is no longer supported by pyelftools; if you need to use Python 2,
please download an older pyelftools version (such as version 0.29).
'''


if PY3:
    # Functions for acting on bytestrings and strings. In Python 2 and 3,
    # strings and bytes are the same and chr/ord can be used to convert between
    # numeric byte values and their string representations. In Python 3, bytes
    # and strings are different types and bytes hold numeric values when
    # iterated over.


    def bytes2str(b): return b.decode('latin-1')
    def str2bytes(s): return s.encode('latin-1')
    def int2byte(i): return bytes((i,))
    def byte2int(b): return b

else:
    def bytes2str(b): return b
    def str2bytes(s): return s
    int2byte = chr
    byte2int = ord
    def iterbytes(b):
        return iter(b)
