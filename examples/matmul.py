import time
import random
import sys


def main():
    size = int(sys.argv[1])

    a = [[random.randint(0, 100) for j in range(size)] for i in range(size)]
    b = [[random.randint(0, 100) for j in range(size)] for i in range(size)]
    c = [[random.randint(0, 100) for j in range(size)] for i in range(size)]

    print a

    print b

    for i in range(len(a)):
        for j in range(len(b)):
            sum = 0
            for k in range(len(a)):
                sum = sum + a[i][k] * b[k][j]
            c[i][j] = sum

    print c


if __name__ == '__main__':
    start = time.time()
    main()
    print str(time.time() - start) + "seconds"
