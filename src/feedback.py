import csv

def feedback(name, rating, comments): #this function will save the feedback that customer gives
    feedback_id = sum(1 for _ in open("data/feedback.csv")) #here it is counting how many lines are there in the file

    with open("data/feedback.csv", "a", newline="") as f: #we add new feedback entry using this
        writer = csv.writer(f)
        writer.writerow([feedback_id, name, rating, comments])

    return "Thank you for your feedback!"
