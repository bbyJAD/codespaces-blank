import random

preguntas = {
    "França": "París",
    "Espanya": "Madrid",
    "Itàlia": "Roma",
    "Regne Unit": "Londres",
    "Alemanya": "Berlín",
    "Portugal": "Lisboa",
    "Suïssa": "Bern",
    "Bèlgica": "Brussel·les",
    "Holanda": "Amsterdam",
    "Austràlia": "Camberra",
    "Canadà": "Ottawa",
    "Mèxic": "Ciutat de Mèxic",
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Colòmbia": "Bogotà",
    "Perú": "Lima",
    "Xile": "Santiago",
    "Veneçuela": "Caracas",
    "Egipte": "El Caire",
    "Marroc": "Rabat",
    "Algèria": "Algiers",
    "Tunísia": "Tunis",
    "Nigèria": "Abuja",
    "Ghana": "Accra",
    "Senegal": "Dakar",
}


pregunta, respuesta = random.choice(list(preguntas.items()))


vidas = 5
letras_adivinadas = []
letras_utilizadas = []


print("Adivina la capital de", pregunta)


while True:
    
    letra = input("Introduce una letra: ").lower()

    
    if letra in letras_utilizadas:
        print(letra, "ya se ha utilizado.")
    elif letra in letras_adivinadas:
        print(letra, "ya se ha adivinado.")
    
    elif letra in respuesta.lower():
        print(letra, "es correcta!")
        letras_adivinadas.append(letra)
    
    else:
        print(letra, "es incorrecta.")
        vidas -= 1
        if vidas == 0:
            print("Te has quedado sin vidas! La capital era", respuesta)
            break

    
    letras_utilizadas.append(letra)
    if set(respuesta.lower()) <= set(letras_adivinadas):
        print("¡Has adivinado la capital de", pregunta, "que era", respuesta, "!")
        break

    
    print("Letras adivinadas:", letras_adivinadas)
    print("Letras utilizadas:", letras_utilizadas)
