import multiprocessing
import time


def calcsq(numbers):
    print('printing squares')
    for i in numbers:
        time.sleep(5)
        print('square: ', i * i)


def calcub(numbers):
    print('printing cubes')
    for i in numbers:
        time.sleep(5)
        print('cubes: ', i * i * i)


if __name__ == '__main__':
    arr = [4, 6, 7, 2]

    mp1 = multiprocessing.Process(target=calcsq, args=(arr,))
    mp2 = multiprocessing.Process(target=calcub, args=(arr,))

    mp1.start()
    mp2.start()

    mp1.join()
    mp2.join()

    print('done')

