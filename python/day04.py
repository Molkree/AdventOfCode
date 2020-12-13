print('Day 04')
def isValidPassport(fields):
  keyValuePairs = fields.replace(' ', '\n').split()
  keyValuePairs = [keyValuePair.split(':') for keyValuePair in keyValuePairs]
  keyValuePairs = {key: value for (key, value) in keyValuePairs}

  return 'byr' in keyValuePairs and \
    keyValuePairs['byr'].isdigit() and \
    1920 <= int(keyValuePairs['byr']) <= 2002 and \
    \
    'iyr' in keyValuePairs and \
    keyValuePairs['iyr'].isdigit() and \
    2010 <= int(keyValuePairs['iyr']) <= 2020 and \
    \
    'eyr' in keyValuePairs and \
    keyValuePairs['eyr'].isdigit() and \
    2020 <= int(keyValuePairs['eyr']) <= 2030 and \
    \
    'hgt' in keyValuePairs and \
    (keyValuePairs['hgt'].endswith('cm') and \
     150 <= int(keyValuePairs['hgt'][:-2]) <= 193 or \
     keyValuePairs['hgt'].endswith('in') and \
     59 <= int(keyValuePairs['hgt'][:-2]) <= 76) and \
    \
    'hcl' in keyValuePairs and \
    keyValuePairs['hcl'].startswith('#') and \
    len(keyValuePairs['hcl']) == 7 and \
    all('0' <= c <= '9' or 'a' <= c <= 'z' for c in keyValuePairs['hcl'][1:]) and \
    \
    'ecl' in keyValuePairs and \
    keyValuePairs['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
    \
    'pid' in keyValuePairs and \
    len(keyValuePairs['pid']) == 9 and \
    all('0' <= c <= '9' for c in keyValuePairs['pid'])

with open('../input/input04.txt') as f:
  passports = f.read().split('\n\n')
  requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  validPassports1 = sum(
      all(field in passport for field in requiredFields) for passport in passports)
  validPassports2 = sum(isValidPassport(passport) for passport in passports)

print(f'Part 1: {validPassports1}')
print(f'Part 2: {validPassports2}')
