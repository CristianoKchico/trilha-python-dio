def recomendar_plano(consumo_mensal):
    """
    Recomenda o plano de internet ideal com base no consumo médio mensal de dados.

    Args:
    consumo_mensal (float): Consumo médio mensal de dados em GB.

    Returns:
    str: Nome do plano recomendado.
    """
    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB."
    elif consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB."
    else:
        return "Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB."

def main():
    try:
        consumo_mensal = float(input("Informe seu consumo médio mensal de dados (em GB): "))
        plano_recomendado = recomendar_plano(consumo_mensal)
        print(plano_recomendado)
    except ValueError:
        print("Por favor, insira um valor numérico válido para o consumo mensal.")

if __name__ == "__main__":
    main()
