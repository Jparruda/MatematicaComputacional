def newton_raphson(f, df, x0, e1, e2):
  """
  Implementa o método de Newton-Raphson para encontrar a raiz de uma função.

  Args:
    f: A função para a qual se deseja encontrar a raiz.
    df: A derivada da função.
    x0: Aproximação inicial.
    e1: Tolerância para o valor absoluto da função.
    e2: Tolerância para a diferença entre duas iterações.

  Returns:
    A raiz aproximada da função.
  """

  k = 1
  while True:
    x1 = x0 - f(x0) / df(x0)
    print(f"Iteração {k}: x = {x1:.8f}, f(x) = {f(x1):.8e}, |x1 - x0| = {abs(x1 - x0):.8e}")
    if abs(f(x1)) < e1 or abs(x1 - x0) < e2:
      break
    x0 = x1
    k += 1

  return x1

# Exemplo: encontrando a raiz de f(x) = x^3 - 9x + 3
def f(x):
  return x**3 - 9*x + 3
def df(x):
  return 3*x**2 - 9

x0 = 0.5
e1 = 1e-4
e2 = 1e-4

raiz = newton_raphson(f, df, x0, e1, e2)
print(f"A raiz aproximada é: {raiz:.8f}")