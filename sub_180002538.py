import sys
import math
import re
from pwn import * 
from dumpulator import Dumpulator

def REV(n: int) -> int:
    return ((n >> 24) & 0xff) | ((n << 8) & 0xff0000) | ((n >> 8) & 0xff00) | ((n << 24) & 0xff000000)
    # If output of all the above expression is
    # OR'ed then it results in 0xddccbbaa

def sub_180002464(x,y):
    r9 = x[0xc0]
    pe_heder = x[0xa0+0xc:]
    r8d = 0
    ebx = pe_heder[6]
    r9 += 0x18
    r9 = pe_heder[r9:]
    #print(hexdump(r9))
    r11 = y
    #print(hex(r11))
    v6 = ebx != 0
    for i in range(6):
        v8 = REV(int.from_bytes(r9[0xc:0x10]))
        print(hex(v8))
        tmp = REV(int.from_bytes(r9[8:0xc]))
        print(hex(tmp))
        tmp += v8
        print("--------------")
        print(hex(tmp))
        if(v8 <= y and tmp > y):
            print("ahah")
            #print(hexdump(r9))
            r8 = REV(int.from_bytes(r9[0x14:0x18]))
            print(hex(r8))
            r8 -= y
            if(r8 < 0):
                r8 = r8 & 0xffffffff
            r8 += y
            #print(hex(r8)[5:])
            return "0x"+hex(r8)[5:]
        else:
            r9 = r9[0x28:]
    return y

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
        to_compare_two = REV(int.from_bytes((x[(0x3c+4+158+10+0x98):(0x3c+4+158+10+0x98+4)])))
        if(to_compare_two):
            to_compare_three = REV(int.from_bytes(x[(0x3c+4+158+10+0x54):(0x3c+4+158+10+0x58)]))
            #print(hexdump(to_compare_three))
            rax =0 
            v7 = y
            #for test case we set v7 = 0 , remove after finishing testing
            #v7 = 0
            if(v7 or to_compare_two < to_compare_three):
                print(1)
                return hex(to_compare_two)
            else:
                print(2)
                return sub_180002464(x[0x3c:],to_compare_two)

def main():
    binar = open("winload.efi","rb").read()
    mz_header = binar[0:2]
    if(mz_header == b'MZ'):
        mz_header_binary = binar
        print("aici")
        pe_heder =  binar[binar[0x3c]:]
        if(pe_heder):
            print((sub_1800024C4(binar,1)))


if __name__ == "__main__":
    main()
