# calculator.py
import sys

def print_header(title):
    """Prints a styled CLI header box."""
    width = 46
    print("\n" + "=" * width)
    print(f"║ {title.center(width - 4)} ║")
    print("=" * width)

def get_valid_score(prompt):
    """Repeatedly prompts user for a valid score between 0 and 100."""
    while True:
        try:
            score_str = input(f"  ▸ {prompt}: ").strip()
            if not score_str:
                print("    ❌ Input cannot be empty. Please enter a number.")
                continue
            
            score = float(score_str)
            if 0 <= score <= 100:
                return score
            else:
                print("    ❌ Invalid range! Score must be between 0 and 100.")
        except ValueError:
            print("    ❌ Invalid format! Please enter a numeric value.")

def calculate_grade():
    print_header("STUDENT GRADE CALCULATOR")
    
    print("\n[ Step 1: Input Academic Scores ]")
    quizzes = get_valid_score("Enter Quiz Average (0-100)")
    exams = get_valid_score("Enter Exam Average (0-100)")
    assignments = get_valid_score("Enter Assignment Average (0-100)")
    
    # Calculate weighted final grade (30% Quizzes, 50% Exams, 20% Assignments)
    final_score = (quizzes * 0.3) + (exams * 0.5) + (assignments * 0.2)
    
    # Determine Letter Grade and clean UI color placeholders
    if final_score >= 90:
        letter = "A"
        remark = "Excellent Work! 🌟"
    elif final_score >= 80:
        letter = "B"
        remark = "Very Good Job! 👍"
    elif final_score >= 70:
        letter = "C"
        remark = "Good Effort. Keep growing! 📈"
    elif final_score >= 60:
        letter = "D"
        remark = "Passed, but needs improvement. ⚠️"
    else:
        letter = "F"
        remark = "Failed. Please seek assistance. 🛑"
        
    print_header("FINAL EVALUATION REPORT")
    print(f"  📊 Final Weighted Score : {final_score:.2f}%")
    print(f"  🎓 Earned Letter Grade  : Grade {letter}")
    print(f"  📝 Instructor Remarks   : {remark}")
    print("=" * 46 + "\n")

if __name__ == "__main__":
    try:
        calculate_grade()
    except KeyboardInterrupt:
        print("\n\n🛑 Process terminated by user. Goodbye!")
        sys.exit(0)
