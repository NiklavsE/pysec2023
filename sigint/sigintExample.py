import sys
import time
import signal
import math


def sigintHandler(signum, frame):
    print('Received CTRL+C signal, stopping.')
    sys.exit(0)


def main():
    n1, n2 = 0, 1
    print('The Fibonacci sequence is as follows:')

    while True:
        print(n1)
        time.sleep(1)
        nth = n1 + n2
        n1 = n2
        n2 = nth


if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigintHandler)
    main()
