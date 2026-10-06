def tamano(numero):
    return len(str(abs(numero)))

def multClasica(u, v):
    return u * v

def mult(u, v):
    u_str, v_str = str(u), str(v)
    n = max(len(u_str), len(v_str))
    
    if n <= 1:
        return multClasica(u, v)
    
    # Alineamos los dígitos rellenando con ceros a la izquierda
    u_str, v_str = u_str.zfill(n), v_str.zfill(n)
    
    s = n // 2
    
    # Dividimos exactamente por número de dígitos
    w = int(u_str[:-s])
    x = int(u_str[-s:])
    
    y = int(v_str[:-s])
    z = int(v_str[-s:])
    
    termino1 = mult(w, y) * (10 ** (2 * s))
    termino2 = (mult(w, z) + mult(x, y)) * (10 ** s)
    termino3 = mult(x, z)
    
    return termino1 + termino2 + termino3

if __name__ == "__main__":
    print("--- MULTIPLICACIÓN POR DIVIDE Y VENCERÁS ---")
    
    num_u = int(input("Ingrese el primer número entero (u): "))
    num_v = int(input("Ingrese el segundo número entero (v): "))
    
    resultado_recursivo = mult(num_u, num_v)
    
    print("Resultado obtenido con el algoritmo:", resultado_recursivo)
    print("Verificación del lenguaje (u * v):  ", num_u * num_v)
