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

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


print(Art.logo)

game_role = 17
cards = [11, 2, 3, 4, 5, 6, 7, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []

user_total = 0
computer_total = 0


def deal_card():
    return random.choice(cards)


def main():
    print("Computer's first card: ", computer_cards[0])
    print("Your cards: ", user_cards, " Current score: ", user_total)


def check_draw():
    if game_role < computer_total == user_total > game_role:
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


def check_result():
    if game_role < computer_total < user_total > game_role and user_total < 22:
        print("Your final hand: ", user_cards, "Final Score: ", user_total)
        print("Computer's final hand: ", computer_cards, "Final Score: ", computer_total)
        print("You win")
        exit()
    if game_role < user_total < computer_total > game_role and computer_total < 22:
        print("Your final hand: ", user_cards, "Final Score: ", user_total)
        print("Computer's final hand: ", computer_cards, "Final Score: ", computer_total)
        print("You lost")
        exit()

    if user_total > 21:
        print("Your final hand: ", user_cards, "final score: ", user_total)
        print("Computer's final hand: ", computer_cards, "final score: ", computer_total)
        print("You lost")
        exit()


def check_black_jack():
    if computer_total == 21:
        print("You lost with a BlackJack")
        exit()
    if user_total == 21:
        print("You with a BlackJack")
        exit()


user_cards.append(deal_card())
user_cards.append(deal_card())
user_total += user_cards[0] + user_cards[1]

computer_cards.append(deal_card())
computer_cards.append(deal_card())

computer_total += computer_cards[0] + computer_cards[1]

main()
check_black_jack()

user_index = 2
while True:
    user_input = input("Do you want to get another card? y or n: ")
    if user_input == 'y':
        user_cards.append(random.choice(cards))
        user_new_choice = user_cards[user_index]
        user_total += user_new_choice
        user_index += 1
        print("Your new card: ", user_new_choice)
        print("Your total points: ", user_total)
        if 21 < user_total and is_user_has_acs():
            user_total -= 10
        check_draw()
        check_result()

    else:
        if user_total > 21 and is_user_has_acs():
            user_total -= 10

        if user_total < game_role:
            continue
        check_result()
        break

computer_index = 2
while computer_total < 17:
    computer_cards.append(random.choice(cards))
    computer_new_choice = computer_cards[computer_index]
    computer_total += computer_new_choice
    computer_index += 1
    print("Computer's new card: ", computer_new_choice)
    print("Computer total points: ", computer_total)

    if 21 < computer_total and is_comp_has_acs():
        computer_total -= 10
    check_draw()
    check_black_jack()
    check_result()
    if computer_total > 21:
        print("You win")
        break
