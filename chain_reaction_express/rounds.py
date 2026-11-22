#define round targets, modifiers, clear conditions, and bonus Token thresholds
#Arvint

#Target amount can be changed; the step can as well

# The target for round 0 (each round adds to this)
BASE_TARGET = 3
# How much the target goes up every round
TARGET_STEP = 2
# First bonus margin (M1): score needed is target + M1
BONUS_MARGIN_1 = 3
# Second bonus margin (M2): score needed is target + M2 (must be bigger than M1)
BONUS_MARGIN_2 = 6


def get_target(round_number):
    """
    (int) --> int

    Return the base Target Reaction Score (T) for a round,
    before any modifier is applied.

        >>> get_target(1)
        5
        >>> get_target(2)
        7
        >>> get_target(3)
        9
    """
    # Start from the base and add one step for every round played
    return BASE_TARGET + TARGET_STEP * round_number


def get_modifier(round_number):
    """
    (int) --> dict

    Return the modifier for a round as a dictionary with a
    "name" and a "target_change" (how much it changes the target).
    Even rounds get High Pressure; odd rounds have no modifier.

        >>> get_modifier(1)["name"]
        'None'
        >>> get_modifier(2)["name"]
        'High Pressure'
        >>> get_modifier(2)["target_change"]
        2
    """
    # Check whether the round number is even (remainder 0 when divided by 2)
    if round_number % 2 == 0:
        # Even rounds are harder: the target goes up by 2
        return {"name": "High Pressure", "target_change": 2}
    # Odd rounds have no modifier, so the target does not change
    return {"name": "None", "target_change": 0}


def get_round_info(round_number):
    """
    (int) --> dict

    Return everything the player should see before a round starts:
    the final target, both bonus thresholds, and the modifier name.

        >>> info = get_round_info(2)
        >>> info["target"]
        9
        >>> info["bonus1"]
        12
        >>> info["bonus2"]
        15
        >>> info["modifier"]
        'High Pressure'
    """
    # Get the modifier for this round
    modifier = get_modifier(round_number)
    # Final target = base target plus whatever the modifier changes
    target = get_target(round_number) + modifier["target_change"]
    # Package all the round details into one dictionary
    return {
        "round": round_number,                     # Which round this is
        "target": target,                          # Target Reaction Score (T)
        "bonus1": target + BONUS_MARGIN_1,         # Score needed for first bonus Token
        "bonus2": target + BONUS_MARGIN_2,         # Score needed for second bonus Token
        "modifier": modifier["name"],              # Modifier name to display
    }


def is_cleared(score, target):
    """
    (int, int) --> bool

    Return True if the round is cleared (S >= T), otherwise False.

        >>> is_cleared(5, 5)
        True
        >>> is_cleared(4, 5)
        False
        >>> is_cleared(9, 5)
        True
    """
    # The doc's clear condition: score meets or beats the target
    return score >= target


def get_bonus_tokens(score, target):
    """
    (int, int) --> int

    Return how many bonus Tokens (0, 1, or 2) the score earns.
    There is no base reward for clearing, since the doc leaves it undecided.

        >>> get_bonus_tokens(5, 5)
        0
        >>> get_bonus_tokens(7, 5)
        0
        >>> get_bonus_tokens(8, 5)
        1
        >>> get_bonus_tokens(10, 5)
        1
        >>> get_bonus_tokens(11, 5)
        2
    """
    # Start with no bonus Tokens
    tokens = 0
    # Check whether the score crossed the first threshold (T + M1)
    if score >= target + BONUS_MARGIN_1:
        # Award one bonus Token for crossing the first threshold
        tokens = tokens + 1
    # Check whether the score crossed the second threshold (T + M2)
    if score >= target + BONUS_MARGIN_2:
        # Award a second bonus Token for crossing the second threshold
        tokens = tokens + 1
    # Give back the total bonus Tokens earned
    return tokens


#Add a Game Over? And Stats
