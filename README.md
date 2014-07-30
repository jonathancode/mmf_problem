mmf_problem
===========



$ time py.test -vx

Only runs Stack Test class (more efficient tests)

$ time py.test -vx -k "Stack"

Runs all other test cases(less efficient tests)

$ time py.test -vx -k "not Stack"
