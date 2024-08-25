import sys
import os

# Add the root directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import average

def test_average():
    assert average([2,4]) == 3

def test_average2():
    assert average([4,6]) == 4
