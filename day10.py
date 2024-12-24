def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

def day10():
  input = [[int(num.strip()) for num in val if num.strip()] for val in read_in_data('day10_full.txt')]


  cordinates_to_heights = {}
  heights_to_coordinates = {}

  for row in range(len(input)):
    for col in range(len(input[row])):
      cordinates_to_heights[(row, col)] = input[row][col]
      if input[row][col] not in heights_to_coordinates:
        heights_to_coordinates[input[row][col]] = [[row, col]]
      else:
        heights_to_coordinates[input[row][col]].append([row, col])

  trail_heads = set()
  paths_taken = [0]

  def dfs(row, col, current_path):
    print(f'current height: {input[row][col]} and current coord ({row},{col},{start})')
    if len(current_path) == 10:
      trail_heads.add((row, col, start))
      paths_taken[0] += 1
      return

    # right
    if (row, col + 1) in cordinates_to_heights and current_path[-1] + 1 == input[row][col + 1]:
      dfs(row, col + 1, current_path + [input[row][col + 1]])

    # left
    if (row, col - 1) in cordinates_to_heights and current_path[-1] + 1 == input[row][col - 1]:
      dfs(row, col - 1, current_path + [input[row][col - 1]])

    # down
    if (row + 1, col) in cordinates_to_heights and current_path[-1] + 1 == input[row + 1][col]:
      dfs(row + 1, col, current_path + [input[row + 1][col]])

    # up
    if (row - 1, col) in cordinates_to_heights and current_path[-1] + 1 == input[row - 1][col]:
      dfs(row - 1, col, current_path + [input[row - 1][col]])

    return

  start = 0
  for zero_coord in heights_to_coordinates[0]:
    row, col = zero_coord[0], zero_coord[1]
    dfs(row, col, [0])
    start += 1

  return len(trail_heads), paths_taken

print(day10())