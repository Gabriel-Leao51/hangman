from utils import show_difficulty_menu
from utils import get_random_word
from utils import play_hangman

if __name__ == "__main__":
    difficulty_setting = show_difficulty_menu()
    selected_word = get_random_word(difficulty_setting=difficulty_setting)
    player_wins = play_hangman(selected_word, difficulty_setting)

    if player_wins:
        print("Parabéns! Você adivinhou a palavra corretamente.")
    else:
        print("Você perdeu.")

    print(f"A palavra era: {selected_word}")
