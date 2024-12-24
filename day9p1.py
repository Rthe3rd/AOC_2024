import math
def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

class DLL(object):
  def __init__(self, val):
    new_node = self.new_node(val)
    self.head = new_node
    self.tail = new_node
    self.total_length = 0
    self.files_checked = set()
    self.dummy_tail = None
    self.last_checked = None
    self.last_checked_distance_from_end = 0

  def new_node(self, val):
    return Node(val)
  
  def print_list(self):
    current = self.head
    index = 0
    while current:
      print(f'Index: {index} Value: {current.val}')
      index += 1 
      current = current.next

  def calculate_checksum(self):

    current = self.head
    index = 0
    check_sum = 0
    while current:
      if current.val != '.': 
        check_sum += index * int(current.val)
      index += 1
      current = current.next
    return check_sum

  def expanded_disk_map_to_dll(self, expanded_disk_map):
    current = self.head
    tail = None
    for val in expanded_disk_map:
      new_node = Node(val)
      current.next = new_node
      new_node.prev = current
      tail = current
      current = current.next
    
    self.tail = tail.next
    self.head = self.head.next

  def move_one_file_at_a_time(self):
    dummy_tail = Node(0)
    dummy_tail.prev = self.tail
    dummy_head = Node(0)
    dummy_head.next = self.head

    forward_current = dummy_head.next
    back_current = dummy_tail.prev

    unsorted = True
    count = 0
    while forward_current and unsorted:
      count += 1
      # moving forward, if you've found a val to swap, ".",
      if forward_current.val == ".":

        # Nodes before/after forward_current
        f_c_prev = forward_current.prev
        f_c_next = forward_current.next

        back_current = dummy_tail.prev
        back_current.next = dummy_tail

        while back_current and back_current.val == '.':
          back_current = back_current.prev
    
          if forward_current == back_current:
            unsorted = False
            break

        # point the nodes pointing at f_c to b_c
        f_c_prev.next = back_current
        f_c_next.prev = back_current

        # point back_current's nieghors to each other to "close" the hole created
        back_current.prev.next = back_current.next
        back_current.next.prev = back_current.prev

        # point back_current new neighbors
        back_current.next = f_c_next 
        back_current.prev = f_c_prev 

        # point forward_current to the back
        forward_current.prev = dummy_tail.prev
        forward_current.next = dummy_tail

        # point last node at forward_current
        dummy_tail.prev.next = forward_current

        forward_current = dummy_head.next

      else:
        forward_current = forward_current.next

    # clean up dummy pointers (not needed)
    dummy_tail.prev.next = None
    dummy_tail.prev = None
    dummy_head.next = None

class Node(object):
  def __init__(self, val):
    self.prev = None
    self.next = None
    self.val = val


def day9():

  input = [val.strip() for val in read_in_data("day9_full.txt")][0]
  
  expanded_disk_map = []
  free_space = False
  file_index = 0
  for index, value in enumerate(input):
    for j in range(int(value)):
      if free_space:
        expanded_disk_map.append('.')
      else:
        expanded_disk_map.append(file_index)
    if free_space:
      file_index += 1
    free_space = not free_space

  dll_2 = DLL(float("inf"))
  dll_2.expanded_disk_map_to_dll(expanded_disk_map)

  total_length = len(expanded_disk_map)
  dll_2.total_length = total_length


  dummy_head = Node("dummy head")
  dummy_head.next = dll_2.head

  dll_2.dummy_tail = Node("dummy tail")
  dll_2.dummy_tail.prev = dll_2.tail
  dll_2.tail.next = dll_2.dummy_tail
  dll_2.last_checked = dll_2.tail


  dll_2.tail.next = None
  dll_2.move_one_file_at_a_time()

  return dll_2.calculate_checksum()