import pytest
from um import count

def main():
    test1()



def test1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2