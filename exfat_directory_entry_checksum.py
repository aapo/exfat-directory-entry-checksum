#!/usr/bin/python
'''
Python2 implementation of exFAT Directory Entry checksum calculation:
[ https://docs.microsoft.com/en-us/windows/win32/fileio/exfat-specification#figure-2-entrysetchecksum-computation ]
'''

def EntrySetChecksum(data, secondaryCount):
    checksum = 0 #this should be UINT16 all the time -> max value of 65535
    bytes = (secondaryCount + 1) * 32
    if len(data)<bytes:
        print "Error: Not enough input data"
        sys.exit(1)

    for i in range(0,bytes):
        if i == 2 or i == 3:   #skip checksum-field itself
            continue

        #This doesn't keep checksum UINT16 in the middle of the calculation
        #checksum = (checksum << 15) | (checksum >> 1) + int(ord(data[i]))

        #Forcing values to UINT16
        a_temp=(checksum << 15) % 65535
        b_temp=(checksum >> 1) % 65535
        c_temp=(a_temp | b_temp) % 65535
        d_temp=c_temp + ord(data[i])
        checksum=d_temp % 65535

        #print "debug: ",a_temp,b_temp,c_temp,d_temp,checksum

    return checksum

import sys

if len(sys.argv) == 1:
    print "Usage: python "+sys.argv[0]+" entry.dd"
    sys.exit(1)

d=open(sys.argv[1], "rb").read()

secondaryCount=ord(d[1])
checksum=EntrySetChecksum(d,secondaryCount)

print "checksum in decimal:", checksum
print "checksum in hex:", hex(checksum)

swapped_temp=str(hex(checksum))
swapped=swapped_temp[4:6]+swapped_temp[2:4]
print "checksum in hex (swapped):", "0x"+swapped

print "Values from the given data (offset 0x02 and 0x03):", hex(ord(d[2])),hex(ord(d[3]))

if swapped_temp[4:6] == hex(ord(d[2]))[2:4] and swapped_temp[2:4] == hex(ord(d[3]))[2:4]:
    print "Checksum OK"
else:
    print "Checksum NOT OK"
