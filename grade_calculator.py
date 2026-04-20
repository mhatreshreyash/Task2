# Function to determine grade and message
def get_grade(marks):
    if marks >= 90:
        return "A", "🌟 Excellent work! Keep shining!"
    elif marks >= 75:
        return "B", "👏 Great job! You're doing really well!"
    elif marks >= 60:
        return "C", "👍 Good effort! Keep improving!"
    elif marks >= 50:
        return "D", "🙂 You passed! Try to do even better next time!"
    else:
        return "F", "💪 Don't give up! Work harder and you'll improve!"

# Main program
def main():
    name = input("Enter student name: ")

    # Input validation using while loop
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            
            if 0 <= marks <= 100:
                break
            else:
                print("❌ Invalid input! Marks must be between 0 and 100.")
        
        except ValueError:
            print("❌ Please enter a valid number!")

    # Get grade and message
    grade, message = get_grade(marks)

    # Display result
    print("\n🎓 Result")
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("Message:", message)

# Run the program
main()
