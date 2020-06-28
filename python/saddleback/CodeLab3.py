# =========
# CodeLab 3
# =========

def letter_grade(test_score):
    if test_score >= 90 and test_score <= 100:
        return "A"
    elif test_score >= 80 and test_score <= 89:
        return "B"
    elif test_score >= 70 and test_score <= 79:
        return "C"
    elif test_score >= 60 and test_score <= 69:
        return "D"
    elif test_score >= 0 and test_score <= 59:
        return "F"
    else:
        return "Error"

def calculate_average_grade(test1, test2, test3, test4, test5):
    return (test1 + test2 + test3 + test4 + test5) / 5

def main():
    student_name = input("Enter student name: ")

    total_score = 0
    num_tests = 5
    
    for i in range(num_tests):
        test_score = float(input("Enter test score " + str(i+1) + ": "))
        total_score += test_score

        grade = letter_grade(test_score)

        print("\ntest " + str(i+1) + ": score: " + str(test_score) + ", grade: " + grade)
    
    average_score = total_score / num_tests

    print("\nStudent name: " + student_name + ", average test score: " + str(average_score))

main()




                         
                         
