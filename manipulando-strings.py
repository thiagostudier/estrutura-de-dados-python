"""# Manipulando Strings"""

a = 'casaco'
print(a)

upper_case = a.upper()
print(upper_case)

lower_case = a.lower()
print(lower_case)

capital_letter = a.capitalize()
print(capital_letter)

middle_word = a[0:3]
print(middle_word)

last_words = a[3:]
print(last_words)

b = a.replace('aco', 'inha')
print(a)
print(b)

c = a.replace('o', 'a')
print(c)

c.find('s')

c.find('a')

c.find('b')

e = ' casado '
print(len(e))

f = e.strip()
print(len(f))

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')