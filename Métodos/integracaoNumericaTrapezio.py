def trapezoidal_rule(func, a, b, n):
    """
    Calcula a integral aproximada de uma função usando a regra dos trapézios.

    Args:
        func: A função a ser integrada.
        a: Limite inferior de integração.
        b: Limite superior de integração.
        n: Número de subintervalos (trapézios).

    Returns:
        O valor aproximado da integral.
    """
    h = (b - a) / n  # Tamanho de cada subintervalo
    
    # Calcula os valores da função nos pontos extremos
    f_a = func(a)
    f_b = func(b)
    
    # Calcula a soma dos valores da função nos pontos intermediários
    sum_f = 0
    for i in range(1, n):
        sum_f += func(a + i * h)
    
    # Aplica a fórmula da regra dos trapézios
    integral = (h / 2) * (f_a + 2 * sum_f + f_b)
    
    return integral

# Exemplo de uso
def f(x):
    return x**2

a = 0  # Limite inferior
b = 1  # Limite superior
n = 100  # Número de trapézios

resultado = trapezoidal_rule(f, a, b, n)
print(f"A integral aproximada é: {resultado}")