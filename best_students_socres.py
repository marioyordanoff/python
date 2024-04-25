student_scores = {
    "Ivan": 5.00,
    "Maria": 5.50,
    "Georgy": 5.00,
    "John": 3.50,
    "Emily": 4.00,
    "Michael": 4.50
}

best_students_scores = {}


for name, score in student_scores.items():
    if score > 4.00:
        best_students_scores[name] = score

# Print names and scores from best_students_scores
for name, score in best_students_scores.items():
    print(f"{name} - {score}")