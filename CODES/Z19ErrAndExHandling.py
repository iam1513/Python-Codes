# ERROR AND EXCEPTIONS : > Syntax error > ZeroDivisor > TypeError > Name Error 
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide valid numeric inputs.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))
    finally:
        print("Execution completed.")

# Example usage
divide_numbers(10, 0)
