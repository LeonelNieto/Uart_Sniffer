def separar_tramas_por_tipo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()

    tokens = contenido.replace('\n', ' ').split()

    tramas_tx = []
    tramas_rx = []

    trama_actual = []
    tipo_actual = None

    for token in tokens:
        if token == 'tx:e5':
            if trama_actual and tipo_actual == 'tx':
                tramas_tx.append(trama_actual)
            elif trama_actual and tipo_actual == 'rx':
                tramas_rx.append(trama_actual)
                print(f"RX: {trama_actual}")
            trama_actual = [token]
            tipo_actual = 'tx'
        elif token == 'rx:e5':
            if trama_actual and tipo_actual == 'tx':
                tramas_tx.append(trama_actual)
                print(f"TX: {trama_actual}")
            elif trama_actual and tipo_actual == 'rx':
                tramas_rx.append(trama_actual)
            trama_actual = [token]
            tipo_actual = 'rx'
        else:
            trama_actual.append(token)


    # Agregar la última trama si existe
    if trama_actual:
        if tipo_actual == 'tx':
            tramas_tx.append(trama_actual)
        elif tipo_actual == 'rx':
            tramas_rx.append(trama_actual)

    return tramas_tx, tramas_rx

# Ejemplo de uso
archivo = 'log_2025_07_08_12_31_05.876840.txt'
tx_tramas, rx_tramas = separar_tramas_por_tipo(archivo)

# print("Tramas TX:")
# for trama in tx_tramas:
#     print(trama)

# print("\nTramas RX:")
# for trama in rx_tramas:
#     print(trama)
