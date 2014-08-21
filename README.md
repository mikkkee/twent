# Twent (Time WEather News in Terminal)
Twent (Time WEather News in Terminal) is a Python script that allows you to display time, weather, and rss feeds in text console.

usage: twent.py [-h] Flags [Flags ...]

Flags can be numbers or names of feeds you specified in config.ini

Use 0 to display all feeds together.

Press Ctrl-C to stop twent.

## Configuration
In config.ini, you can customize the following settings:

1. You can add rss feeds under [rss] section, using name = rss_url format.
2. In [weather] section, city stands for your city_code used in yahoo weather api. You can find code for your city by search it in yahoo weather. 'unit' can be F or C, corresponding to Fahrenheit and Celsius, respectively. 
3. In [duration] section, you can specify how long twent will run, in minutes. The default is 0, stands for running forever.
