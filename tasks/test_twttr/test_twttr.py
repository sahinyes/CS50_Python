from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("word") == "wrd"
    assert shorten("WORD") == "WRD"
    assert shorten("WorD") == "WrD"
    assert shorten("1234") == "1234"
    assert shorten(".!?,") == ".!?,"

if __name__ == "__main__":
    main()