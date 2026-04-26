def roll_dice(*dices):
  from collections import Counter
  from itertools import product
  outcomes = list(product(*[range(1,sides +1)for sides in dices]))
  sums = [sum(outcome)for outcome in outcomes]
  counts = Counter(sums)
  total = len(sums)
  print(f"\n\nFor dice group:{sorted(dices)}/n")
  print("OUTCOME PROBABILITY")
  for outcome in sorted(counts):
    probability = (counts[outcome]/total) *100 
    print(f"{outcome:<7}{probability:.3f}%")

if __name__ == '__main__':
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)
    roll_dice(6,7,9,8,9)