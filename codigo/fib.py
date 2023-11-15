def fib(n):
    """
    Calcula la sucesión de Fibonacci y devuelve una lista.
    
    El parámetro n define la longitud de la sucesión a calcular.
    """
    seq = [0,1]
    for i in range(1,n):
        seq.append(seq[i]+seq[i-1])
    return seq