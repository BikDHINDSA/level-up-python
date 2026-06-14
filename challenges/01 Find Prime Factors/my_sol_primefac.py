def get_prime_factors(num):
  fac = []
  div = 2
  while div <= num:
    if num % div == 0:
      fac.append(div)
      num = num // div
    else:
      div+=1
  return fac
print(get_prime_factors(650))

#random thought!!!
def is_prime(num):
  primes=[]
  for nu in range(2,num +1 ):
    for fac in range(2,int(num ** 0.5) + 1):
      if nu % fac == 0:
        break
    else:
      primes.append(nu)
  return f'{num in primes}! Nearest prime number is {primes[-1]}'
is_prime(76723)