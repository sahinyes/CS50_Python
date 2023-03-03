import pytest
from seasons import diff

def main():
    test()

def test():
    assert diff("2022-01-20") == "Five hundred twenty-five thousand, six hundred minutes"
    assert diff("2021-01-20") == "One million, fifty-one thousand, two hundred minutes"
    with pytest.raises(SystemExit, match="Invalid"):
        diff("Januar 6th, 1998")



if __name__ == "__main__":
    main()




