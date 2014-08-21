# Twent (Time, WEather, and News in Terminal)

## About
Twent (<b>T</b>ime, <b>WE</b>ather, and <b>N</b>ews in <b>T</b>erminal) is a Python script that allows you to display time, weather, and rss feeds in a text console.

## Installtion
### Requirements

Twent uses [feedparser](https://pypi.python.org/pypi/feedparser) to parse rss feeds and [pyfiglet](https://pypi.python.org/pypi/pyfiglet/) to display time.

You need to have them installed to run twent.

### Installation and Running
```
git clone git@github.com:mikkkee/twent.git
cd twent
python twent.py 0
```

## Usage
```
usage: twent.py [-h] Flag [Flags ...]
```

`Flag`s can be numbers or `name`s of feeds you specified in config.ini. 

Numbers and `name`s cannot be used together. 

If numbers are used, the numbers corresponding to the order of rss feeds in config.ini, starting from 1.

Use `0` as `Flag` to display all feeds together.

Press `Ctrl-C` to stop twent.

## Configuration
In config.ini, you can customize the following settings:

###[rss] section

+ You can add rss feeds here, using `name = value` format. 
+ `name` can be used as a `Flag` to choose the corresponding feed when running.
+ `value` is url of the rss feed.
+ Default `value`s are [Hacker News (50 points and above)](http://feeds.feedburner.com/hacker-news-feed-50?format=rss) and [The Wall Street Journal - World News](http://online.wsj.com/xml/rss/3_7085.xml)

###[weather] section

+ `city` stands for the location code used in yahoo weather api.
+ You can find location code for you city by searching you city in yahoo weather. For example, the location code for New York is `2459115`, the corresponding url for New York is https://weather.yahoo.com/united-states/new-york/new-york-2459115/ 
+ `unit` can be `F` or `C`, case insensitive, stands for Fahrenheit or Celsius, respictively.

###[duration] section

+ `duration` stands for the time that twent should run, in minutes.
+ Default value `0` stands for running forever.

## Screenshot

![Screenshot](https://www.dropbox.com/s/cje9fjxptmauj9p/twent_screenshot.PNG?dl=1)

Using world news feed from The Wall Street Journal.
