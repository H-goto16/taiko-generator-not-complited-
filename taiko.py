from timeout_decorator import timeout, TimeoutError
import time

def taiko():
    print("input bpm")
    bpm_get = int(input())

    if bpm_get < 400:
      division_second = bpm_get / 120
      print(division_second)
      
      for i in range(4):
        time.sleep(1)
        print(3 - i)

      time.sleep(1)
      print("start")

      for j in range(100):

        data = input()

        if data == "f" or "k":
          print(1) 
        elif data == "d" or "k":
          print(2)
        else:
          print(0)


    else:
      print('You must check your numbers')
taiko()