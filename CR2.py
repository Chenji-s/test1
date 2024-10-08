def student_pass(score1, score2, score3):
    # Insert your code here
    average = (score1 + score2 + score3) / 3 # Calculate the average score

    passing_count = 0 # Count the number of subjects with scores 40 or above
    if score1 >= 40:
        passing_count += 1
    if score2 >= 40:
        passing_count += 1
    if score3 >= 40:
        passing_count += 1

    # Determine pass or fail based on the count and average
    if passing_count == 3:
        print("This student has passed.")
    elif passing_count >= 2 and average > 50:
        print("This student has passed.")
    else:
        print("This student has not passed.")