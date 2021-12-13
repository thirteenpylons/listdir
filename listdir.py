"""
Functions for creating list of directory

Generates a file that consists the names of files
in the current working directory.
Files will be sorted in alphabetical order.
Directories are omitted.

Author: Christian M. Fulton
Date: 23/04/2021
"""

import os


def main():
	"""
	Run this if not imported
	"""
	get_files()
	append_file()
	editFile()

def get_files():
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	print(sorted(files))
	with open('my_files.txt', 'wt') as wfile:
		wfile.write(str(sorted(files)))


def append_file():
	rfile = open('./my_files.txt', 'rt')
	with open('./my_files.txt', 'at') as afile:
		for line in rfile:
			afile.write(line.replace(',', '\n'))
		rfile.close()


def editFile():
	"""
	Find the first close of square bracket and remove up to it
	"""
	with open('./my_files.txt', 'rt') as src_file:
		cp_file = src_file.read()
	locate = ']'
	find_end = cp_file.find(locate)
	slc = cp_file[find_end+1:]

	with open('./my_files.txt', 'wt') as wfile:
		wfile.write(slc)


if __name__ == '__main__':
	main()