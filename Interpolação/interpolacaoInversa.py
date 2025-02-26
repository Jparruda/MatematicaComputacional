import matplotlib.pyplot as plt

def interpolacao_inversa(x_vals, y_vals, y_target):
    """
    Realiza interpolação inversa para encontrar x correspondente a um dado y_target.
    x_vals: lista de valores de x
    y_vals: lista de valores de y
    y_target: valor alvo de y para encontrar x correspondente
    Retorna: x estimado
    """
    # Ordena os pontos pelo valor de y (importante para interpolação inversa)
    pontos = sorted(zip(y_vals, x_vals))
    y_vals_ord, x_vals_ord = zip(*pontos)

    # Verifica se o y_target está dentro do intervalo
    if y_target < min(y_vals_ord) or y_target > max(y_vals_ord):
        raise ValueError("y_target está fora do intervalo de interpolação!")

    # Encontrar os pontos mais próximos para interpolação
    for i in range(len(y_vals_ord) - 1):
        if y_vals_ord[i] <= y_target <= y_vals_ord[i + 1]:
            # Interpolação linear inversa
            x_inverso = x_vals_ord[i] + (y_target - y_vals_ord[i]) * (x_vals_ord[i + 1] - x_vals_ord[i]) / (y_vals_ord[i + 1] - y_vals_ord[i])
            return x_inverso, (x_vals_ord[i], y_vals_ord[i]), (x_vals_ord[i + 1], y_vals_ord[i + 1])

    return None, None, None  # Caso inesperado (não deveria ocorrer devido à verificação de intervalo)

def plotar_interpolacao_inversa(x_vals, y_vals, x_est, y_target, p1, p2):
    """
    Plota os pontos originais e o ponto estimado pela interpolação inversa.
    """
    plt.scatter(x_vals, y_vals, color="blue", label="Pontos Originais")  # Pontos originais
    plt.scatter(x_est, y_target, color="red", label=f"Interpolação (x={x_est:.2f})")  # Ponto interpolado
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color="green", linestyle="dashed", label="Interpolação Linear")  # Reta de interpolação

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Interpolação Inversa")
    plt.legend()
    plt.grid(True)
    plt.show()

# Teste
if __name__ == "__main__":
    x_test = [1, 2, 3, 4, 5]
    y_test = [2, 4, 8, 16, 32]  # Crescendo exponencialmente
    y_alvo = 10

    x_est, p1, p2 = interpolacao_inversa(x_test, y_test, y_alvo)
    
    if x_est is not None:
        print(f"O valor estimado de x para y = {y_alvo} é x ≈ {x_est:.4f}")
        plotar_interpolacao_inversa(x_test, y_test, x_est, y_alvo, p1, p2)
