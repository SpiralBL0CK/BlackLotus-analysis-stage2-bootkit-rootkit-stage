import sys
import math
import re
from pwn import * 
from dumpulator import Dumpulator


def extra_help():
    f = open("winload.efi","rb").read()
    m = re.search(b"\x41\xb8\x09\x00\x00\xd0", f)
    pos = m.span()[0]
    print(hex(pos))
    #print(hexdump(f[591361:]))
    #print(m.span())
    #print(hexdump(f))

def REV(n: int) -> int:
    return ((n >> 24) & 0xff) | ((n << 8) & 0xff0000) | ((n >> 8) & 0xff00) | ((n << 24) & 0xff000000)
    # If output of all the above expression is
    # OR'ed then it results in 0xddccbbaa


def sub_180002398(x,y):
    offset_pe_header = (int.from_bytes(x[0x3c:0x3d]))
    tmp = int.from_bytes(x[offset_pe_header+0x84:offset_pe_header+0x85])
    #print(hex(tmp))
    if(tmp > 3):
        z = REV(int.from_bytes(x[(offset_pe_header+0xa4):(offset_pe_header+0xa6)]))
        print(hex(z))
        if(z):
            ebx = REV(int.from_bytes(x[offset_pe_header+0xa0:offset_pe_header+0xa4]))
            rax = 0xAAAAAAAAAAAAAAAB
            #print(hex(ebx))
            k = open("memory_ram.dmp","rb").read()
            #1458464 = 00000000`00164120
            tmp = k[3000:]
            #print(hexdump(k))
            #print(hex(z))
            rax *=z 
            rdx = int(hex(rax)[2:6],base=16)
            rax = hex(rax)[18:22]
            rax = int(rax,base=16)
            rdx = (rdx >> 3)-1
            print(hex(rdx))
            r11 = 0x91201
            #print(hexdump(k))
            tmp = rdx
            flag = 0
            ecx_tmp = 0
            for i in range(rdx):
                if flag:
                    ecx = tmp+ecx_tmp >> 1
                else:
                    ecx = tmp+i >> 1
                rax = ecx
                print(hex(rax))
                rdi = rax+rax*2
                rdi = rdi*4+0x2fec+20
                eax = REV(int.from_bytes(k[rdi:rdi+4]))
                #print(hex(eax))
                if(eax >= 0x91201):
                    flag = 1
                    if(0x91201 > REV(int.from_bytes(k[rdi+4:rdi+8]))):
                        print("aici2")
                        break
                    ecx_tmp = ecx+1
                    print("in cazu meu"+str(hex(ecx_tmp)))
                flag = 0
                tmp = ecx-1


                    
                #print(hex(eax))
                """
                v10 = (rdx+i >> 1)
                if(i >= 1):
                    v10 = v10 >> 1
                rax = v10-1
                rdi = (rax+rax*2)
                print(hex(v10))
                rdi = rdi*4+0x2fec+20
                #print(hex(rdi))
                
                    
                        print(hex(i))
                        print(hex(REV(int.from_bytes(k[rdi+4:rdi+8]))))
                        print("aici sunt")
                        break
                
                """

def main():
    binar = open("winload.efi","rb").read()
    #print(hexdump(binar))
    mz_header = binar[0:2]
    if(mz_header == b'MZ'):
        mz_header_binary = binar
        print("aici")
        pe_heder =  binar[binar[0x3c]:]
        if(pe_heder):
            #extra_help()
            print((sub_180002398(binar,"41b8090000d0")))


if __name__ == "__main__":
    main()