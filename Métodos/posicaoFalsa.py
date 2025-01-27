def posicao_falsa(f, a, b, e1, e2):
  """
  Implementa o método da posição falsa para encontrar a raiz de uma função.

  Args:
    f: A função para a qual se deseja encontrar a raiz.
    a: Extremo esquerdo do intervalo.
    b: Extremo direito do intervalo.
    e1: Tolerância para o tamanho do intervalo.
    e2: Tolerância para o valor absoluto da função.

  Returns:
    A raiz aproximada da função no intervalo dado.
  """

  k = 1
  while True:
    x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    print(f"Iteração {k}: x = {x:.8f}, f(x) = {f(x):.8e}, b - a = {b - a:.8f}")
    if abs(f(x)) < e2 or abs(b - a) < e1:
      break
    if f(a) * f(x) < 0:
      b = x
    else:
      a = x
    k += 1

  return x

# Exemplo conforme dado
def f(x):
  return x**3 - 9*x + 3

a = 0
b = 1
e1 = 5e-4
e2 = 5e-4

raiz = posicao_falsa(f, a, b, e1, e2)
print(f"A raiz aproximada é: {raiz:.8f}")