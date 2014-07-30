mmf_problem
===========
My solution's to an example problem. 

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

Running Tests
=============

This assumes you already have python, pip, and virutalenv installed.

To setup environment:

1. Create a virutal environment using virtualenv. 

  $ ``virtualenv mmf_env``
  
2. After virutalenv creation, activate environment. 

  $ ``source ./mmf_env/bin/activate``
  
3. pip install requirements.txt or simply "pip install pytest"

4. Check out the code to a preferred location. 

  $ ``git clone https://github.com/jonathangarza/mmf_problem.git``

5. Run the commands below to test. 

    $ ``time py.test -vx``
    
    Only runs Stack Test class (more efficient tests)
    
    $ ``time py.test -vx -k "Stack"``
    
    Runs all other test cases(less efficient tests)
    
    $ ``time py.test -vx -k "not Stack"``
