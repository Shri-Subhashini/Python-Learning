import os
os.getcwd()  # return current working directory
# os.chdir('/server/accesslogs')  # change current working directory
# os.system('mkdir today')   # make directory ; today name of the directory; os.system() - run system shell commands; not recommended
# os.mkdir('tomorrow') # if already exist error occur
os.makedirs('today', exist_ok = True)

import shutil
shutil.copyfile('file1.txt', 'newfile.txt') # Copies content of file1.txt to newfile.txt
# shutil.move('today', 'file3') # changed today directory to file3.txt
# shutil.move('file3', 'Shutil_folder')
# shutil.move('today/file.txt', 'newResult.txt') # changing today/file.txt to newResult.txt; so this file came out from today folder

#FILE WILDCARDS
import glob
print(glob.glob('*.py')) # list all the files in the current working directory which have .py extension as a list


# Error Output Redirection and Program Termination 
import sys
sys.stderr.write('Warning, log file not started')  #  useful for emitting warnings and error messages to make them visible even when stdout has been redirected.
# sys.exit() # to terminate a script; Immediately terminates the program.


# String Pattern Matching
import re 
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')) 
# r before string - raw string; r"\n" treated as 2 characters-\ and n; "\n" treated as newline character; \b - word boundry matches position where word starts or ends. f - matches literal character(first character should be); [a-z] - matches zero or more lowercase letters; * - matches zero or more of preceding character;
print('tea for too'.replace('too', 'two'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', ' a cat in the the a hat hat'))
# re.sub(pattern, replacement, string)


#Mathematics

import math 
print(math.cos(math.pi/4))
print(math.log(1024, 2))

#random

import random
print(random.choice(['orange', 'apple', 'pineapple'])) # select 1 irandom item
print(random.sample(range(100), 10))   # randomly select 10 unique numbers from 0 to 99; select multiple random items; no duplicates in a list
print(random.random())
print(random.randrange(7))

#statistics

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

#Internet Access

'''
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())

import smtplib 
server = smtplib.SMTP('localhost')
server.sendmail('skumarvel@msystechnologies.com', 'subha.krs7@gmail.com',
"""To: subha.krs7@gmail.com
From: skumarvel@msystechnologies.com

Beware the Ides of March.
""")
server.quit()

'''


# Date and Time 
from datetime import date 
now = date.today()
print("Today's date: ", now)
print(now.strftime("%m-%d. %d %b %Y is a %A on the %d day of %B."))
# %d - date; %m - month in numbers; %Y - year; %A - days; %b - Apr, Jun,Jan, Aug; %B - April, August, May
birthday = date(1999, 8, 27)
age = now - birthday
print(age.days)

#Date Compression 
import zlib
s = b'witch which has which witches wrist watch' # encoded as byte object
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s)) # Cyclic Redundancy Check, produces 32 bit integer hash value

#Performance Measurement
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1;b=2').timeit())
print(Timer('a,b = b,a', 'a=1;b=2').timeit())

#Quality control

def average(values):
    return sum(values)/ len(values)
print(average([20,30,40]))
import doctest
doctest.testmod()