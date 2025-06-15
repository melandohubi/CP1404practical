"""BEGIN

    SET NUMBER_OF_PICKS TO 6
    SET MINIMUM TO 1
    SET MAXIMUM TO 45

    PROMPT user for number_of_quick_picks
    CONVERT input TO integer

    FOR each_pick FROM 1 TO number_of_quick_picks DO
        INITIALIZE quick_pick AS empty list

        WHILE LENGTH of quick_pick != NUMBER_OF_PICKS DO
            GENERATE random number BETWEEN MINIMUM AND MAXIMUM

            IF number NOT IN quick_pick THEN
                APPEND number TO quick_pick
            END IF
        END WHILE

        SORT quick_pick in ascending order

        FOR EACH number IN quick_pick DO
            PRINT number formatted to width 2
        END FOR
        PRINT newline

    END FOR

END
"""

"""
CP1404/CP5632 Practical
Quick Picks lottery number generator
"""

import random

NUMBER_OF_PICKS = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    number_of_quick_picks = int(input("How many quick picks? "))

    for _ in range(number_of_quick_picks):
        quick_pick = []
        while len(quick_pick) < NUMBER_OF_PICKS:
            number = random.randint(MINIMUM, MAXIMUM)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))

main()
