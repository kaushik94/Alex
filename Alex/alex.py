#! /usr/bin/env python
"""
Usage:
  alex FILE_NAME

Arguments:
  FILE        input file

"""

from docopt import docopt
from subprocess import Popen, PIPE, STDOUT, call
import re

def _collect_input(content):
	m = re.findall('"""I\n(.*?)\n"""', content, re.DOTALL)
	if len(m):
		return m
	return None

def _collect_output(content):
	m = re.findall('"""O\n(.*?)\n"""', content, re.DOTALL)
	if len(m):
		return m
	return None

def _test_python_input_output(filename, inputs, outputs):
	pass

def do_it(filename, one):
	p = Popen(['python', filename], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
	grep_stdout = p.communicate(input=one)[0]
	print(grep_stdout.decode())

def _test_python_input(filename, inputs):
	for each_input in inputs:
		do_it(filename, each_input)

def _test_python_normal(filename):
	return call(['python', filename])

def _run_python_tests(arguments):
	fp = open(arguments['FILE_NAME'], 'r')
	content = fp.read()
	inputs = _collect_input(content)
	outputs = _collect_output(content)
	# print inputs, outputs
	if inputs or outputs:
		if outputs and inputs:
			return _test_python_input_output(arguments['FILE_NAME'], inputs, outputs)
		if inputs:
			return _test_python_input(arguments['FILE_NAME'], inputs)
	else:
		print 'No test cases were provided so running as is'
		return  _test_python_normal(arguments['FILE_NAME'])

def _run_tests(arguments):
	return _run_python_tests(arguments)

def main():
	arguments = docopt(__doc__)
	if len(arguments) is not 1:
		raise ValueError('Expected 1 argument, %d given'%len(arguments))
	print 'Running tests on ', arguments['FILE_NAME']
	_run_tests(arguments)

if __name__ == '__main__':
	main()
