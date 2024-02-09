def paréntesis_balanceados(cadena):
    pila = []
    for c in cadena:
        # Si es un paréntesis de apertura, lo agregamos a la pila       
        if c== '(':           
            pila.append(c)
        # Si es un paréntesis de cierre         
        elif c == ')': 
            # verificamos si la pila no está vacía
            # si el paréntesis de apertura correspondiente está en la cima de la pila           
            if not pila or pila.pop() != '(':
                return False
    # La cadena está balanceada si la pila está vacía al final
    return not pila

cadena = input("Ingrese la cadena de paréntesis: ")
if paréntesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")


