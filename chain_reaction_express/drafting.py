#offer two random cards after a cleared round and award the player's choice
#Arvint


#card_pool is a list of cards that can be awarded/offered to the players once a round is done
#card_pool = list, insert list once cards are defined, different cards earn different points
#Must create cards before executing code 
#] end of card pool

#card_pool must exist before this code runs


def given_cards(round_number):
    
    """
         (int) ---> (list)
         
         Returns two cards from a list after the given round
         
         >>> get_offer(0)[0]["name"]
        'Exotherm'
        >>> get_offer(1)[0]["name"]
        'Catalyst'
        >>> get_offer(1)[1]["name"]
        'Polymer Chain'
        >>> get_offer(3)[0]["name"]
        'Exotherm'
    """
    
    # Work out the position of the first card, wrapping around the pool with %
    index_a = (round_number * 2) % len(card_pool)
    # The second card is the next position, so it is always different from the first
    index_b = (round_number * 2 + 1) % len(card_pool)
    # Return both cards together in a list
    return [card_pool[index_a], card_pool[index_b]]

#round_number must exist, so a for loop must implement it to define this variable
#lineup is the preexisting cards the user has so they must be defined to run


def offer_draft(lineup, round_number):
    """
    (list, int) --> None

    Offer the player two cards and add their choice to the lineup.
    The chosen card is appended to the lineup list directly.
    (No examples here because this function uses input().)
    """
    # Get the two cards offered this round
    offer = get_offer(round_number)
    # Store the first offered card in its own variable
    card_a = offer[0]
    # Store the second offered card in its own variable
    card_b = offer[1]

    # Tell the player they need to choose
    print("Congrats!!! Round cleared! Choose a card:")
    # Show option 1 with its name and point value
    print("1 -", card_a["name"], card_a["value"], "points")
    # Show option 2 with its name and point value
    print("2 -", card_b["name"], card_b["value"], "points")

    # Ask the player which card they want and store what they typed
    pick = input("Enter 1 or 2: ")

    # Check whether the player chose the first card
    if pick == "1":
        # Add the first card to the end of the lineup
        lineup.append(card_a)
        # Confirm which card was added
        print("You added", card_a["name"], "to your lineup!")
    # Otherwise the player chose the second card
    else:
        # Add the second card to the end of the lineup
        lineup.append(card_b)
        # Confirm which card was added
        print("You added", card_b["name"], "to your lineup!")
