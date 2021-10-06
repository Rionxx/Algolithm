
#function linear_search
def linear_search(key, input):
  for i, num in enumerate(input):
    if key == num:
      print("{} is found input[{}]!").format(key, i)
      break
    else:
      print("{} is not found..").format(key)


input = [3, 5, 9, 12, 15, 21, 29, 37, 42, 53, 63, 77, 82, 89, 92]

linear_search(62, input)
linear_search(9, input)
linear_search(81, input)
linear_search(42, input)