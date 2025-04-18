student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86,169,50]

max_score = max(student_scores)
for score in student_scores:
    if score == max_score:
        print(f"{score} is the maximum score")