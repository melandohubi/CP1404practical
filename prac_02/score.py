"""FUNCTION get_result(score)
    IF score >= 90 THEN
        RETURN "A"
    ELSE IF score >= 80 THEN
        RETURN "B"
    ELSE IF score >= 70 THEN
        RETURN "C"
    ELSE IF score >= 60 THEN
        RETURN "D"
    ELSE
        RETURN "F"
    END IF
END FUNCTION


FUNCTION main()
    DISPLAY "Enter your score: "
    READ input_score
    CONVERT input_score TO FLOAT → score

    result ← CALL get_result(score)
    DISPLAY "Your grade is: " + result

    random_score ← GENERATE RANDOM FLOAT BETWEEN 0 AND 100
    random_result ← CALL get_result(random_score)
    DISPLAY "Random score: " + FORMAT random_score TO 2 DECIMAL PLACES + ", Grade: " + random_result
END FUNCTION


IF program is being run directly THEN
    CALL main()
END IF
"""


import random

def get_result(score):
    """Determines the result based on the user's score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():

    score = float(input("Enter your score: "))
    result = get_result(score)
    print(f"Your grade is: {result}")

    random_score = random.uniform(0, 100)
    random_result = get_result(random_score)
    print(f"Random score: {random_score:.2f}, Grade: {random_result}")

if __name__ == "__main__":
    main()
