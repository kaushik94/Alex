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
import time

time_log = []

def timer(test_code):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = test_code(*args, **kwargs)
        time_log.append(round(time.time() - start_time, 3))
        return result
    return timed

def _collect_input(content):
	m = re.findall('"""I\n(.*?)"""', content, re.DOTALL)
	if len(m):
		return m
	return None

def _collect_output(content):
	m = re.findall('"""O\n(.*?)"""', content, re.DOTALL)
	if len(m):
		return m
	return None

def _test_python_input_output(filename, inputs, outputs):
	if len(inputs) != len(outputs):
		raise ValueError('inputs and outputs should be of same length')

	results = _test_python_input(filename, inputs)
	output = []
	for index, each in enumerate(results):
		output.append(outputs[index] == each)
	return output, results, outputs

@timer
def do_it(filename, one):
	p = Popen(['python', filename], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	grep_stdout = p.communicate(input=one.encode())[0]
	# print(grep_stdout.decode())
	return grep_stdout.decode()

def _test_python_input(filename, inputs):
	results = []
	for each_input in inputs:
		results.append(do_it(filename, each_input))
	return results

@timer
def _test_python_normal(filename):
	p = Popen(['python', filename], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
	grep_stdout = p.communicate()[0]
	print(grep_stdout.decode())

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
		print
		print 'YOUR OUTPUT'
		print '==========='
		_test_python_normal(arguments['FILE_NAME'])

def _run_tests(arguments):
	return _run_python_tests(arguments)

def status(boolean):
	if boolean:
		return 'PASS'
	return 'FAIL'

def pretty_print(to_print, times):
	if to_print is None:
		return ''
	if len(to_print) is 3:
		bool_res, results, expected = to_print
		print "YOUR OUTPUT"
		print '==========='
		for each in results:
			print each
		print "EXPECTED OUTPUT"
		print '==============='
		for each in expected:
			print each
		print "PASS/FAIL (of %d testcases)"%len(results)
		print '========='
		for index, each in enumerate(bool_res):
			print 'TESTCASE %d'%(index+1), status(each), times[index], 'seconds'
	if len(to_print) is 1:
		print "YOUR OUTPUT"
		print '==========='
		print to_print[0]

def main():
	arguments = docopt(__doc__)
	if len(arguments) is not 1:
		raise ValueError('Expected 1 argument, %d given'%len(arguments))
	print 'Alex is working on ', arguments['FILE_NAME']
	print
	pretty_print(_run_tests(arguments), time_log)

if __name__ == '__main__':
	main()
