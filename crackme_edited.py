import codecs, base64, binascii

scrambled_flag = 'dXF1e3QndXZ1IHVzcXJ3JHVydHdxc3UjdXB3JHV2cXF0dXckdSNxcnRzdXB0IXUm'

def scramble(flag):
    flag = codecs.encode(flag, 'rot13')
    print "1 " + flag
    flag = binascii.hexlify(bytes(flag.encode('utf-8')))
    print "2 " + flag
    flag = ''.join(chr(ord(char) ^ 0x42) for char in flag)
    print "3 " + flag
    flag = base64.b64encode(flag)
    print "4 " + flag
    return flag

if __name__ == '__main__':
    flag = raw_input("Enter the flag: ").strip()

    if scramble(flag) == scrambled_flag:
        print("You got it!")
    else:
        print("Hack harder next time")