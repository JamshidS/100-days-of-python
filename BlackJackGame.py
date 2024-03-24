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


game_role = 17
cards = [11, 2, 3, 4, 5, 6, 7, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []

user_score = 0
computer_score = 0


def deal_card():
    return random.choice(cards)


def main():
    print(f"Computer's first card: {computer_cards[0]}")
    print(f"Your cards: {user_cards}, current score: {user_score}")


def check_draw():
    if game_role < computer_score == user_score > game_role:
        print("No one win the game....")
        exit()


def is_user_has_acs():
    for c in user_cards:
        if c == 11:
            return True
        else:
            return False


def is_comp_has_acs():
    for c in computer_cards:
        if c == 11:
            return True
        else:
            return False


def print_results():
    print(f"Your final hande: {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hande: {computer_cards}, Final Score: {computer_score}")


def check_result():
    if game_role < computer_score < user_score > game_role and user_score < 22:
        print_results()
        print("You win")
        exit()
    if game_role < user_score < computer_score > game_role and computer_score < 22:
        print()
        print("You lost")
        exit()

    if user_score > 21:
        print_results()
        print("You lost")
        exit()


def check_black_jack():
    if computer_score == 21:
        print_results()
        print("You lost with a BlackJack")
        exit()
    if user_score == 21:
        print_results()
        print("You with a BlackJack")
        exit()


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score += user_cards[0] + user_cards[1]
computer_score += computer_cards[0] + computer_cards[1]

main()
check_black_jack()

user_index = 2
computer_index = 2
while True:
    user_input = input("Do you want to get another card? y or n: ")
    if user_input == 'y':
        user_cards.append(deal_card())
        user_new_choice = user_cards[user_index]
        user_score += user_new_choice
        user_index += 1
        print("Your new card: ", user_new_choice)
        print("Your total points: ", user_score)

        if 21 < user_score and is_user_has_acs():
            user_score -= 10
        check_draw()
        check_result()

    if computer_score < game_role:
        computer_cards.append(deal_card())
        computer_new_choice = computer_cards[computer_index]
        computer_score += computer_new_choice
        computer_index += 1
        print("Computer's new card: ", computer_new_choice)
        print("Computer total points: ", computer_score)

        if 21 < computer_score and is_comp_has_acs():
            computer_score -= 10
        check_draw()
        check_black_jack()
        check_result()
        if computer_score > 21:
            print("You win")
            break
    else:
        if user_score > 21 and is_user_has_acs():
            user_score -= 10

        if user_score < game_role:
            continue
        check_result()
        break

print(Art.logo)
