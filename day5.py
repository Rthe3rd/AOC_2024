def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

def part1():
  input_rules = [val.strip().split("|") for val in read_in_data('day5_rules.txt')]
  input_pages = [val.strip().split(",") for val in read_in_data('day5_pages.txt')]
  unique_vals = set() 

  [[unique_vals.add(page_number) for page_number in val] for val in input_rules]
  after_rules = dict()
  before_rules = dict()
  for rule in input_rules:
    before = rule[0]
    after = rule[1]

    if not before in before_rules:
      before_rules[before] = set([after])
    if before in before_rules:
      before_rules[before].add(after)

    if not after in after_rules:
      after_rules[after] = set([before])
    if after in after_rules:
      after_rules[after].add(before)

  good_pages = []
  bad_pages = []
  # while you loop through the pages, make sure that none of the numbers seen should be AFTER the current letter
  # AND make sure that you
  for pages in input_pages:
    pages_seen = set()
    good_order = True
    for i in range(len(pages)):
      current_page = pages[i]
      if current_page in before_rules:
        pages_current_page_should_be_before = before_rules[current_page]
        for page_seen in pages_seen:
          if page_seen in pages_current_page_should_be_before:
            bad_pages.append(pages)
            good_order = False
            break
        if good_order == False:
          break
      pages_seen.add(current_page)
      if i == len(pages) - 1:
        good_pages.append(pages)

  good_sum = 0
  for good_page in good_pages:
    good_sum += int(good_page[len(good_page) // 2])

  sorted_arrays = []
  for bad_page in bad_pages:
    sorted_array = []

    for i in range(len(bad_page)):
      
      current_page = bad_page[i]
      if i == 0:
        sorted_array.append(current_page)
        continue
      # are there "rules" for the current page which dictate which numbers need to be AFTER it?
      if current_page in after_rules: 
        pages_after_current_page = after_rules[current_page]

        # Since the array is already sorted, you just need to find the first value you come across that needs to be after the current page
        j = 0
        end_of_sorted_array = len(sorted_array)
        while j < end_of_sorted_array:
          page_to_check = sorted_array[j]
          if page_to_check in pages_after_current_page:
            sorted_array = sorted_array[0:j] + [current_page] + sorted_array[j:]
            j = len(sorted_array)
          elif j == end_of_sorted_array - 1:
            sorted_array.append(current_page)
          j += 1
      # if there are no rules about what pages need to be after the current page, add it to the end
      else:
        sorted_array.append(current_page)
    sorted_arrays.append(sorted_array.copy()[::-1])
    print(sorted_arrays)

    bad_sum = 0
    for bad_page in sorted_arrays:
      bad_sum += int(bad_page[len(bad_page) // 2]) 

  return good_sum, bad_sum

print(part1())

