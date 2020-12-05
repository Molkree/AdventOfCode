import re
with open('../input/input02.txt') as f:
  validPasswords1 = 0
  validPasswords2 = 0
  for line in f:
    m = re.match(r"(?P<min>.+)-(?P<max>.+) (?P<char>.+): (?P<password>.+)",
                 line)
    min, max, char, password = m.groups()
    min = int(min)
    max = int(max)
    count = 0
    for item in password:
      if item == char:
        count += 1
    if min <= count and count <= max:
      validPasswords1 += 1
    if (password[min - 1] == char or password[max - 1] == char) and \
      password[min - 1] != password[max - 1]:
      validPasswords2 += 1
  print('Part 1:', validPasswords1)
  print('Part 2:', validPasswords2)
