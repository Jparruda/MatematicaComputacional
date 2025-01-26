def somatorioMenosMil(x : float, n : int) -> float:
    soma = 0
    k = 1
    for i in range(k, n + 1):
        soma = soma + x
    return 10000 -soma


print(somatorioMenosMil(0.1, 100000))

print(somatorioMenosMil(0.125, 80000))