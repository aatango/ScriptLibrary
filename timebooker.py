"""Small utility to help me keep track of time spent per task.

Upon launching, will calculate time spent using info written on last line.
Afterwards, asks for user inputs: project name, and comments.
Finally, writes the whole existing data[1], replacing the last line
Appends time of writing at the end of file, for future use.

If no file exists, or is badly formatted, a new log is started.

[1] File is not expected to be big enough to affect performance.
"""

# to be formatted as function if ever needed
if __name__ == '__main__':
	import time

	
	FILE_PATH = '../'
	FILE_NAME = 'timekeeper'
	TIME_APPROX = 0.25 #Hours
	try:
		with open(FILE_PATH + FILE_NAME, 'r') as file:
			lines = file.readlines()
		start_time = float(lines[-1])
		current_time = time.time()
		# approx by ceiling to interval; flooring also possible
		# -(-a//b) == math.ceil(a/b)
		spent_time = -(-(current_time - start_time)/3600//TIME_APPROX)\
			*TIME_APPROX
		print('| NEW ENTRY |')
		project = input('Project name: ')
		comment = input('Comments: ')
		last_line = '\t'.join(
			[time.ctime(start_time), f'{spent_time:.2f}', project, comment]
		)

		new_lines = lines[:-1] + [last_line] + ['\n'+ str(time.time())]
		with open(FILE_PATH + FILE_NAME, 'w') as file:
			file.writelines(new_lines)
		# if print below is done then entry is surely added
		print(last_line)
	except:
		current_time = time.time()
		with open(FILE_PATH + FILE_NAME, 'w') as file:
			file.write(str(current_time))
		print('New log started:')
		print(time.ctime(current_time))
		print(FILE_PATH + FILE_NAME)
