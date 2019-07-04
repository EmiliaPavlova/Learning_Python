import math

pool_volume = int(input())
debit_pipe_1 = int(input())
debit_pipe_2 = int(input())
hours = float(input())

fullness = (debit_pipe_1 + debit_pipe_2) * hours
debit_pipes = debit_pipe_1 + debit_pipe_2

print(f'The pool is {math.trunc(fullness * 100 / pool_volume)}% full. '
      f'Pipe 1: {math.trunc(debit_pipe_1 / debit_pipes * 100)}%. '
      f'Pipe 2: {math.trunc(debit_pipe_2 / debit_pipes * 100)}%.'
      if fullness <= pool_volume
      else f'For {hours} hours the pool overflows with {fullness - pool_volume} liters.')
