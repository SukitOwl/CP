from subprocess import Popen, PIPE
import sys
from data import data


def main():
    proc = Popen(['python3', '100.py', stdin=PIPE)

    # input_data = '{} {}'.format(sys.argv[1], sys.argv[2])
    # proc.stdin.write(input_data.encode('utf-8'))
    for x in data:
        proc.stdin.write(x.encode('utf-8'))

main()
