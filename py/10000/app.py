from subprocess import Popen, PIPE
import sys
from data import data


def main():
    proc = Popen(['python3', '100.py'], stdin=PIPE)
    for x in data:
        proc.stdin.write(x.encode('utf-8'))
main()
