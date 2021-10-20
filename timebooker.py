"""Small utility to help me keep track of time spent per task/project.

Also has method to present summary of existing projects in log.

Referenced file is meant to be deleted, and restarted, at arbitrary times:
originally meant for one work day.

File is not meant to host any information not produced with this script.
Corruption, or absence of, needed file will result in complete overwrite.
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
	
	try:
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
		current_time = time.time()
		with open(FILE_PATH + FILE_NAME, 'w') as file:
			file.write(str(current_time))
		print('New log started:')
		print(time.ctime(current_time))
		print(FILE_PATH + FILE_NAME)
		add_entry(project, comment)


def view_log() -> None:
	"""Sorts (by project) and presents current status of timebook.

	Sums spent time, and lists comments related to each of the projects.
	If log file does not comform to spec, exception will be indicated.
	"""

	projects = {}
	
	try:
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
			header = f'{project_time:.2f}\t{project}'
			print(header, '-' * len(header), project_entries, sep='\n')
	except:
		print('Logfile does not exist.\nA new one will be created on file execution.')


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
	TIME_APPROX = 0.25 #Hours
	main()
	
