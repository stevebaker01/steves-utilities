import pytest
import os
import re
import subprocess

def test_profiler():
    # TODO: modify test to cover python 2 and python 3.5
    # http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    # weird stuff to subprocess the running of the test method so that stdout can be captured
    # this implementation only works with python3.4
    # perhaps if/then to test other versions
    f = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'profiler.py')
    c = 'from importlib.machinery import SourceFileLoader as sfl; '
    c += 'm = sfl("steves_utilities.profiler", "{}").load_module(); '.format(f)
    c += 'm.waste_time(10000000)'
    # run the method, capture stdout and compare
    o = subprocess.Popen(['python3', '-c', c], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    match = re.compile(r"waste_time \(\(10000000,\), \{\}\) \d+\.\d{6} sec").match(o.strip())
    assert(True if match else False)
