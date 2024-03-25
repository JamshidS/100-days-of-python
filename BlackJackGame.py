############### Blackjack Project #####################
import random

import Art

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

print(Art.logo)

game_role = 17
cards = [11, 2, 3, 4, 5, 6, 7, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []

user_score = 0
computer_score = 0
user_index = 2
computer_index = 2


def reset_game():
    global user_cards, computer_cards, user_score, computer_score, user_index, computer_index
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    user_index = 2
    computer_index = 2


def deal_card():
    return random.choice(cards)


def main():
    print(f"Computer's first card: {computer_cards[0]}")
    print(f"Your cards: {user_cards}, current score: {user_score}")


def check_draw():
    if game_role < computer_score == user_score > game_role:
        print("No one win the game....")
        return


def has_ace(cards):
    return 11 in cards


def print_results():
    print(f"Your final hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Final Score: {computer_score}")


def check_result():
    if game_role < computer_score < user_score > game_role and user_score < 22:
        print_results()
        print("You win")
        return
    if user_score < computer_score > game_role and computer_score < 22:
        print_results()
        print("You lost")
        return

    if user_score > 21:
        print_results()
        print("You lost")
        return

    if computer_score > 21:
        print_results()
        print("You win")
        return


def check_blackjack():
    if computer_score == 21:
        print_results()
        print("You lost with a Blackjack")
        return
    if user_score == 21:
        print_results()
        print("You won with a Blackjack")
        return


def draw_card_and_update_score(cards, score, index):
    cards.append(deal_card())
    new_card = cards[index]
    score += new_card
    index += 1
    return score, index


def play_game():
    global user_score, user_index, computer_score, computer_index
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    main()
    check_blackjack()

    while True:
        user_input = input("Do you want to get another card? y or n: ")
        if user_input == 'y':
            user_score, user_index = draw_card_and_update_score(user_cards, user_score, user_index)
            if user_score > 21 and has_ace(user_cards):
                user_score -= 10
            check_draw()
            check_blackjack()
            check_result()
        else:
            check_result()
            check_draw()
            check_blackjack()
            if user_score < game_role and computer_score > user_score:
                print_results()
                print("You lost the game")
                return
            break

    while computer_score < 17:
        computer_score, computer_index = draw_card_and_update_score(computer_cards, computer_score, computer_index)
        if computer_score > 21 and has_ace(computer_cards):
            computer_score -= 10

        check_draw()
        check_blackjack()
        check_result()

    check_result()
    check_draw()
    check_blackjack()


while True:
    reset_game()
    play_game()
    play_again = input("Do you want to play again? y or no: ")
    if play_again != 'y':
        break
