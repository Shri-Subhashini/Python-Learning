#Command Line Arguments

import argparse
parser = argparse.ArgumentParser(
    prog = "top",
    description = 'Display top 5 lines from each file'
   )
parser.add_argument('filenames', nargs = '+')
parser.add_argument('-l','--lines', type=int, default = 7)
args = parser.parse_args()
print(args)  # Namespace(filenames=['file1.txt', 'file2.txt'], lines=1)
# To run: python top.py --lines=1 file1.txt file2.txt