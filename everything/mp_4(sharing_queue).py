import multiprocessing

def sq(n,q):
    for i in n:
        q.put(i*i)


if __name__=='__main__':

    arr=[2,3,4,5]

    q=multiprocessing.Queue()

    t=multiprocessing.Process(target=sq,args=(arr,q))

    t.start()
    t.join()

    while q.empty() is False:
        print(q.get())