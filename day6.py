def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()
  
positions = set()
def day6():

  coordinates_features_hash, starting_postion, puzzle = generate_coordinates_from_features()
  in_bounds = True
  walking_direction = "up"
  current_location = starting_postion
  positions.add(starting_postion)
  coordinates_directions_taken = set((*current_location, walking_direction))

  # coordinates_directions_taken.add((*current_location, walking_direction))

  # part 1
  while in_bounds:
    current_location, walking_direction, in_bounds, looped = move_gaurd(current_location, walking_direction, coordinates_features_hash, coordinates_directions_taken)
  
  solution_1_positions = len(positions.copy()) + 1

  # part 2
  potential_looping_puzzle = coordinates_features_hash.copy()
  blocks_that_will_loop = 0

  in_bounds = True
  looped = False
  current_location = starting_postion
  walking_direction = "up"

  # loop through all the positions in the puzzle
  for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):

      # When you find a space that could potentially have a new obstruction, put it there and run the simulation
      if potential_looping_puzzle[(row, column)] == ".":
        potential_looping_puzzle[(row, column)] = "#"
        coordinates_directions_taken = set((*current_location, walking_direction))

        # The new block could result in a loop, what we want, so add a check that will break the while loop if this is the case
        while in_bounds and not looped:
          current_location, walking_direction, in_bounds, looped = move_gaurd(current_location, walking_direction, potential_looping_puzzle, coordinates_directions_taken)
        if looped:
          blocks_that_will_loop += 1
        potential_looping_puzzle[(row, column)] = "."
        # after you have tested placing a # at a spot, reset your initial vals
        potential_looping_puzzle[(row, column)] = "."
        current_location, walking_direction, in_bounds, looped = starting_postion, "up", True, False
  return solution_1_positions, blocks_that_will_loop

def generate_coordinates_from_features():
  puzzle = read_in_data('day6.txt')
  puzzle = [val.strip() for val in puzzle]
  coordinates_features_hash = dict()
  for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):
      coordinates_features_hash[(row, column)] = puzzle[row][column]
      if puzzle[row][column] == "^":
        starting_position = (row, column)
  return coordinates_features_hash, starting_position, puzzle.copy() 

def move_gaurd(current_location, walking_direction, current_puzzle, coordinates_directions_taken):
  looped = False
  in_bounds = True
  row = current_location[0]
  column = current_location[1]
  walking_switch = {
    "up":"right",
    "right":"down",
    "down":"left",
    "left":"up",
  }

  match walking_direction:
    case "left":
      while current_puzzle[row, column - 1] != "#":
        positions.add((row, column))
        column -= 1
        if not (row, column - 1) in current_puzzle:
            in_bounds = False
            break
    case "right":
      while current_puzzle[row, column + 1] != "#":
        positions.add((row, column))
        column += 1
        if not (row, column + 1) in current_puzzle:
            in_bounds = False
            break
    case "down":
      while current_puzzle[row + 1, column] != "#":
        positions.add((row, column))
        row += 1
        if not (row + 1, column) in current_puzzle:
            in_bounds = False
            break
    case "up":
      while current_puzzle[row - 1, column ] != "#":
        positions.add((row, column))
        row -= 1
        if not (row - 1, column) in current_puzzle:
            in_bounds = False
            break

  walking_direction = walking_switch[walking_direction]
  current_location = (row, column)

  if (*current_location, walking_direction) in coordinates_directions_taken:
    looped = True

  coordinates_directions_taken.add((*current_location, walking_direction))

  return current_location, walking_direction, in_bounds, looped

print(day6())