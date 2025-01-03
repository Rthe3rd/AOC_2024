def read_in_data(file):
  with open(file, 'r') as file:
    return file.readlines()
  file.close()
  

class GardenBuilder():

  def __init__(self):
    self.input_data = [val.strip() for val in read_in_data('day12_example.txt')]
    self.garden_type_to_coords = dict()
    self.coords_to_garden_type = dict()
    self.garden_checker = dict()
    self.gardens = dict()

  def create_maps(self):
    for row in range(len(self.input_data)):
      for column in range(len(self.input_data[row])):
        self.coords_to_garden_type[(row, column)] = self.input_data[row][column]
        if self.input_data[row][column] not in self.garden_type_to_coords:
          self.garden_type_to_coords[self.input_data[row][column]] = [(row, column)]
        else:
          self.garden_type_to_coords[self.input_data[row][ column]].append((row, column))

  def create_gardens(self):
    garden_number = 0
    gardens = {garden_type: {} for garden_type in self.garden_type_to_coords.keys()}

    for garden_type, all_plant_coords in self.garden_type_to_coords.items():
      all_plant_coords_hash = set(all_plant_coords)

      for plant_coords in all_plant_coords_hash:
        row, col = plant_coords[0], plant_coords[1]
        adjacent_plants = set()

        if (row - 1, col) in self.coords_to_garden_type and garden_type == self.coords_to_garden_type[(row - 1, col)]:
          adjacent_plants.add((row - 1, col))
        if (row + 1, col) in self.coords_to_garden_type and garden_type == self.coords_to_garden_type[(row + 1, col)]:
          adjacent_plants.add((row + 1, col))
        if (row, col - 1) in self.coords_to_garden_type and garden_type == self.coords_to_garden_type[(row, col - 1)]:
          adjacent_plants.add((row, col - 1))
        if (row, col + 1) in self.coords_to_garden_type and garden_type == self.coords_to_garden_type[(row, col + 1)]:
          adjacent_plants.add((row, col + 1))

        # for adjacent_plant in adjacent_plants:



    return gardens


      # for adjacent_plant in adjacent_plants:


    # for garden_type, all_plant_coordinates in self.garden_type_to_coords.items():
    #   for plant_coordinates in all_plant_coordinates:
    #     plant_row, plant_column = plant_coordinates[0], plant_coordinates[1]

    #     if garden_type not in self.garden_map:
    #       self.garden_map[garden_type] = {garden_number: {(plant_row, plant_column)}}
    #       self.gardens[garden_number] = [(plant_column, plant_column)]
    #       garden_number += 1

        # else:
        #   for garden_number, mapped_plant_coordinates in self.garden_map[garden_type].items():
            # print(f'Garden Number: {garden_number}, Plant Coordinates: {mapped_plant_coordinates}')

        # determine which garden this plant belongs to




def day12():
  gardenbuilder = GardenBuilder()
  gardenbuilder.create_maps()
  gardenbuilder.create_gardens()

  return 



print(day12())