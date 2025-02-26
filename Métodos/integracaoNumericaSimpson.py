def simpson_rule(func, a, b, n):
    """
    Calcula a integral aproximada de uma função usando a regra 1/3 de Simpson.

    Args:
        func: A função a ser integrada.
        a: Limite inferior de integração.
        b: Limite superior de integração.
        n: Número de subintervalos (deve ser par).

    Returns:
        O valor aproximado da integral.
    """
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser par para a regra de Simpson.")

    h = (b - a) / n  # Tamanho de cada subintervalo
    
    # Calcula os valores da função nos pontos extremos
    f_a = func(a)
    f_b = func(b)
    
    # Calcula a soma dos valores da função nos pontos ímpares
    sum_odd = 0
    for i in range(1, n, 2):
        sum_odd += func(a + i * h)
    
    # Calcula a soma dos valores da função nos pontos pares
    sum_even = 0
    for i in range(2, n - 1, 2):
        sum_even += func(a + i * h)
    
    # Aplica a fórmula da regra 1/3 de Simpson
    integral = (h / 3) * (f_a + 4 * sum_odd + 2 * sum_even + f_b)
    
    return integral

# Exemplo de uso
def f(x):
    return x**4

a = 0  # Limite inferior
b = 2  # Limite superior
n = 100  # Número de subintervalos (deve ser par)

resultado = simpson_rule(f, a, b, n)
print(f"A integral aproximada é: {resultado}")