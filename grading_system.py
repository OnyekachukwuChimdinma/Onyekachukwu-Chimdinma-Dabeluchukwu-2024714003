get_grade(score):
    if 70 <= score <= 100:
        return 'A'
    elif 60 <= score <= 69:
        return 'B'
    elif 50 <= score <= 59:
        return 'C'
    elif 45 <= score <= 49:
        return 'D'
    elif 40 <= score <= 44:
        return 'E'
    elif 0 <= score <= 39:
        return 'F'
    else:
        return 'Invalid score. Please enter a number between 0 and 100.'

def main():
    try:
        score_input = input("Enter the score (0-100): ")
        score = int(score_input)
        grade = get_grade(score)
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
