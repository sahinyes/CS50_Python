from project import is_regex, req, url_valid
import pytest

def main():
    test_is_regex()
    test_req()
    test_url_valid()


@pytest.fixture(autouse=True)
def mock_args(monkeypatch):
    monkeypatch.setattr("sys.argv", ["pytest", "example_input"])

#With not enought or more argument
def test_url_valid():
    with pytest.raises(SystemExit, match="Should be three argument <<python ./project -u or --url >>"):
        url_valid()

#Input validation 
def test_is_regex():
    assert is_regex("http") == False
    assert is_regex("https") == False
    assert is_regex("www.sahinyes.com") == False
    assert is_regex("http:/www.sahinyes.com") == False

#If website doesnt give some responses or errors
def test_req():
    #Example for valid website
    assert req("https://www.sahinyes.com") == (None, None, True)

    with pytest.raises(SystemExit, match="Cannot not request to website"):
        req("invalidwebsite.comq")
        req("htpp://invalidwebsite.com")
        req("www.invalidwebsite.com")
    
        
if __name__ == "__main__":
    main()