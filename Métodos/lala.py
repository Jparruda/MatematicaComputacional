import matplotlib.pyplot as plt

def runge_function(x):
  """Função de Runge."""
  return 1 / (1 + 25 * x**2)

def generate_samples(num_points, interval=(-2, 2)):
  """Gera amostras igualmente espaçadas da função de Runge."""
  x_values = [interval[0] + i * (interval[1] - interval[0]) / (num_points - 1) for i in range(num_points)]
  y_values = [runge_function(x) for x in x_values]
  return x_values, y_values

def polynomial_interpolation(x_sample, y_sample, x_plot):
  """Realiza a interpolação polinomial."""
  def lagrange_polynomial(x, x_sample, y_sample):
    """Calcula o polinômio de Lagrange."""
    result = 0
    for j in range(len(y_sample)):
      term = y_sample[j]
      for m in range(len(x_sample)):
        if j != m:
          term *= (x - x_sample[m]) / (x_sample[j] - x_sample[m])
      result += term
    return result

  y_plot = [lagrange_polynomial(x, x_sample, y_sample) for x in x_plot]
  return y_plot

def spline_interpolation(x_sample, y_sample, x_plot):
  """Realiza a interpolação spline linear simplificada."""
  y_plot = []
  for x in x_plot:
    if x <= x_sample[0]:
      y_plot.append(y_sample[0])
    elif x >= x_sample[-1]:
      y_plot.append(y_sample[-1])
    else:
      for i in range(len(x_sample) - 1):
        if x_sample[i] <= x <= x_sample[i + 1]:
          y = y_sample[i] + (y_sample[i + 1] - y_sample[i]) * (x - x_sample[i]) / (x_sample[i + 1] - x_sample[i])
          y_plot.append(y)
          break
  return y_plot

def plot_results(x_plot, y_runge, x_samples, y_interpolations, y_spline=None):
  """Plota os resultados."""
  plt.figure(figsize=(10, 6))
  plt.plot(x_plot, y_runge, label="Função Original", color="black", linestyle="--")

  colors = ["red", "blue", "green"]
  for i, (x_sample, y_interpolation) in enumerate(zip(x_samples, y_interpolations)):
    plt.plot(x_plot, y_interpolation, label=f"Interpolação ({len(x_sample)} pontos)", color=colors[i])

  if y_spline is not None:
    plt.plot(x_plot, y_spline, label="Spline Cúbica (10 pontos)", color="purple", linestyle=":")

  plt.scatter(x_samples[1], generate_samples(10)[1], color="blue", marker="o", label="Pontos Amostrados")
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.title("Interpolação da Função de Runge e Spline Cúbica")
  plt.legend()
  plt.grid(True)
  plt.xlim(-2.2, 2.2)
  plt.ylim(-1.6, 1.1)
  plt.show()

def main():
  """Função principal para executar o programa."""
  x_plot = [ -2 + i * 4 / 399 for i in range(400)] # Pontos para plotar as curvas
  y_runge = [runge_function(x) for x in x_plot]

  num_points_list = [6, 10, 14]
  x_samples = []
  y_interpolations = []

  for num_points in num_points_list:
    x_sample, y_sample = generate_samples(num_points)
    x_samples.append(x_sample)
    y_interpolations.append(polynomial_interpolation(x_sample, y_sample, x_plot))

  x_sample_spline, y_sample_spline = generate_samples(10)
  y_spline = spline_interpolation(x_sample_spline, y_sample_spline, x_plot)

  plot_results(x_plot, y_runge, x_samples, y_interpolations, y_spline)

if __name__ == "__main__":
  main()