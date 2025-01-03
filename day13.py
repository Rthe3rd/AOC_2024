import re
def read_file(file_name):
  with open(file_name, 'r') as file:
    data = file.readlines()
    file.close()
  return data

def day13():
  prize = []
  # data = [val.strip() for val in read_file('day13_example.txt') if val.split()]
  data = [val.strip() for val in read_file('day13_full.txt') if val.split()]

  stripped_data = [re.findall('\d+', val) for val in data]

  a, b, prize =  stripped_data[::3], stripped_data[1::3], stripped_data[2::3]
  x = [(int(a[val][0]), int(b[val][0])) for val in range(len(a))]
  y = [(int(a[val][1]), int(b[val][1])) for val in range(len(a))]
  prize = [(int(prize[val][0]), int(prize[val][1])) for val in range(len(a))]
  big_prizes = [(int(prize[val][0]) + 10000000000000, int(prize[val][1]) + 10000000000000) for val in range(len(a))]

  total_tokens = 0
  big_total_tokens = 0

  for i in range(len(prize)):
    xa_movement, xb_movement = x[i][0], x[i][1]
    ya_movement, yb_movement = y[i][0], y[i][1]
    prize_x, prize_y = prize[i][0], prize[i][1]
    B = -1 * (prize_y * xa_movement - prize_x * ya_movement ) / (xb_movement * ya_movement - yb_movement * xa_movement)
    A = (prize_x  - B * xb_movement) / xa_movement
    if A.is_integer() and B.is_integer():
      total_tokens += (A * 3 + B)

  for i in range(len(prize)):
    xa_movement, xb_movement = x[i][0], x[i][1]
    ya_movement, yb_movement = y[i][0], y[i][1]
    big_prize_x, big_prize_y = big_prizes[i][0], big_prizes[i][1]
    B = -1 * (big_prize_y * xa_movement - big_prize_x * ya_movement ) / (xb_movement * ya_movement - yb_movement * xa_movement)
    A = (big_prize_x  - B * xb_movement) / xa_movement
    if A.is_integer() and B.is_integer():
      big_total_tokens += (A * 3 + B)

  return total_tokens, big_total_tokens


print(day13())