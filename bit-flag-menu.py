# f1-f4 example functions
def f1():
	print('1. F1 is considered the top of motorsports')

def f2():
	print('2. F2 is where potential F1 drivers hone their skills')

def f3():
	print('4. The Nikon F3 was one Nikon\'s best professional grade SLR!')

def f4():
	print('8. F4 is a decentralised open-wheel racing category intended for junior drivers')


def bit_flag(query: int, *functions: str) -> None:
	"""Bit-coded flags to filter several different options/functions.

	Input of 0 (zero) executes none of the associated functions.
	Currently raises ValueError if not enough functions for the query.

	ARGS
		query	Requested flag
			VALUE	DESC.
				1	f1
				2	f2
				4	f3
				8	f4
			...		...
	"""
	
	b_length = query.bit_length()
	if len(functions) < b_length:
		raise ValueError('Input query does not fit within range')
	else:
		for i in range(b_length):
			if 1 & (query >> i):
				functions[i]()


if __name__ == '__main__':
	# Testing
	query = int(input('Input flag:\t'))
	bit_flag(query, f1, f2, f3, f4)
	print(help(bit_flag))
