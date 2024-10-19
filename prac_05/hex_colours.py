from operator import itemgetter

# Dictionary of names to scores
name_to_score = {
    'Derek': 7,
    'Xavier': 80,
    'Bob': 612,
    'Chantanelle': 9
}

# Calculate the maximum width for names and scores
name_width = max(len(name) for name in name_to_score.keys())
score_width = max(len(str(score)) for score in name_to_score.values())

# Sort and display the items in the dictionary
for name, score in sorted(name_to_score.items(), key=itemgetter(1), reverse=True):
    print(f"{name:<{name_width}} = {score:{score_width}}")