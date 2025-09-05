
#compute the average score first
def average_score(scores):
    Average = sum(scores)/len(scores)
    return Average 

#compute the students' grade on the basis average score.
def student_grade(Average):
    if Average >= 80:
        return 'A'
    elif Average >= 60:
        return 'B'
    elif Average >= 50:
        return 'C'
    else:
        return 'F' 

scores = [55, 64, 75, 80, 65]             

Class_Average = average_score(scores)
print(f"Class Average Score : {Class_Average}")

Grade = student_grade(Class_Average)
print(f"Grade of Student : {Grade}")
