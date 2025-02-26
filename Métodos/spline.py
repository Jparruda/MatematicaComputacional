import matplotlib.pyplot as plt

def spline_interpolation(x_sample, y_sample, x_plot):
    """
    Realiza a interpolação spline linear simplificada.

    Args:
        x_sample: Lista com os valores de x dos pontos de amostra.
        y_sample: Lista com os valores de y dos pontos de amostra.
        x_plot: Lista com os valores de x para os quais a interpolação será calculada.

    Returns:
        Lista com os valores de y interpolados.
    """
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

def plot_graph(x_values, y_values, title="Gráfico", xlabel="Eixo X", ylabel="Eixo Y", color="blue", marker="o", linestyle="-"):
    """
    Plota um gráfico simples.

    Args:
        x_values: Lista com os valores de x.
        y_values: Lista com os valores de y.
        title: Título do gráfico (opcional).
        xlabel: Rótulo do eixo x (opcional).
        ylabel: Rótulo do eixo y (opcional).
        color: Cor da linha (opcional).
        marker: Marcador dos pontos (opcional).
        linestyle: Estilo da linha (opcional).
    """
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, color=color, marker=marker, linestyle=linestyle)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Exemplo de uso
x_sample = [1, 2, 3, 4, 5]
y_sample = [2, 4, 1, 3, 5]
x_plot = [1.5, 2.5, 3.5, 4.5]

y_interpolated = spline_interpolation(x_sample, y_sample, x_plot)

# Combina os pontos originais e interpolados para plotagem
x_combined = sorted(x_sample + x_plot)
y_combined = []
for x in x_combined:
    if x in x_sample:
        y_combined.append(y_sample[x_sample.index(x)])
    else:
        y_combined.append(y_interpolated[x_plot.index(x)])

plot_graph(x_combined, y_combined, title="Interpolação Spline Linear", xlabel="x", ylabel="y")