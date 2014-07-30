'''
	** Modified **
	Added '<>' and '{}' to solution
	Optimized code to use the Stack data structure. 

	To Test code runtimes, execute the followinging in terminal
		time python mmf_jesse.py

	Write a program that determines if a string is valid or invalid. In lieu of
	a formal definition, generalize from the following examples.

	Examples of valid strings include:

	[]
	()
	()[]
	a(b[c]d)e
	[[[((()))]]]
	([([])])
	 
	Examples of invalid strings include:

	([([)])
	[
	)
	[(])
	asdfasdf]]]
	(((adsfb]]]

	For example, a command-line program is-string-valid, should produce the 
	following outputs for the given inputs:

	$ is-string-valid '[]'
	true
	$ is-string-valid '['
	false
'''

# First attempt
GOOD_PAIRINGS = ['[',']','(',')', '<', '>', '{', '}']
def is_string_valid_v1(s):
	'''
	Test if a string has valid open and closing brackets
	'''
	# Remove all other non-test case characters. Only keep GOOD_PAIRINGS 
	f = filter(lambda x: x in GOOD_PAIRINGS, s)

	# Loop and remove all valid pairings
	for i in range(0, len(s)/2):
		f = f.replace('[]', '').replace('()', '').replace("{}", "")

	return not f

# Optimized Code using STACK data structure
# Group pairing in dict key/value pairs
GOOD_PAIRINGS_DICT = {'(': ')', '<': '>', '[': ']', '{': '}'}
CLOSING_VALUES = GOOD_PAIRINGS_DICT.values()

def is_string_valid(test_str):
	'''
	This function utilizes the stack data structure to validate strings with
	the GOOD_PAIRINGS_DICT.

	'''
	stack = []
	for ch in test_str:
		close_pair = GOOD_PAIRINGS_DICT.get(ch, None)
		if close_pair:
			stack.append(close_pair)
		elif ch in CLOSING_VALUES:
			# check if no opening pairings
			if not stack:
				return False
			# Check if proper value has proper CLOSING_VALUES
			elif ch != stack.pop():
				return False

	return not stack


# Test Cases
test_pass = ['[]', '()', '()[]', 'a(b[c]d)e', '[[[((()))]]]', '([([])])', '{[]}']
test_fail = ['([([)])' , '[', ']', '(', '[(])', 'asdfasdf]]]', '(((adsfb]]]', '{{[()]}']


def main():
	pass

if __name__ == '__main__':
	main()