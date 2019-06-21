def is_colorfull(number):
  total = int(str(number)[0])
  res_list = [int(i) for i in str(number)]
  for index in range(1, len(str(number))):
    total *= int(str(number)[index])
    res_list.append(int(str(number)[index-1]) * int(str(number)[index]))
  if number > 99:
    res_list.append(total)
  result = set(res_list)
  return len(res_list) == len(result)

def is_colorfull2(number):
  total = int(str(number)[0])
  res_list = [int(i) for i in str(number)] + [int(str(number)[index-1]) * int(str(number)[index]) for index in range(1, len(str(number)))]
  for index in range(1, len(str(number))):
    total *= int(str(number)[index])
  if number > 99:
    res_list += [total]
  result = set(res_list)
  return len(res_list) == len(result)

number = 1

while int(number) > 0:
  number = int(input('Select a number between 1 and 999 (0 to end) :\n> '))
  if number == 0:
    print('Exiting program.')
  elif is_colorfull(number):
      print(f'Number {number} is colorfull.')
  else:
    print(f'Number {number} is not colorfull.')

for i in range(1,1000):
  if is_colorfull2(i):
    print(f'\tNumber {i} is colorfull')
