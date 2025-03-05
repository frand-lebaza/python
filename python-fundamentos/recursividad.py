#  la recursividad es un concepto en programación en el que una función se llama a sí misma directa o indirectamente.
#  La recursividad es un enfoque poderoso para resolver problemas que se pueden dividir en problemas más pequeños del mismo tipo.
#  La recursividad se puede utilizar para resolver problemas de manera más elegante y concisa.
#  La recursividad es un concepto importante en programación funcional.
#  La recursividad se puede utilizar para reemplazar bucles en algunos casos.

def factorial(n):
    print(f"llamando a factorial({n})")
    if n == 0:
        print(f"factorial({n}) = 1")
        return 1
    else:
        resultado =  n * factorial(n-1)
        print(f"factorial({n}) = {resultado}")
        return resultado
    
print(factorial(5)) # 120