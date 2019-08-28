# Numeros pares até 30
print ([num for num in range(1,31) if num % 2 == 0])

# Números ímpares até 10
print ([num**2 for num in range(10) if num % 2 != 0])

# Idade de cada pessoa de acordo com os anos de nascimento
list_years = [1991, 1994, 1995, 1999, 2000, 2004, 2010]
print ([2019-idade for idade in list_years])

# Chaves: números pares até 10; Valores: Cubo das chaves 
print({num: num**3 for num in range(1,11) if num % 2 == 0})

# Chaves: elementos da lista; Valores: qtde. de vezes que o elemente apareceu na lista
test_list = [3, 3, 2, 1, 1, 3, 2, 2, 1, 3, 0]
test_list = sorted(test_list)
print({elem: sum([i == elem for i in test_list]) for elem in test_list})

# Uma tupla (x, y), onde x representa a n-ésima letra de uma string e y = (n+1)-ésima letra
string = "python"
print([(string[i],string[i+1]) for i in range(len(string)-1)])

# Funcao que retorna divisivel por 6
def by_six(x):
  if(x % 6 == 0): return True
  return False

print(by_six(6))
print(by_six(12))

# Soma duas listas
def add_lists(list_1, list_2):
  return [(list_1[elem] + list_2[elem]) for elem in range(len(list_1))]

# não altere o código abaixo
list_1 = [1, 2, 3, 4, 5]
list_2 = [7, 9, 6, 4, 0]

add_lists(list_1, list_2)
