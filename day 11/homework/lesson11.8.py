"""ასოების შეფასება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოცდის ქულას. 
შემდეგ დაბეჭდეთ მათი ასოების შეფასება შემდეგი სკალის მიხედვით: 
A (90-100), B (80-89), C (70-79), D (60-69), F (< 60)."""

exam_point=int(input("please enter exam point "))

if exam_point >= 90 and exam_point <= 100:
    print("A")
elif exam_point >= 80 and exam_point <= 89:
    print("B")
elif exam_point >= 70 and exam_point <= 79:
    print("C")
elif exam_point >= 60 and exam_point <= 69:
    print("D")      
elif exam_point < 60:
    print("F")        