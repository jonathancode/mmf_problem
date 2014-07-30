mmf_problem
===========

To setup environment:
1. Create a virutal environment using virtualenv. 

  $ virtualenv mmf_env
  
2. After virutalenv creation, activate environment. 

  $ ``source ./mmf_env/bin/activate``
  
3. pip install requirements.txt or simply "pip install pytest"

4. Run the commands below to test. 

    $ time py.test -vx
    
    Only runs Stack Test class (more efficient tests)
    
    $ time py.test -vx -k "Stack"
    
    Runs all other test cases(less efficient tests)
    
    $ time py.test -vx -k "not Stack"
