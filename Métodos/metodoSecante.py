def secante(f, x0, x1, e1, e2):
  """
  Implementa o método da secante para encontrar a raiz de uma função.

  Args:
    f: A função para a qual se deseja encontrar a raiz.
    x0, x1: Aproximações iniciais.
    e1: Tolerância para o valor absoluto da função.
    e2: Tolerância para a diferença entre duas iterações.

  Returns:
    A raiz aproximada da função.
  """

  k = 1
  while True:
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    print(f"Iteração {k}: x = {x2:.8f}, f(x) = {f(x2):.8e}, |x2 - x1| = {abs(x2 - x1):.8e}")
    if abs(f(x2)) < e1 or abs(x2 - x1) < e2:
      break
    x0 = x1
    x1 = x2
    k += 1

  return x2

# Exemplo: encontrando a raiz de f(x) = x^3 - 9x + 3
def f(x):
  return x**3 - 9*x + 3

x0 = 0
x1 = 1
e1 = 5e-4
e2 = 5e-4

raiz = secante(f, x0, x1, e1, e2)
print(f"A raiz aproximada é: {raiz:.8f}")