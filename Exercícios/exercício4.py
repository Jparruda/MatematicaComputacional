import math

def trapezoidal_rule(func, a, b, n):
  """Calcula a integral usando a regra dos trapézios."""
  h = (b - a) / n
  result = 0.5 * (func(a) + func(b))
  for i in range(1, n):
    result += func(a + i * h)
  result *= h
  return result

def simpson_rule(func, a, b, n):
  """Calcula a integral usando a regra de Simpson."""
  if n % 2 != 0:
    raise ValueError("n deve ser par para a regra de Simpson")
  h = (b - a) / n
  result = func(a) + func(b)
  for i in range(1, n, 2):
    result += 4 * func(a + i * h)
  for i in range(2, n - 1, 2):
    result += 2 * func(a + i * h)
  result *= h / 3
  return result

def func_a(x):
  return math.exp(x)

def func_b(x):
  return math.sqrt(x)

def func_c(x):
  return 24 / math.sqrt(x)

# Caso a
print("Caso a:")
print("Trapézios (4 divisões):", trapezoidal_rule(func_a, 1, 2, 4))
print("Trapézios (6 divisões):", trapezoidal_rule(func_a, 1, 2, 6))
print("Simpson (4 divisões):", simpson_rule(func_a, 1, 2, 4))
print("Simpson (6 divisões):", simpson_rule(func_a, 1, 2, 6))

# Caso b
print("\nCaso b:")
print("Trapézios (4 divisões):", trapezoidal_rule(func_b, 1, 4, 4))
print("Trapézios (6 divisões):", trapezoidal_rule(func_b, 1, 4, 6))
print("Simpson (4 divisões):", simpson_rule(func_b, 1, 4, 4))
print("Simpson (6 divisões):", simpson_rule(func_b, 1, 4, 6))

# Caso c
print("\nCaso c:")
print("Trapézios (4 divisões):", trapezoidal_rule(func_c, 2, 14, 4))
print("Trapézios (6 divisões):", trapezoidal_rule(func_c, 2, 14, 6))
print("Simpson (4 divisões):", simpson_rule(func_c, 2, 14, 4))
print("Simpson (6 divisões):", simpson_rule(func_c, 2, 14, 6))