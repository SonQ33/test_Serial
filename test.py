name = bytes('SPb_CTF_2017', 'utf-8')


valid = [
	int.from_bytes(name[:4], 'big'),
	int.from_bytes(name[4:8], 'big'),
	int.from_bytes(name[8:], 'big')]

valid[0] ^= valid[2]
valid[2] ^= valid[0]
valid[0] ^= valid[2]
serial = '{:08x}-{:08x}-{:08x}'.format(*valid)
print(serial)