pairs = [['CM', 900], ['CD', 400], ['XC', 90], ['XL', 40], ['IX', 9], ['IV', 4]]
vals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
tens = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
hundreds = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
thousands = {0: '', 1: 'M', 2: 'MM', 3: 'MMM', 4: 'MMMM'}

def read_roman(num):
	total = 0
	for glyph, val in pairs:
		if glyph in num:
			total += val
			num = num.replace(glyph, '')
	for glyph, val in vals.items():
		total += num.count(glyph) * val
		num = num.replace(glyph, '')
	return total

def write_roman(num):
	string = ''
	one = num % 10
	string = ones[one]
	num -= one
	num /= 10
	ten = num % 10
	string = tens[ten] + string
	num -= ten
	num /= 10
	hundred = num % 10
	string = hundreds[hundred] + string
	num -= hundred
	num /= 10
	thousand = num
	string = thousands[thousand] + string
	return string


if __name__ == '__main__':
	f = open('data/roman.txt', 'r')
	numerals = f.readlines()
	f.close()
	saved = 0
	for num in numerals:
		num = num.strip()
		roman = write_roman(read_roman(num))
		print('{0} -> {1}'.format(num, roman))
		saved += len(num) - len(roman)
	print(saved)