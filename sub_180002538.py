import sys
import math
import re
from pwn import * 
from dumpulator import Dumpulator

def REV(n: int) -> int:
    return ((n >> 24) & 0xff) | ((n << 8) & 0xff0000) | ((n >> 8) & 0xff00) | ((n << 24) & 0xff000000)
    # If output of all the above expression is
    # OR'ed then it results in 0xddccbbaa

def sub_1800024C4(x,y):
    r9 = int.from_bytes(x[0x3c:0x3c+1])
    #print(hexdump(r9))
    #print(type(r9))
    #print(r9)
    r10 = x[r9:]
    #print(hexdump(r10))
    v3 = 0
    r8d= 0
    rbx = x
    rcx = rbx
    to_compare = (x[(0x3c+4+158+0x84+10):(0x3c+4+158+0x84+14)])
    to_compare = (REV(int.from_bytes(to_compare)))
    if(to_compare > 2):
        

def main():
    binar = open("winload.efi","rb").read()
    mz_header = binar[0:2]
    if(mz_header == b'MZ'):
        mz_header_binary = binar
        print("aici")
        pe_heder =  binar[binar[0x3c]:]
        if(pe_heder):
            sub_1800024C4(binar,1)


if __name__ == "__main__":
    main()
