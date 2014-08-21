#!/usr/bin/env python
from __future__ import print_function
import sys
import subprocess
import datetime
import time
import string
import argparse
import ConfigParser
from urllib import urlencode
import feedparser
from pyfiglet import Figlet

def clear_console():
  '''
  Clear previous screen.
  '''
  subprocess.call(['clear'])

def read_config():
  '''
  Read configuration from config.ini.
  See config.ini for details on configuration.
  '''
  config = ConfigParser.ConfigParser()
  config.read('config.ini')
  city_code = config.get('weather','city')
  unit = config.get('weather','unit')
  duration = config.get('duration','duration')
  rss_list = config.items('rss')
  return city_code,unit,int(duration),rss_list

def weather_now(code,unit):
  '''
  Get weather for city represented by code.
  '''
  yahoo_api = 'http://weather.yahooapis.com/forecastrss?'
  para = {'w': code, 'u': unit.lower()}
  feed_url = yahoo_api + urlencode(para)
  f = feedparser.parse(feed_url)
  f_entries = f['entries']
  f_forecast = f_entries[0]['yweather_forecast']
  weather_heading = '=============Weather==============\n'
  weather_details = "{f[text]} {f[low]}{c}-{f[high]}{c} Singapore\n".format(
    f=f_forecast,
    c=u'\u00b0'.encode('utf-8')
    )
  return (weather_heading + weather_details).decode('utf-8')
  
def time_now():
  '''
  Return current time in Figlet format.
  '''
  time_heading = '===============Time===============\n'
  now = datetime.datetime.now().strftime("%H:%M")
  f = Figlet(font='doom')
  time_details = f.renderText(now).rstrip() + '\n'
  return (time_heading + time_details).decode('utf-8')

def read_rss(rss_list,num,width):
  '''
  Return rss titles from rss in rss_list.
  Sort items from newest to oldest.
  Cut number of items to fit window height.
  '''
  rss = []
  for item in rss_list:
    source,url = item[0],item[1]
    f = feedparser.parse(url)
    f_entries = f['entries']
    for x in f_entries:
      title = x['title'][:width - len(source + ': ')].replace('\n',' ')
      rss.append((x['published_parsed'],title,source))
  rss.sort(key=lambda x: x[0],reverse=True)
  return rss[:num]

def news_now(rows,columns,rss_list,rss_option):
  '''
  Return newest feed titles from given urls.
  Number of feeds to return is determined by console height.
  '''
  rss_dict = {x:y for (x,y) in rss_list}
  f_num = rows - 8 - 1 - 3
  if all([x in string.digits for x in rss_option]):
    rss_option = [int(x) for x in rss_option]
    if len(rss_option) == 1:
      if rss_option[0] == 0:
        feed_list = rss_list
        feed_content = read_rss(feed_list,f_num,columns)
      else:
        feed_list = [rss_list[rss_option[0] - 1]]
        feed_content = read_rss(feed_list,f_num,columns)
    else:
      feed_list = [x for x in rss_list if rss_list.index(x)+1 in rss_option]
      feed_content = read_rss(feed_list,f_num,columns)
  else:
    try:
      feed_list = [(x,rss_dict[x]) for x in rss_option]
      feed_content = read_rss(feed_list,f_num,columns)
    except KeyError as e:
      sys.exit('Invalid Flag: ' + e.message)
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise

  news_heading = '===============News===============\n'
  news_details = ''
  for entry in feed_content:
    news_details += '{srs}: {title}\n'.format(srs=entry[2].encode('utf-8'),title=entry[1].encode('utf-8'))
  return (news_heading + news_details).decode('utf-8')

def console_size():
  '''
  Return current console size.
  To be used to determine number of feeds to display.
  '''
  p = subprocess.Popen(['stty','size'],stdout=subprocess.PIPE)
  rows, columns = [int(x) for x in p.stdout.read().split()]
  return rows,columns

def main(argv):
  parser = argparse.ArgumentParser(description='Feed choose flags.')
  parser.add_argument('flags',metavar='Flags',type=str,nargs='+',
		      help='numbers or names of feeds.')
  args = parser.parse_args(argv[1:])
  rss_option = args.flags
  city_code,unit,duration,rss_list = read_config()
  end = time.time() + duration * 60
  try:
    while time.time() < end if duration !=0 else True:
      rows,columns = console_size()
      now = time_now()
      weather = weather_now(city_code,unit)
      news = news_now(rows,columns,rss_list,rss_option)
      content = weather + now + news
      clear_console()
      print(content)
      time.sleep(60)
    else:
      sys.exit('Time up. Exit now.')
  except KeyboardInterrupt:
    sys.exit(1)
if __name__ == '__main__':
  main(sys.argv)
