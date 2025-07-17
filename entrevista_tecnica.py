lista = [2, 3, 4, 5, 9, 1, 6]

print("--" * 20)
print(f"Cantidad de productos en lista: {0 if sum(lista) == 0 else len(lista)}")
print(f"Peso Total de La lista: {sum(lista)} Kg")
print(f"La cantidad de Viajes a Realizar es:"
      f" {round(sum(lista) // 10) if sum(lista) == sum(lista) // 10 * 10 else round((sum(lista) // 10) + 1)}")
print("--" * 20)

