'''
Fibonacci Sequence
-------------------------------------------------------------
'''

fib_cache = {}


def fib_memo(input_val):
   if input_val in fib_cache:
       print(f"fib_cache: {fib_cache} \n\n")
       return fib_cache[input_val]

   if input_val == 0:
       val = 0
   elif input_val < 2:
       val = 1
   else:
       val = fib_memo(input_val - 1) + fib_memo(input_val - 2)

   fib_cache[input_val] = val
   print(f"Fib_cache end {fib_cache} \n")
   return val


if __name__ == '__main__':
   print('======== Fibonacci Series ========')
   for i in range(1, 5):
       print(f'\nFibonacci ({i}) : {fib_memo(i)}')