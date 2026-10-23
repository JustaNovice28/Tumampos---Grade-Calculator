def calculate_grade():
    print("--- Student Grade Calculator ---")
    try:
        quizzes = float(input("Enter Quiz Score (0-100): "))
        exams = float(input("Enter Exam Score (0-100): "))
        assignments = float(input("Enter Assignment Score (0-100): "))
        
        # Calculate weighted final grade (30% Quizzes, 50% Exams, 20% Assignments)
        final_score = (quizzes * 0.3) + (exams * 0.5) + (assignments * 0.2)
        
        print(f"\nFinal Score: {final_score:.2f}%")
        
        if final_score >= 90:
            print("Letter Grade: A")
        elif final_score >= 80:
            print("Letter Grade: B")
        elif final_score >= 70:
            print("Letter Grade: C")
        elif final_score >= 60:
            print("Letter Grade: D")
        else:
            print("Letter Grade: F")
            
    except ValueError:
        print("Please enter valid numeric scores.")

if __name__ == "__main__":
    calculate_grade()