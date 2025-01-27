import matplotlib.pyplot as plt

# Função que define f(x)
def funcao(x):
    return (x**3)-(9*x)+3

# Função para criar a tabela de valores e sinais
def criar_tabela(valores_x):
    print("\n*** Tabela de Valores e Sinais de f(x) ***")
    print(f"{'x':>10} | {'f(x)':>15} | {'Sinal':>10}")
    print("-" * 40)

    for x in valores_x:
        fx = funcao(x)
        sinal = "Positivo" if fx > 0 else "Negativo"
        print(f"{x:>10.2f} | {fx:>15.6f} | {sinal:>10}")

# Função para exibir o gráfico
def exibir_grafico(valores_x):
    x_grafico = valores_x
    y_grafico = [funcao(x) for x in valores_x]

    plt.figure(figsize=(8, 6))
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.plot(x_grafico, y_grafico, label="f(x) = x³ - 5x - 9", color="blue")
    plt.scatter(x_grafico, y_grafico, color="red")
    plt.title("Gráfico de f(x) = x³ - 5x - 9")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

# Solicita ao usuário os valores de x
print("Insira os valores de x separados por espaço (exemplo: -100 -10 -5 -3 -1 0 1 2 3 4 5):")
valores_x = list(map(float, input().split()))

# Cria a tabela
criar_tabela(valores_x)

# Pergunta ao usuário se deseja visualizar o gráfico
mostrar_grafico = input("\nDeseja exibir o gráfico da função? (s/n): ").lower()
if mostrar_grafico == 's':
    exibir_grafico(valores_x)
