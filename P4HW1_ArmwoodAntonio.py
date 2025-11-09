# Antonio Armwood
# 11/7/2025
# P4HW1
# Grade Analyzer with Score Validation and Letter Grade

# Pseudocode:
# 1. Start the program.
# 2. Ask the user how many scores they would like to enter.
# 3. Initialize an empty list called student_scores.
# 4. For each score (repeat for the number of scores the user specified):
#    a. Prompt the user to enter a score.
#    b. While the entered score is not valid (not between 0 and 100):
#       i. Display an error message.
#       ii. Prompt the user to re-enter a valid score.
#    c. Once valid, add the score to student_scores list.
# 5. After collecting all scores:
#    a. Find the lowest score in the list.
#    b. Remove the lowest score from the list.
#    c. Calculate the average of the remaining scores.
#    d. Determine the letter grade based on the average:
#       - A: 90–100
#       - B: 80–89
#       - C: 70–79
#       - D: 60–69
#       - F: below 60
# 6. Display:
#    a. The lowest score dropped.
#    b. The list of remaining scores.
#    c. The average of the remaining scores (formatted to 2 decimal places).
#    d. The corresponding letter grade.
# 7. End the program.

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Ask user how many scores they want to enter
    num_scores = int(input("How many scores would you like to enter? "))
    student_scores = []  # Informative name for the score list

    # Loop to collect valid scores
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score #{i + 1} (0–100): "))
                if 0 <= score <= 100:
                    student_scores.append(score)
                    break
                else:
                    print("INVALID Score entered!!!!")
                    print("Score should be between 0 and 100")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Drop the lowest score
    lowest_score = min(student_scores)
    student_scores.remove(lowest_score)

    # Calculate average
    average_score = sum(student_scores) / len(student_scores)
    letter_grade = get_letter_grade(average_score)

    # Display results
    print("\n---------- Results ----------")
    print(f"Lowest score        : {lowest_score}")
    print(f"Modified List       : {student_scores}")
    print(f"Scores Average      : {average_score:.2f}")
    print(f"Grade               : {letter_grade}")
    print("-----------------------------")

if __name__ == "__main__":
    main()
