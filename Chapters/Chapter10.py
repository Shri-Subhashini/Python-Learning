import os
os.getcwd()  # return current working directory
# os.chdir('/server/accesslogs')  # change current working directory
# os.system('mkdir today')   # make directory ; today name of the directory; os.system() - run system shell commands; not recommended
# os.mkdir('tomorrow') # if already exist error occur
os.makedirs('today', exist_ok = True)

import shutil
shutil.copyfile('file1.txt', 'newfile.txt') # Copies content of file1.txt to newfile.txt
# shutil.move('today', 'file3') # changed today directory to file3.txt
# shutil.move('file3.txt', 'Shutil_folder')
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

import random
print(random.choice(['orange', 'apple', 'pineapple']))
print(random.sample(range(100), 10))   # randomly select 10 unique numbers from 0 to 99




