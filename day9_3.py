import re
import math
def read_in_data(input_data):
  with open(input_data, "r") as file:
    return file.readlines()

class Node(object):
  def __init__(self, val, index = None):
    self.prev = None
    self.next = None
    self.index = index
    self.val = val

class DLL(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def new_node(self, val):
    return Node(val)

def disk_map_conversion():
  expanded_disk_map = []
  compacted_version = [int(val) for val in read_in_data('day9.txt')[0]]
  file_id = 0

  for i in range(len(compacted_version)):
    if i % 2 == 0:
      for _ in range(compacted_version[i]):
        expanded_disk_map.append(file_id)
      file_id += 1
    else:
      for _ in range(compacted_version[i]):
        expanded_disk_map.append('.')

  return expanded_disk_map

def create_dll_from_disk_map():
  expanded_disk_map = disk_map_conversion()
  dll = DLL()

  compacted_version = [int(val) for val in read_in_data('day9_full.txt')[0]]

  start_index = 0 
  index = 0
  files = []
  memory = []

  for i in range(len(compacted_version)):
    size = compacted_version[i]
    if i % 2 == 0:
      files.append([size, start_index, index])
      index += 1
    else:
      memory.append([size, start_index])
    start_index += size
  
  files_and_memory = []
  for i in range(len(files) -1, -1, -1):
    added = False

    file_size = files[i][0]
    file_start = files[i][1]
    file_id = files[i][2]

    for j in range(len(memory)):
      memory_size = memory[j][0]
      memory_start = memory[j][1]


      if file_size <= memory_size and file_start > memory_start:
        file_start = memory_start
        files_and_memory.append([file_size, file_start, file_id])

        memory_size -= file_size
        memory_start += file_size

        memory[j][0] = memory_size 
        memory[j][1] = memory_start
        added =True
        break
    if not added:
      files_and_memory.append(files[i])

  total = 0
  for files in files_and_memory:
    file_size = files[0]
    file_start = files[1]
    file_id = files[2]

    for _ in range(file_size):
      total += file_start * file_id
      file_start += 1
  return total
create_dll_from_disk_map()

