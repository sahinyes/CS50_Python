
# cs50 Final
#### Video Demo: https://youtu.be/n8XVfozVkgU

## Description
This is my final project for "Harvard CS50 Introduction to programming with Python". This project makes websites scraping easier. You can see quickly the comment lines or directories which the page has.

This project will also print requests and responses for you. From the URL addresse that you gave as an input, it will print the website response code from the URL link and the page sizes.

You need to be careful when you use it because it will look inside the directories which are found and sometimes it takes a lot of time and too much request. WAF (Web Application Firewall) can easily detect you, and probably you will get an IP ban.

## Installation & Use
1. Clone the code.
1. Run the command `pip install -r requirements.txt` in the app directory.
2. Than run it: `python3 ./project.py -u https://example.com`

## Overviews
```
project/ $ python3 project.py
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
|C|S|5|0| |@|s|a|h|i|n|y|e|s|
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
+-+-+-+-+-+ +-+-+-+-+-+-+-+
|F|i|n|a|l| |P|r|o|j|e|c|t|
+-+-+-+-+-+ +-+-+-+-+-+-+-+

python ./project.py
python ./project.py -u <url>
python ./project.py --url <url>

URL:
```

```
project/ $ python3 ./project.py --url https://cs50.harvard.edu/course
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
|C|S|5|0| |@|s|a|h|i|n|y|e|s|
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
+-+-+-+-+-+ +-+-+-+-+-+-+-+
|F|i|n|a|l| |P|r|o|j|e|c|t|
+-+-+-+-+-+ +-+-+-+-+-+-+-+

python ./project.py
python ./project.py -u <url>
python ./project.py --url <url>

https://cs50.harvard.edu/course Status: 404 Size: 623
# COMMENT LINES
# https://github.com/httpcats/http.cat
```
