from plates import is_valid

def main():
    test_isvalid1()
    test_isvalid2()
    test_isvalid3()


def test_isvalid1():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False
    assert is_valid("a") == False
    assert is_valid("A") == False

def test_isvalid2():
    assert is_valid("some word") == False
    assert is_valid("cs50") == True
    assert is_valid(".!") == False
    assert is_valid("cs50!") == False
    assert is_valid("cs 50") == False
    assert is_valid("cs05") == False


def test_isvalid3():
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFABC") == False
    assert is_valid("AAA111") == True
    assert is_valid("111AAA") == False
    assert is_valid("AAA11A") == False
    assert is_valid("AAA11") == True

if __name__ == "__main__":
    main()