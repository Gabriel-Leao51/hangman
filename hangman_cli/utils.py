import re
import random
from constants import DIFFICULTY_LEVELS, WORDS_LENGTHS


def show_difficulty_menu():
    """
    Exibe o menu que permite que o jogador selecione o nível de dificuldade

    :return: uma string que representa o nível de dificuldade selecionado"""

    print("A seguir escolha um nível de dificuldade:")
    difficulty_setting = ""

    while not difficulty_setting:

        for k, v in DIFFICULTY_LEVELS.items():
            print(f"{k} - {v.upper()}")

        difficulty_setting = input("Escolha a dificuldade pelo número associado: ")

        if difficulty_setting not in DIFFICULTY_LEVELS.keys():
            print(f"{difficulty_setting} não é uma opção válida.")
            difficulty_setting = ""

    return difficulty_setting


def get_random_word(difficulty_setting):
    """
    Abre o arquivo que contém o banco de palavras e seleciona uma
    palavra aleatoriamente baseada no parametro difficulty_setting

    :param difficulty_setting: string que representa o nível de dificuldade
    selecionado pelo usuario
    :return: string que representa a palavra aleatoriamente selecionada
    """
    with open("static/words.txt", mode="r") as f_words:
        words = []
        for word in f_words.readlines():
            w = word.strip()
            min, max = WORDS_LENGTHS[difficulty_setting]

            if min <= len(w) <= max:
                words.append(w)

    max_index = len(words) - 1
    random_index = random.randint(0, max_index)
    selected_word = words[random_index]

    return selected_word


def get_total_tries(selected_word, difficulty_setting):
    """
    Define a quantidade de vezes que o jogador pode tentar adivinhar a
    palavra 'selected_word' sem que o jogo chegue ate o final.

    :param selected_word: string que representa a palavra aleatoriamente
    selecionada de dentro do banco de palavras
    :param difficulty_setting: string que define o nivel de dificuldade
    selecionado pelo usuario
    :return: O número de tentativas que o jogador terá para acertar a palavra
    gerada aleatoriamente
    """

    unique_letters = set(selected_word)
    total_tries = 1.5 * len(unique_letters)
    if difficulty_setting == "1":
        total_tries += 2
    elif difficulty_setting == "3":
        total_tries -= 2
        total_tries = min([total_tries, 18])

    total_tries = round(total_tries)
    return(total_tries)

def play_hangman(selected_word, difficulty_setting):
    """
    Simula um jogo da forca com o usuário baseado em uma palavra
    aleatoriamente selecionada e um nível de dificuldade.

    :param selected_word: string que representa a palavra a ser adivinhada
    :param difficulty_setting: string que representa o nível de dificuldade selecionado
    :return: int que se positivo representa vitória do jogador, caso contrario, o jogador perdeu
    """
    total_tries = available_tries = get_total_tries(selected_word=selected_word, difficulty_setting=difficulty_setting)
    current_state = ["_" for letter in selected_word]
    guessed_letters = []

    while "_" in current_state and available_tries:
        print(f"\n\n###Tentativa número {total_tries - available_tries + 1} de {total_tries}###")
        for char in current_state:
            print(char, end="")

        guess = ""
        while not guess:
            guess = input("\nTente uma letra: ").lower()
            if len(guess) != 1 or not re.match("[a-z]", guess):
                print("Entrada inválida. Tente novamente inserindo apenas 1 letra")
                guess = ""

        if guess not in guessed_letters:
            guessed_letters.append(guess)

            if guess in selected_word:
                pass

            positions = [m.start() for m in re.finditer(guess, selected_word)]

            for index in positions:
                current_state[index] = guess

            else:
                available_tries -= 1

        else:
            print(f"{guess} é uma tentativa repetida")
    return available_tries