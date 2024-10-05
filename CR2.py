def student_pass(score1, score2, score3):
    # Insert your code here
# Calculate the average of three scores
    average = (score1 + score2 + score3) / 3

# First passing condition: all three scores are 40 or above
    if score1 >= 40 and score2 >= 40 and score3 >= 40:
        print("This student has passed.")
    
# Second passing condition: at least two scores are 40 or above, and average is greater than 50
    elif(score1 >= 40 and score2 >= 40 or score2 >= 40 and score3 >= 40 or score1 >= 40 and score3 >= 40) and average > 50:
        print("This student has passed.")
    
# If none of the passing conditions are met, the student has not passed
    else:
        print("This student has not passed.")