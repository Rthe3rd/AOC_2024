lines = File.readlines('day1_input.txt', chomp: true)

def part_1 lines
  left = []
  right = []
  lines.each do |line|
    left << line.split(" ")[0].to_i
    right << line.split(" ")[1].to_i
  end

  left = left.sort
  right = right.sort

  running_sum = 0
  puts left
  # numbers.zip(letters, colors).each do |num, let, col|

  (0...left).to_a.zip(left, right).each do |num, left_num, right_num|
    puts num
    running_sum += (left_num - right_num).abs
    # puts (left_num)
  end 
  # puts running_sum
end

part_1 lines