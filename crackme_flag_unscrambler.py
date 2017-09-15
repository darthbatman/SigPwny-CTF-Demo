# scrambled flag
# dXF1e3QndXZ1IHVzcXJ3JHVydHdxc3UjdXB3JHV2cXF0dXckdSNxcnRzdXB0IXUm

import codecs, base64, binascii

def reverse_operations(scrambled_flag):
	scrambled_flag = base64.b64decode(scrambled_flag)
	print scrambled_flag
	scrambled_flag = ''.join(chr(ord(char)^ 0x42) for char in scrambled_flag)
	print scrambled_flag
	scrambled_flag = binascii.unhexlify(scrambled_flag)
	print scrambled_flag
	scrambled_flag = codecs.decode(scrambled_flag, 'rot13')
	print scrambled_flag
	return scrambled_flag

if __name__ == '__main__':
    scrambled_flag = raw_input("Enter the scrambled flag: ").strip()
    print scrambled_flag
    flag = reverse_operations(scrambled_flag)
    print "flag: " + flag