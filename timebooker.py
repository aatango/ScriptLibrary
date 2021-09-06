"""Small utility to help me keep track of time spent per task/project.

Also has method to present summary of existing projects in log.
"""


def add_entry(project: str, comment: str) -> None:
	"""Adds new entry to log.

	Calculates difference between current time,
	and timestamp present on last line of referenced file.

	Rewrites entire file[1], with new entry appended at end.
	Finally, new starting timestamp is added.

	If no file exists, or is badly formatted, a new log is started.

	[1] File is not expected to become big enough to affect performance.
	"""

	import time
	
	TIME_APPROX = 0.25 #Hours

	try:
		with open(FILE_PATH + FILE_NAME, 'r') as file:
			lines = file.readlines()
		start_time = float(lines[-1])
		current_time = time.time()
		spent_time = round((current_time - start_time)/3600/TIME_APPROX)\
			*TIME_APPROX
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


def view_log() -> None:
	"""Sorts (by project) and presents current status of timebook.

	Sums spent time, and lists comments related to each of the projects.
	"""

	with open(FILE_PATH + FILE_NAME, 'r') as file:
		lines = file.readlines()[:-1]
	projects = list(set([line.split('\t')[2] for line in lines]))
	for project in projects:
		spent_time = 0.0
		comments = ''
		for line in lines:
			line = line.split(sep='\t')
			if line[2] == project:
				spent_time += float(line[1])
				comments += line[3]
		header = f'{project}\t{spent_time:.2f}'
		print(header, '-' * len(header), comments, sep='\n')


def main() -> None:
	"""Execute timekeepr program.

	Boolean check on project ID to both maintain window visible
	(in case user wants to read log), and to close program
	without new entry.
	"""
	
	bool_log = input('Truthy to view Log: ') 
	if bool_log:
		view_log()
	print('| NEW ENTRY |')
	project = input('Project ID: ')
	if project:
		comment = input('Comments: ')
		add_entry(project, comment)


if __name__ == "__main__":
	FILE_PATH = '../'
	FILE_NAME = 'timekeeper'
	main()
	
