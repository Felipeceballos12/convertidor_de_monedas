def convertir_usd_a_cop(valor_ingresado):

    valor_ingresado = float(valor_ingresado)

    valor_peso_colombiano = 0.0005
    valor_total_cop = valor_ingresado / valor_peso_colombiano
    valor_total_cop = round(valor_total_cop, 2)

    print(f"Tienes ${ valor_total_cop } pesos colombianos ")
