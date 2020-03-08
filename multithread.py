from multiprocessing.dummy import Pool

class Test:
    def __init__(self):
        self.num = 2
        self.x = [1, 10, 6, 20]

    def func(self, x):
        print("num is %d" %x)

    def proc_para(self):
        def func2(x, y):
            print("num is %d" %(x+y))
        pool = Pool(2)
        # pool.map(func2, self.x)
        # pool.starmap(func2, [(1, 2), (10, 20)])

        pool.starmap(func2, enumerate(self.x))

def fun1(x):
    print("square num is %d" %(x*x))

if __name__ == "__main__":
    T = Test()
    T.proc_para()
    pool = Pool(2)
    pool.map(fun1, [1, 2, 3])