import random  # Importa el módulo random para seleccionar una palabra al azar

def ahorcado():
    # Lista de palabras para el juego
    palabras = ["Java", "Python", "C++", "JavaScript", "PHP", "Ruby"]
    # Selecciona una palabra al azar de la lista y la convierte a mayúsculas
    palabra = random.choice(palabras).upper()
    # Crea una lista con guiones bajos para cada letra de la palabra (espacios permanecen iguales)
    palabraVerificar = ["_" if char != " " else " " for char in palabra]
    # Crea un conjunto para almacenar las letras que ya han sido ingresadas
    letrasIngresadas = set()
    # Número de intentos permitidos
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    # Muestra el estado inicial de la palabra con guiones bajos
    print(" ".join(palabraVerificar))

    # Bucle que continúa hasta que el jugador se quede sin intentos o adivine la palabra
    while intentos > 0 and "_" in palabraVerificar:
        # Solicita al jugador que ingrese una letra
        letraIngresada = input("Ingresa una LETRA: ").upper()

        # Verifica si la letra ya fue ingresada anteriormente
        if letraIngresada in letrasIngresadas:
            print("La letra ya fue ingresada.")
        # Verifica si la letra ingresada está en la palabra
        elif letraIngresada in palabra:
            # Agrega la letra ingresada al conjunto de letras ingresadas
            letrasIngresadas.add(letraIngresada)
            # Actualiza la lista de palabraVerificar con la letra correcta
            for idx, letra in enumerate(palabra):
                if letra == letraIngresada:
                    palabraVerificar[idx] = letraIngresada
            print("¡La letra es correcta!")
        else:
            # Si la letra no está en la palabra, se agrega al conjunto y se reduce el número de intentos
            letrasIngresadas.add(letraIngresada)
            intentos -= 1
            print(f"La letra no está en la palabra. Intentos restantes: {intentos}")

        # Muestra el estado actual de la palabra con las letras adivinadas y los guiones bajos
        print(" ".join(palabraVerificar))

    # Verifica si el jugador adivinó la palabra o se quedó sin intentos
    if "_" not in palabraVerificar:
        print("¡Felicidades! ¡Has adivinado la palabra!")
    else:
        print(f"Has perdido. La palabra era: {palabra}")

# Llama a la función para iniciar el juego
ahorcado()

