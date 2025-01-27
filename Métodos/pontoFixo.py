def ponto_fixo(f, x0, e1, e2):
  """
  Implementa o método do ponto fixo para encontrar a raiz de uma função.

  Args:
    g: A função iterativa g(x).
    x0: Aproximação inicial.
    e1: Tolerância para o valor absoluto da função.
    e2: Tolerância para a diferença entre duas iterações.

  Returns:
    A raiz aproximada da função.
  """

  k = 1
  x = x0
  while True:
    x1 = f(x)
    print(f"Iteração {k}: x = {x1:.8f}, f(x1) = {f(x1):.8e}, |x1 - x| = {abs(x1 - x):.8e}")
    if abs(f(x1)) < e1 or abs(x1 - x) < e2:
      break
    x = x1
    k += 1

  return x

# Exemplo: encontrando a raiz de f(x) = x^3 - 9x + 3
# Reorganizando para a forma g(x) = x
def f(x):
  return (x**3 + 3) / 9

x0 = 1
e1 = 5e-4
e2 = 5e-4

raiz = ponto_fixo(f, x0, e1, e2)
print(f"A raiz aproximada é: {raiz:.8f}")