import pylint

options = ["--disable=unnecessary-lambda,missing-function-docstring", 'part1.py']
pylint.run_pylint(argv=options)
