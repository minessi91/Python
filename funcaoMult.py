

valor = input("Digite um valor ") #a
# lista = [a * 1 for a in range(11)]  # b
lista = [1,2,3,4,5,6,7,8,9,10]  # b



def multiplicando(a, b):
     counter = 1
     for var1 in [x * int(a) for x in b]:
      print('{} * {} = {}'.format(a, counter, var1))
      counter += 1

multiplicando(valor, lista)

