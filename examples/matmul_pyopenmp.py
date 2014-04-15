import sys
import time
import random

sys.path.insert(0, '../')
from pyopenmp.pyomp import *


def main():
    size = int(sys.argv[1])

    a = [[random.randint(0, 100) for j in range(size)] for i in range(size)]
    b = [[random.randint(0, 100) for j in range(size)] for i in range(size)]
    c = [[random.randint(0, 100) for j in range(size)] for i in range(size)]

    #create a team of processes
    @OMPParallel(numprocs=4)
    def parallel_blk(*args, **kwargs):

        # for directive to share the work
        @OMPFor(args=args, kwargs=kwargs)
        def for_blk_one(a, *args, **kwargs):
            for i in range(kwargs["start"], kwargs["end"]):
                for j in range(len(b)):
                    sum = 0
                    for k in range(len(a)):
                        sum = sum + a[i][k] * b[k][j]
                    c[i][j] = sum

        for_blk_one(a)

    parallel_blk()


if __name__ == '__main__':
    start = time.time()
    main()
    print str(time.time() - start) + "seconds"
