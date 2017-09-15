import codecs, base64, binascii

scrambled_flag = 'dXF1e3QndXZ1IHVzcXJ3JHVydHdxc3UjdXB3JHV2cXF0dXckdSNxcnRzdXB0IXUm'

def scramble(flag):
    flag = codecs.encode(flag, 'rot13')
    flag = binascii.hexlify(bytes(flag.encode('utf-8')))
    flag = ''.join(chr(ord(char) ^ 0x42) for char in flag)
    flag = base64.b64encode(flag)
    return flag

if __name__ == '__main__':
    flag = raw_input("Enter the flag: ").strip()

    if scramble(flag) == scrambled_flag:
        print("You got it!")
    else:
        print("Hack harder next time")