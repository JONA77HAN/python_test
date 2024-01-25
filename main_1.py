import random
import string

def generar_clave():
    caracteres = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y números
    clave_generada = ''.join(random.choice(caracteres) for _ in range(8))
    return clave_generada

# Ejemplo de uso:
clave_aleatoria = generar_clave()
print("Clave generada:", clave_aleatoria)

