


import multiprocessing

import mp_0
sq1=[]
def calc_square(n):
    global sq1
    print('printing squares')
    for i in n:
        sq1.append(i*i)

    print('inner process -->',sq1)


if __name__=='__main__':

    arr=[2,3,4,5]

    t1=multiprocessing.Process(target=calc_square,args=(arr,))

    t1.start()

    t1.join()

    print('outer process---->',sq1)
    # this will give empty list becoz outside the process 'calc_sq'
    # we can only access sq1 inside the calc_sq process




