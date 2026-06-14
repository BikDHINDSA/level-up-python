import time
import random
def waiting_game():

  wait_time = random.randint(2,4)
  print(f"Your target time is {wait_time} seconds")
  input("---Press Enter to Begin---")
  start = time.perf_counter()
  input(f"...Press Enter again after {wait_time} seconds...")
  end = time.perf_counter()
  elapsed = end - start
  print(f"Elapsed time: {elapsed:.3f} seconds")
  diff = elapsed - wait_time
  if abs(diff)<0.2:
    print(f"You are right on target!!!")
  elif diff < 0:
    print(f"You are {abs(diff):.3f} seconds too fast!!!")
    
  else:
    print(f"You are {diff:.3f} seconds too late!!!")
if __name__ == '__main__':
  waiting_game()