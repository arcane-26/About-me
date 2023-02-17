# sharing data between processes
# with Array and Value


import multiprocessing

def square(n,s,k):

    k.value=2.3


    print("printing squares")

    for i,d in enumerate(n):
        s[i]=d*d








if __name__=='__main__':

    arr=[2,4,5,6]

    result=multiprocessing.Array('i',4)
    v=multiprocessing.Value('d',0.0)

    t=multiprocessing.Process(target=square,args=(arr,result,v))

    t.start()
    t.join()

    print(result[:])
    print(v.value)
    
