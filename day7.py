def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

# def test():
#   input = [[inner_val.strip().split(" ") for inner_val in val.strip().split(":")] for val in read_in_data("day7.txt")]
#   a = [[inner_val for inner_val in val if len(inner_val) == 1][0][0] for val in input]
#   s = set([[inner_val for inner_val in val if len(inner_val) == 1][0][0] for val in input])
#   return len(a) == len(s)


def day7_p1():
  running_sums  = set()
  input = [[inner_val.strip().split(" ") for inner_val in val.strip().split(":")] for val in read_in_data("day7.txt")]

  all_targets = [[inner_val for inner_val in val if len(inner_val) == 1][0][0] for val in input]
  all_operands = [[[int(val) for val in inner_val] for inner_val in val if len(inner_val) > 1][0] for val in input]

  def dfs(targets, operands, current_sum, start):
    if start >= len(operands):
      if current_sum == int(targets):
        running_sums.add(current_sum)
        return
      return

    dfs(targets, operands, current_sum + operands[start], start + 1)
    dfs(targets, operands, current_sum * operands[start], start + 1)

    return 
  
  for i in range(len(all_targets)):
    targets = all_targets[i]
    operands = all_operands[i]
    dfs(targets, operands, operands[0], 1)

  return sum(running_sums)

def day7_p2():
  running_sums  = set()
  input = [[inner_val.strip().split(" ") for inner_val in val.strip().split(":")] for val in read_in_data("day7.txt")]

  all_targets = [[inner_val for inner_val in val if len(inner_val) == 1][0][0] for val in input]
  all_operands = [[[int(val) for val in inner_val] for inner_val in val if len(inner_val) > 1][0] for val in input]

  def dfs(targets, operands, current_sum, start):
    if start >= len(operands):
      if current_sum == int(targets):
        running_sums.add(current_sum)
        return
      return

    dfs(targets, operands, current_sum + operands[start], start + 1)
    dfs(targets, operands, int(str(current_sum) + str(operands[start])), start + 1)
    dfs(targets, operands, current_sum * operands[start], start + 1 )

    return 
  
  for i in range(len(all_targets)):
    targets = all_targets[i]
    operands = all_operands[i]
    dfs(targets, operands, operands[0], 1)

  return sum(running_sums)


# 975671981569
# 975726879950 too high