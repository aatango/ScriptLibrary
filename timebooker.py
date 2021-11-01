"""Small utility to help me keep track of time spent per task/project.

Also has method to present summary of existing projects in log.

Referenced file is meant to be deleted, and restarted, at arbitrary times:
originally meant for one work day.

File is not meant to host any information not produced with this script.
Corruption, or absence of, needed file will result in complete overwrite.
"""

import time


def reset_log() -> None:
	"""Clears existing data on file, keeping only current timestamp."""

	with open(FILE_PATH + FILE_NAME, 'w') as file:
		file.write(str(time.time()))

	print(f'Log reset at {FILE_PATH + FILE_NAME}')

	
def add_entry(project: str = '', comment: str = '') -> None:
	"""Adds new entry to log.

	Calculates difference between current time,
	and timestamp present on last line of referenced file.

	Rewrites entire file[1], with new entry appended at end.
	Finally, new starting timestamp is added.

	If no file exists, or is badly formatted, a new log is started.

	[1] File is not expected to become big enough to affect performance.
	"""

	print('- NEW ENTRY -')

	try:
		project = project or input('Project ID: ')
		if project: 
			comment = comment or input ('Comments: ')
		else:
			print('Empty project; no new entry added.')
			return
		
		with open(FILE_PATH + FILE_NAME, 'r') as file:
			lines = file.readlines()
		start_time = float(lines[-1])
		current_time = time.time()
		spent_time = round((current_time - start_time)/3600/TIME_APPROX)\
			*TIME_APPROX
		last_line = '\t'.join(
			[project, f'{spent_time:.2f}', comment]
		)

		new_lines = lines[:-1] + [last_line] + ['\n'+ str(time.time())]
		with open(FILE_PATH + FILE_NAME, 'w') as file:
			file.writelines(new_lines)
		# if print below is done then entry is surely added
		print(last_line)
	except:
		print('Error adding new entry.', end=' ')
		reset_log()
		add_entry(project, comment)


def view_log() -> None:
	"""Sorts (by project) and presents current status of timebook.

	Sums spent time, and lists comments related to each of the projects.
	If log file does not comform to spec, exception will be indicated.
	"""

	projects = {}
	time = 0.0
	
	try:
		print('- VIEW LOG - ')
		# read log file
		with open(FILE_PATH + FILE_NAME, 'r') as file:
			lines = file.readlines()[:-1]
		lines = [line.split('\t') for line in lines]

		# aggregate projects
		for line in lines:
			if line[0] in projects:
				projects[line[0]] += [line[1:]]
			else:
				projects[line[0]] = [line[1:]]

		# prep and print log
		for project in projects:
			project_time = 0.0
			project_entries = ''
			for entry in projects[project]:
				project_time += float(entry[0])
				project_entries += '\t'.join(entry)
			time += project_time
			header = f'{project_time:.2f}\t{project}'
			print(header, '-' * len(header), project_entries, sep='\n')

		# total time on record
		sum_header = f'{time:.2f}\tTOTAL TIME'
		sum_styling = '-' * len(sum_header)
		print(sum_styling,  sum_header, sum_styling, '\n',sep='\n')

		# halt execution until user input
		input('Press ENTER to continue ...')

	except:
		print('Error reading log.', end=' ')
		if input('Reset? <False> '): reset_log()


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
	print('0\tExit program')
	print(f'1\t{f_values[0]}')
	for i, desc in enumerate(f_values[1:]):
		print(i + 1 << 1, desc, sep='\t')

	user_input = input('\nInput flag <1>: ') or '1'
	input_flag = sum([int(i) for i in user_input.split()])

	b_length = input_flag.bit_length()
	if len(functions) < b_length:
		raise Value_Error('Input input_flag  does not fit within range')
	else:
		for i in range(b_length):
			if 1 & (input_flag  >> i):
				print('\n', end='')
				f_keys[i]()


def main() -> None:
	"""Execute timekeepr program.

	"""

	print('timekeeper v1.1.0, (c)aatango\n')

	functions = {
	add_entry: 'Add new entry',
	view_log: 'View existing log',
	reset_log: 'Reset log with current timestamp'
	}

	bit_flag(functions)


if __name__ == "__main__":
	FILE_PATH = '../'
	FILE_NAME = 'timekeeper'
	TIME_APPROX = 0.25 #Hours
	main()
	
