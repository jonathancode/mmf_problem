'''
Common fixtures used in pytest tests.
'''

import pytest


# PyTest Fixtures
@pytest.fixture(scope="module")
def pass_list(request):
	'''Returns a list of good strings
	'''

	return ['[]', '()', '()[]', 'a(b[c]d)e', '[[[((()))]]]', '([([])])', '{[]}',]

@pytest.fixture(scope="module")
def fail_list(request):
	'''Returns a list of bad strings
	'''

	return ['([([)])' , '[', ']', '(', '[(])', 'asdfasdf]]]', '(((adsfb]]]', '{{[()]}']
