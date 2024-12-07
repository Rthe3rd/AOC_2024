def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

def part_1():
  puzzle = [val.strip() for val in read_in_data('day4.txt')]
  coordinate_to_letter = dict()
  letter_to_coordinate = dict()
  for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):
      coordinate_to_letter[(row, column)] = puzzle[row][column]
      if not puzzle[row][column] in letter_to_coordinate:
        letter_to_coordinate[puzzle[row][column]] = [[row, column]]
      else:
        letter_to_coordinate[puzzle[row][column]].append([row, column])

  count = 0
  for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):
      if puzzle[row][column] == "X":
        count += 1

  valid_m_path = []
  for coordinates in letter_to_coordinate["X"]:
    good_pair = touches_letter(coordinates, coordinate_to_letter, "M")
    if good_pair:
      [valid_m_path.append((val[0], val[1], val[2])) for val in good_pair]

  valid_a_path = []
  for coordinates in valid_m_path:
    good_pair = touches_letter_direction(coordinates, coordinate_to_letter,  "A")
    if good_pair:
      [valid_a_path.append((val[0], val[1], val[2])) for val in good_pair]

  valid_s_path = []
  for coordinates in valid_a_path:
    good_pair = touches_letter_direction(coordinates, coordinate_to_letter,  "S")
    if good_pair:
      [valid_s_path.append((val[0], val[1], val[2])) for val in good_pair]

  return len(valid_s_path)

# take in coordinate pair and return a boolean if there is a "touching" the next letter 
  # as well as the coordinates of M's 
def touches_letter(coordinates, coordinate_to_letter, letter_to_check):
  good_pair = []
  row = coordinates[0]
  column = coordinates[1]

  if (row + 0, column + 1) in coordinate_to_letter and coordinate_to_letter[row + 0, column + 1] == letter_to_check:
    good_pair.append([row + 0, column + 1, 1])

  if (row + 1, column + 0) in coordinate_to_letter and coordinate_to_letter[row + 1, column + 0] == letter_to_check:
    good_pair.append([row + 1, column + 0, 2])

  if (row + 1, column + 1) in coordinate_to_letter and coordinate_to_letter[row + 1, column + 1] == letter_to_check:
    good_pair.append([row + 1, column + 1, 3])

  if (row + 0, column + -1) in coordinate_to_letter and coordinate_to_letter[row + 0, column + -1] == letter_to_check:
    good_pair.append([row + 0, column + -1, 4])

  if (row + -1, column + 0) in coordinate_to_letter and coordinate_to_letter[row + -1, column + 0] == letter_to_check:
    good_pair.append([row + -1, column + 0, 5])

  if (row + -1, column + -1) in coordinate_to_letter and coordinate_to_letter[row + -1, column + -1] == letter_to_check:
    good_pair.append([row + -1, column + -1, 6])

  if (row + 1, column + -1) in coordinate_to_letter and coordinate_to_letter[row + 1, column + -1] == letter_to_check:
    good_pair.append([row + 1, column + -1, 7])

  if (row + -1, column + 1) in coordinate_to_letter and coordinate_to_letter[row + -1, column + 1] == letter_to_check:
    good_pair.append([row + -1, column + 1, 8])

  return good_pair

def touches_letter_direction(coordinates, coordinate_to_letter, letter_to_check):
  good_pair = []
  row = coordinates[0]
  column = coordinates[1]
  direction = coordinates[2]

  match direction:
    case 1:
      if (row + 0, column + 1) in coordinate_to_letter and coordinate_to_letter[row + 0, column + 1] == letter_to_check:
        good_pair.append([row + 0, column + 1, 1])

    case 2:
      if (row + 1, column + 0) in coordinate_to_letter and coordinate_to_letter[row + 1, column + 0] == letter_to_check:
        good_pair.append([row + 1, column + 0, 2])

    case 3:
      if (row + 1, column + 1) in coordinate_to_letter and coordinate_to_letter[row + 1, column + 1] == letter_to_check:
        good_pair.append([row + 1, column + 1, 3])

    case 4:
      if (row + 0, column + -1) in coordinate_to_letter and coordinate_to_letter[row + 0, column + -1] == letter_to_check:
        good_pair.append([row + 0, column + -1, 4])

    case 5:
      if (row + -1, column + 0) in coordinate_to_letter and coordinate_to_letter[row + -1, column + 0] == letter_to_check:
        good_pair.append([row + -1, column + 0, 5])

    case 6:
      if (row + -1, column + -1) in coordinate_to_letter and coordinate_to_letter[row + -1, column + -1] == letter_to_check:
        good_pair.append([row + -1, column + -1, 6])

    case 7:
      if (row + 1, column + -1) in coordinate_to_letter and coordinate_to_letter[row + 1, column + -1] == letter_to_check:
        good_pair.append([row + 1, column + -1, 7])

    case 8:
      if (row + -1, column + 1) in coordinate_to_letter and coordinate_to_letter[row + -1, column + 1] == letter_to_check:
        good_pair.append([row + -1, column + 1, 8])

  return good_pair


def part_2():
  puzzle = [val.strip() for val in read_in_data('day4.txt')]
  coordinates_to_letter = dict()
  letter_to_coordinate = dict()
  for row in range(len(puzzle)):
    for column in range(len(puzzle[row])):
      coordinates_to_letter[(row, column)] = puzzle[row][column]
      if not puzzle[row][column] in letter_to_coordinate:
        letter_to_coordinate[puzzle[row][column]] = [[row, column]]
      else:
        letter_to_coordinate[puzzle[row][column]].append([row, column])
  count = 0
  for coordinates in letter_to_coordinate["A"]:
    count += check(coordinates, coordinates_to_letter)
  return count

def check(coordinates, coordinates_to_letter):
  count = 0
  row = coordinates[0]
  column = coordinates[1]
  top_left = (row - 1, column - 1)
  top_right = (row - 1, column + 1)
  bottom_left = (row + 1, column - 1)
  bottom_right = (row + 1, column + 1)
  # if coordinates are "in bounds"
  if top_left in coordinates_to_letter and top_right in coordinates_to_letter and bottom_left in coordinates_to_letter and bottom_right in coordinates_to_letter:
    # check cases
    if coordinates_to_letter[top_left] == coordinates_to_letter[top_right] and coordinates_to_letter[top_left] == "M" and coordinates_to_letter[bottom_left] == coordinates_to_letter[bottom_right] == "S":
      count += 1

    if coordinates_to_letter[top_left] == coordinates_to_letter[bottom_left] and coordinates_to_letter[top_left] == "M" and coordinates_to_letter[top_right] == coordinates_to_letter[bottom_right] == "S":
      count += 1

    if coordinates_to_letter[top_left] == coordinates_to_letter[top_right] and coordinates_to_letter[top_left] == "S" and coordinates_to_letter[bottom_left] == coordinates_to_letter[bottom_right] == "M":
      count += 1

    if coordinates_to_letter[top_left] == coordinates_to_letter[bottom_left] and coordinates_to_letter[top_left] == "S" and coordinates_to_letter[top_right] == coordinates_to_letter[bottom_right] == "M":
      count += 1

  return count