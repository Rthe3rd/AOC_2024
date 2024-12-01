# with open("filename.txt", "r") as file:
#     content = file.read()
#     print(content)

import re

def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

input_data = read_in_data("day1_input.txt")

def part_one():
  left = []
  right = []
  for line in input_data:
    left.append(int(line.strip().split()[0]))
    right.append(int(line.strip().split()[1]))

  left = sorted(left)
  right = sorted(right)

  difference = 0
  for i in range(len(left)):
    difference += abs(left[i] - right[i])

  return difference, set(left), right

def part_two():
  left_set = part_one()[1]
  right = part_one()[2]
  count = 0
  running_sum = 0
  counter = dict()
  for val in right:
    if not val in counter:
      counter[val] = 1
    else:
      counter[val] += 1

  for val in left_set:
    if val in counter:
      running_sum += val * counter[val] 

  return running_sum
print(part_two())

