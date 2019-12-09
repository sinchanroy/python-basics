#! /usr/bin/env python 

import threading 
import time
import logging

 
def hithread():
 print("\n Hi method with T1 thread and time is :" +  time.ctime(time.time()))

def hellothread():
 print("\n Hello Method with T2 thread and time is :" +  time.ctime(time.time()))



if __name__ == "__main__":
 
 for i in range(100):
  t1 = threading.Thread(target = hithread)
  t2 = threading.Thread(target = hellothread)
  
 #for i in range(100):
  t1.start()
  t2.start()

 t1.join()
 t2.join()

 print("Done")


