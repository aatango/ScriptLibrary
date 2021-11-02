# f1-f4 example functions
def f1():
	print('1. F1 is considered the top of motorsports')

def f2():
	print('2. F2 is where potential F1 drivers hone their skills')

def f3():
	print('4. The Nikon F3 was one Nikon\'s best professional grade SLR!')

def f4():
	print('8. F4 is a decentralised open-wheel racing category intended for junior drivers')


def bit_flag(functions: dict) -> None:
	"""Bit-coded flags to select program options.

	
	Input of 0 (zero) executes none of the argument functions.
	Crashes with ValueError if query doesn't fit available functions.
	
	ARGS
		functions - {function_name: description}
	"""

	f_keys = list(functions.keys())
	f_values = list(functions.values())

	print('AVAILABLE FUNCTIONS', '-' * 19, sep='\n')
	print('0\tNothing')
	print(f'1\t{f_values[0]}')
	for i, desc in enumerate(f_values[1:]):
		print(i + 1 << 1, desc, sep='\t')

	user_input = input('\nInput flag: ') or '1'
	input_flag = sum([int(i) for i in user_input.split()])

	b_length = input_flag.bit_length()
	if len(functions) < b_length:
		raise Value_Error('Input input_flag  does not fit within range')
	else:
		for i in range(b_length):
			if 1 & (input_flag  >> i):
				print('\n', end='')
				f_keys[i]()


if __name__ == '__main__':
	# Testing
	function_list = {
		f1: 'f1',
		f2: 'f2',
		f3: 'f3',
		f4: 'f4',
	}

	bit_flag(function_list)
	print(help(bit_flag))
