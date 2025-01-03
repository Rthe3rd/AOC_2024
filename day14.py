import time
import re
def read_in_file(file_name):
  with open(file_name, 'r') as file:
    data = []
    for line in file.readlines():
      data.append(line.strip())
  return data


def day14():
  data = read_in_file('day14_full.txt')

  positions = [(int(re.findall(r'p=(\d+),', val)[0]), int((re.findall(r',(\d+)', val))[0])) for val in data]
  velocities = [(int(re.findall(r'v=(.*\d+),', val)[0]), int((re.findall(r'v=.*\d+,(.*\d+)', val))[0])) for val in data]
  number_of_rows = 103
  number_of_cols = 101

  final_position = []

  for i in range(len(velocities)):
    row_velocity = velocities[i][1]
    col_velocity = velocities[i][0]
    row_position = positions[i][1]
    col_position = positions[i][0]

    final_row = (row_velocity * 100 + row_position) % number_of_rows 
    final_col = (col_velocity * 100 + col_position) % number_of_cols

    if final_row != number_of_rows // 2 and final_col != number_of_cols // 2:
      final_position.append((final_col, final_row))

  q1 = 0
  q2 = 0
  q3 = 0
  q4 = 0

  for val in final_position:
    final_col, final_row = val[0], val[1]
    if final_row < number_of_rows // 2 and final_col < number_of_cols // 2:
      q1 += 1
    if final_row < number_of_rows // 2 and final_col > number_of_cols // 2:
      q2 += 1
    if final_row > number_of_rows // 2 and final_col < number_of_cols // 2:
      q3 += 1
    if final_row > number_of_rows // 2 and final_col > number_of_cols // 2:
      q4 += 1

  return q1*q2*q3*q4


def day14p2():
  data = read_in_file('day14_full.txt')
  p2_final_positions = []
  positions = [(int(re.findall(r'p=(\d+),', val)[0]), int((re.findall(r',(\d+)', val))[0])) for val in data]
  velocities = [(int(re.findall(r'v=(.*\d+),', val)[0]), int((re.findall(r'v=.*\d+,(.*\d+)', val))[0])) for val in data]
  number_of_rows = 103
  number_of_cols = 101

  for number_of_seconds in range(7687, 7688):
    p2_final_positions_set = set()
    
    for i in range(len(velocities)):
      row_velocity = velocities[i][1]
      col_velocity = velocities[i][0]
      row_position = positions[i][1]
      col_position = positions[i][0]


      final_row = (row_velocity * number_of_seconds + row_position) % number_of_rows 
      final_col = (col_velocity * number_of_seconds + col_position) % number_of_cols 

      p2_final_positions_set.add((final_col, final_row))

    p2_final_positions.append(p2_final_positions_set)

  for val in p2_final_positions:
    for i in range(number_of_rows):
      line = ''
      for j in range(number_of_cols):
          if (j, i) in val:
            line += '0'
          else:
            line += ' '
      print(line)

print(day14())
print(day14p2())