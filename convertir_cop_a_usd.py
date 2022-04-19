def convertir_cop_a_usd(valor_ingresado):

    valor_ingresado = float(valor_ingresado)

    valor_dolares = 3759
    valor_total_usd = valor_ingresado / valor_dolares
    valor_total_usd = round(valor_total_usd, 2)

    print(f"Tienes ${ valor_total_usd } dolares ")
