def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()
  

def part_one():
  reports = [[int(inner) for inner in val.strip().split(" ")] for val in read_in_data("day2_input.txt")]
  good_reports = 0
  for report in reports:
    increasing = False
    if report[0] < report[1]:
      increasing = True
    for i in range(1, len(report)):
      if increasing and not report[i] - report[i-1] in (1,2,3):
        break
      elif not increasing and not report[i] - report[i-1] in (-1, -2,-3):
        break
      elif i == len(report) - 1:
        good_reports += 1
  return good_reports, reports

def part_two():
  reports = [[int(inner) for inner in val.strip().split(" ")] for val in read_in_data("day2_input.txt")]
  good_reports = 0
  for report in reports:
    valid = False
    if check_increasing(report)[0] or check_decreasing(report)[0]:
      valid = True
    elif not valid:
      if not check_increasing(report)[0]:
        problem_index_increasing = check_increasing(report)[1]
      if not check_decreasing(report)[0]:
        problem_index_decreasing = check_decreasing(report)[1]
      if check_increasing(report[:problem_index_increasing] + report[problem_index_increasing + 1:])[0] or check_decreasing(report[:problem_index_decreasing] + report[problem_index_decreasing + 1:])[0]:
        valid = True
      if check_increasing(report[:problem_index_increasing-1] + report[problem_index_increasing:])[0] or check_decreasing(report[:problem_index_decreasing-1] + report[problem_index_decreasing:])[0]:
        valid = True
    if valid:
      good_reports += 1
  return good_reports

def check_increasing(report):
  for index in range(1, len(report)):
    difference = report[index] - report[index - 1]
    if not difference in (1, 2, 3):
      return [False, index]
  return [True, index]

def check_decreasing(report):
  for index in range(1, len(report)):
    difference = report[index] - report[index - 1]
    if not difference in (-1, -2, -3):
      return [False, index]
  return [True, index]


from collections import Counter
def part_3():
  reports = [[int(inner) for inner in val.strip().split(" ")] for val in read_in_data("test.txt")]
  
  report_hash_holder = []
  for report in reports:
    # validity_hash = {'increasing': 0, 'decreasing': 0, 'counter': Counter(report)}
    validity_hash = {'increasing': [], 'decreasing': [], 'counter': Counter(report)}

    for index in range(1, len(report)):
      if report[index] - report[index - 1] in (1,2,3):
        # validity_hash['increasing'] += 1
        validity_hash['increasing'].append(index)
      elif report[index] - report[index - 1] in (-1,-2,-3):
        validity_hash['decreasing'].append(index)

    report_hash_holder.append(validity_hash)
    valid_hashes = 0
    for report_hash in report_hash_holder:

      if report_hash['counter'].most_common(1)[0][1] > 2:
        continue

      if len(report_hash['increasing']) >= 2 and len(report_hash['decreasing']) >= 2:
        continue
      
      valid_hashes += 1

  return valid_hashes


print(part_two())
# print(part_3())
# 604 too low
# 605 too low
# 608 is not right
# 609 is not right
# 610 is not right
# 611 is not right
# 615 is not right
# 633 too high