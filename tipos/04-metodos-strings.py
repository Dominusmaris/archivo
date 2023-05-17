import random


def run_game():
    # Genera un número aleatorio entre 1 y 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Pide al jugador que adivine el número
        guess = int(input("Adivina el número secreto entre 1 y 100: "))
        attempts += 1

        # Compara el número adivinado con el número secreto
        if guess == secret_number:
            print("¡Adivinaste el número secreto en", attempts, "intentos!")
            break
        elif guess < secret_number:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")


if __name__ == '__main__':
    run_game()
