def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

import re

def part_one():
  input = read_in_data('day_3.txt')[0]
  factors = [[int(inner) for inner in val.split(',')] for val in re.findall(r'mul\(([0-9]+\,[0-9]+)\)', input)]
  total = sum([vals[0] * vals[1] for vals in factors])
  return total


def part_two():
  input = read_in_data('day_3.txt')[0]
  split_input = input.split('do')
  do = True
  total = 0
  for line in split_input:
    if line[:5] == "n't()":
      do = False
    elif line[:2] == "()":
      do = True
    if do:
      factors = [[int(inner) for inner in val.split(',')] for val in re.findall(r'mul\(([0-9]+\,[0-9]+)\)', line)]
      total += sum([vals[0] * vals[1] for vals in factors])

  return total

# print(part_one())
print(part_two())

# 7668762 too low
# 4426103
# 113965544
# 135602215 too high
# 188192787 part 1