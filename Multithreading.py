import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(second):
    print(f'Sleeping for {second} second')
    time.sleep(second)
def main():
 time1=time.perf_counter()
# func(3)
# func(4)
# func(2)
 t1 = threading.Thread(target=func,args=[4])
 t2 = threading.Thread(target=func,args=[2])
 t3 = threading.Thread(target=func,args=[1])
 t1.start()
 t2.start()
 t3.start()
 t1,t2,t3.join()
 time2=time.perf_counter()
 print(time2-time1)
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1=executor.submit(func,5)
        # future2=executor.submit(func,2)
        # future3=executor.submit(func,3)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l=[2,4,1,4,2,3]
        future=executor.map(func,l)
        for results in future:
            print(results)
poolingDemo()
