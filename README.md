# Twent (Time, WEather, and News in Terminal)
Twent (<b>T</b>ime, <b>WE</b>ather, and <b>N</b>ews in <b>T</b>erminal) is a Python script that allows you to display time, weather, and rss feeds in a text console.

```
usage: twent.py [-h] Flags [Flags ...]
```

Flags can be numbers or names of feeds you specified in config.ini. 

Numbers and names cannot be used together. 

If numbers are used, the numbers corresponding to the order of rss feeds in config.ini, starting from 1.

Use 0 as flag to display all feeds together.

Press Ctrl-C to stop twent.

## Configuration
In config.ini, you can customize the following settings:

###[rss] section

+ You can add rss feeds here, using name = value format. 
+ name can be used as a flag to specify which feed to use when running.
+ value is url of the rss feed.

###[weather] section

+ city stands for the location code used in yahoo weather api.
+ You can find location code for you city by searching you city in yahoo weather. For example, the location code for New York is 2459115, the corresponding url for New York is https://weather.yahoo.com/united-states/new-york/new-york-2459115/ 
+ unit can be F or C, case insensitive, stands for Fahrenheit or Celsius, respictively.

###[duration] section

+ duration stands for the time that twent should run, in minutes.
+ Default value 0 stands for running forever.
