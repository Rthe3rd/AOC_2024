def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()
  

from collections import Counter

def day11():

  all_stones = []
  initial_stones = [int(val) for val in read_in_data('day11_full.txt')[0].split() if val.strip()]

  # DFS approach works for Part I but blows up for Part II
  def dfsp1(number_of_blinks, current_stone):
    if number_of_blinks == 25:
      all_stones.append(current_stone)
      return 

    else:

      # condition 1: 0 -> 1
      if current_stone == 0:
        new_stone = dfsp1(number_of_blinks + 1, 1)

      # condition 2: len(current_stones) % 2 == 0 -> current_stone[:len(current_stones)/2], current_stone[len(current_stones)/2:]
      elif len(str(current_stone)) % 2 == 0:

        half_way = int(len(str(current_stone)) / 2)
        left_stone, right_stone = int(str(current_stone)[:half_way]), int(str(current_stone)[half_way:])

        new_stone = dfsp1(number_of_blinks + 1, left_stone)
        new_stone = dfsp1(number_of_blinks + 1, right_stone)

      # condition 3: else 2024 * current_stone
      else:
        current_stone = int(current_stone) * 2024
        new_stone = dfsp1(number_of_blinks + 1, current_stone)

    return new_stone

  # Part II
  stones = Counter([int(val) for val in initial_stones])

  for _ in range(75):

    stones_to_modify = stones.copy()
    for key, value in stones_to_modify.items():

      stone_to_modify = int(key)

      if value:

        # condition 1: 0 -> 1
        if stone_to_modify == 0:
          new_stone = [1]

        # condition 2: len(stone_to_modifys) % 2 == 0 -> stone_to_modify[:len(stone_to_modifys)/2], stone_to_modify[len(stone_to_modifys)/2:]
        elif len(str(stone_to_modify)) % 2 == 0:

          half_way = int(len(str(stone_to_modify)) / 2)
          new_stone = [int(str(stone_to_modify)[:half_way]), int(str(stone_to_modify)[half_way:])]

        # condition 3: else 2024 * stone_to_modify
        else:
          new_stone = [int(stone_to_modify) * 2024]

        for stone in new_stone:
          stones[stone] += value

        stones[stone_to_modify] -= value

  total_stones = 0
  for key, value in stones.items():
    total_stones += value

  for val in initial_stones:
    dfsp1(0, val)

  return len(all_stones), total_stones

print(day11())
