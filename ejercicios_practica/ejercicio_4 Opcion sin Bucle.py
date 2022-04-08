# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados
# def generar_invitados():
def generar_invitados():
    Invitado_1 = input(str('Introduzca el nombre del primer invitado: '))
    Invitado_2 = input(str('Introduzca el nombre del segundo invitado: '))
    Invitado_3 = input(str('Introduzca el nombre del tercer invitado: '))
    lista_de_invitados = [Invitado_1, Invitado_2, Invitado_3]
    return ('Los invitados son:',lista_de_invitados)

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    invitados = generar_invitados()
    print(invitados)
    
    # Alumno: Crear la función "generar_invitados"

    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar

    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:

    # lista_invitados = generar_invitados()

    # Imprimir en pantalla "lista_invitados":

    print("terminamos")
