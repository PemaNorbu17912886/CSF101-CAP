################################
# Your Name: Pema Norbu
# Your Section: 1 Electrical Engineering
# Your Student ID Number: 02230069
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# Put your number here
################################

def file():
    with open('input_9_cap1.txt', 'r') as a:
        print(a.read())

def calculate_score():
    scores = {
        "A Y":4,       # Draw
        "A X":3,      # Rock loses
        "A Z":8,      # Rock wins
        "B Z":9,       # Paper wins
        "B Y":5,       # Draw
        "B X":1,      # Paper loses
        "C X":2,      # Scissors lose
        "C Z":7,      # Scissors win
        "C Y":6       # Draw
    }

    with open('input_9_cap1.txt', 'r') as a:
        content = a.read().splitlines()

    total_score = sum(scores.get(char, 0) for char in content)
    print("Total score is", total_score)

calculate_score()