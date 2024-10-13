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