import math
def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

unique_antinode_locations = set()
unique_antinode_locations2 = set()
unique_antennas_that_are_paired = set()
solutions = set()
number_of_nodes_between = 0

def day8():
  input = [val.strip() for val in read_in_data('day8.txt')]
  solution_input = [val.strip() for val in read_in_data('day8_solution.txt')]

  antenna_locations = dict()
  puzzle = set()
  antenna_types = set()
  type_to_coordinate = dict()

  for row in range(len(input)):
    for column in range(len(input[row])):
      if input[row][column] != '.':
        antenna_locations[(row, column)] = input[row][column]
        antenna_types.add(input[row][column])
        if input[row][column] in type_to_coordinate:
          type_to_coordinate[input[row][column]].append((row, column))
        else:
          type_to_coordinate[input[row][column]] = [(row, column)]
      puzzle.add((row, column))

  for row in range(len(solution_input)):
    for column in range(len(solution_input[row])):
      if solution_input[row][column] != ".":
        solutions.add((row, column))

  unique_antenna_pairs = []
  for antenna_type, locations in type_to_coordinate.items():
    unique_antenna_pairs.append(calculate_uniqe_anntena_pairs(locations, puzzle))

  return (len(unique_antinode_locations), len(unique_antinode_locations2))

def calculate_uniqe_anntena_pairs(antenna_locations, puzzle):
  unique_antenna_pairs = []
  def dfs(start, current_path):
    if len(current_path) == 2:
      unique_antenna_pairs.append(current_path.copy())
      calculate_antinode_locations_p1(current_path, puzzle)
      calculate_antinode_locations_p2(current_path, puzzle)
      return
    if start >= len(antenna_locations):
      return

    current_path.append(antenna_locations[start])
    dfs(start + 1, current_path)
    current_path.pop()
    dfs(start + 1, current_path)

  dfs(0, [])
  return unique_antenna_pairs

def calculate_antinode_locations_p1(current_path, puzzle):
    # how to calculate antinodes
    antinode_row = abs(current_path[0][0] - current_path[1][0]) 
    antinode_column = abs(current_path[0][1] - current_path[1][1]) 

    # determines which 
    if current_path[0][0] > current_path[1][0] and current_path[0][1] > current_path[1][1]: 
      # if you have a positive slope, increase row while you increase column and vice versa to get + slope
      antinode_0 = current_path[0][0] + antinode_row, current_path[0][1] + antinode_column 
      antinode_1 = current_path[1][0] - antinode_row, current_path[1][1] - antinode_column 

    if current_path[0][0] < current_path[1][0] and current_path[0][1] < current_path[1][1]:
      # if you have a positive slope,
      antinode_0 = current_path[0][0] - antinode_row, current_path[0][1] - antinode_column 
      antinode_1 = current_path[1][0] + antinode_row, current_path[1][1] + antinode_column 

    if current_path[0][0] < current_path[1][0] and current_path[0][1] > current_path[1][1]: 

      # if you have a positive slope, increase row while you increase column and vice versa to get + slope
      antinode_0 = current_path[0][0] - antinode_row, current_path[0][1] + antinode_column 
      antinode_1 = current_path[1][0] + antinode_row, current_path[1][1] - antinode_column 

    if current_path[0][0] > current_path[1][0] and current_path[0][1] < current_path[1][1]: 
      # if you have a positive slope, increase row while you increase column and vice versa to get + slope
      antinode_0 = current_path[0][0] + antinode_row, current_path[0][1] - antinode_column 
      antinode_1 = current_path[1][0] - antinode_row, current_path[1][1] + antinode_column 

    if antinode_0 in puzzle:
      unique_antinode_locations.add(antinode_0)

    if antinode_1 in puzzle:
      unique_antinode_locations.add(antinode_1)

def calculate_antinode_locations_p2(current_path, puzzle):
    antinode_locations = set()

    antinode_0_row = current_path[0][0]
    antinode_0_column = current_path[0][1]
    antinode_1_row = current_path[1][0]
    antinode_1_column = current_path[1][1]

    row_distance = abs(antinode_0_row - antinode_1_row) 
    column_distance = abs(antinode_0_column - antinode_1_column) 

    unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
    unique_antinode_locations2.add((antinode_1_row, antinode_1_column))

    if antinode_0_row > antinode_1_row and antinode_0_column > antinode_1_column:
      calculate_middle_nodes(current_path, row_distance,  column_distance, 1)
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row + row_distance, antinode_0_column + column_distance 
        antinode_1_row, antinode_1_column = antinode_1_row - row_distance, antinode_1_column - column_distance

        if (antinode_0_row, antinode_0_column) in puzzle:
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        if (antinode_1_row, antinode_1_column) in puzzle:
          unique_antinode_locations2.add((antinode_1_row, antinode_1_column))
        elif (antinode_0_row, antinode_0_column) not in puzzle and (antinode_1_row, antinode_1_column) not in puzzle:
          break

    if antinode_0_row < antinode_1_row and antinode_0_column < antinode_1_column:
      calculate_middle_nodes(current_path, row_distance,  column_distance, 2)
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row - row_distance, antinode_0_column - column_distance 
        antinode_1_row, antinode_1_column = antinode_1_row + row_distance, antinode_1_column + column_distance

        if (antinode_0_row, antinode_0_column) in puzzle:
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        if (antinode_1_row, antinode_1_column) in puzzle:
          unique_antinode_locations2.add((antinode_1_row, antinode_1_column))
        elif (antinode_0_row, antinode_0_column) not in puzzle and (antinode_1_row, antinode_1_column) not in puzzle:
          break

    if antinode_0_row > antinode_1_row and antinode_0_column < antinode_1_column:
      calculate_middle_nodes(current_path, row_distance,  column_distance, 3)
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row + row_distance, antinode_0_column - column_distance 
        antinode_1_row, antinode_1_column = antinode_1_row - row_distance, antinode_1_column + column_distance

        if (antinode_0_row, antinode_0_column) in puzzle:
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        if (antinode_1_row, antinode_1_column) in puzzle:
          unique_antinode_locations2.add((antinode_1_row, antinode_1_column))
        elif (antinode_0_row, antinode_0_column) not in puzzle and (antinode_1_row, antinode_1_column) not in puzzle:
          break

    if antinode_0_row < antinode_1_row and antinode_0_column > antinode_1_column:
      calculate_middle_nodes(current_path, row_distance,  column_distance, 4)
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row - row_distance, antinode_0_column + column_distance 
        antinode_1_row, antinode_1_column = antinode_1_row + row_distance, antinode_1_column - column_distance

        if (antinode_0_row, antinode_0_column) in puzzle:
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        if (antinode_1_row, antinode_1_column) in puzzle:
          unique_antinode_locations2.add((antinode_1_row, antinode_1_column))

        elif (antinode_0_row, antinode_0_column) not in puzzle and (antinode_1_row, antinode_1_column) not in puzzle:
          break

    return antinode_locations

def calculate_middle_nodes(current_path, row_distance,  column_distance, slope_direction):

  antinode_0_row = current_path[0][0]
  antinode_0_column = current_path[0][1]
  antinode_1_row = current_path[1][0]
  antinode_1_column = current_path[1][1]

  match slope_direction:
    case 1:
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row - row_distance, antinode_0_column - column_distance
        if antinode_0_row > antinode_1_row and antinode_0_column > antinode_1_column:
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        else:
          break
    case 2:
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row + row_distance, antinode_0_column + column_distance 
        if antinode_0_row < antinode_1_row and antinode_0_column < antinode_1_column:
          print("finding antinodes", antinode_0_row, antinode_0_column)
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        else:
          break
    case 3:
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row - row_distance, antinode_0_column + column_distance 
        if antinode_0_row > antinode_1_row and antinode_0_column < antinode_1_column:
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        else:
          break
    case 4:
      while True:
        antinode_0_row, antinode_0_column = antinode_0_row + row_distance, antinode_0_column - column_distance 
        if antinode_0_row < antinode_1_row and antinode_0_column > antinode_1_column:
          unique_antinode_locations2.add((antinode_0_row, antinode_0_column))
        else:
          break
  return

print(day8())
