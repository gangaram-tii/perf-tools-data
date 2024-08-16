def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file]
        
        if not numbers:
            raise ValueError("The file is empty or contains no valid numbers.")
        
        average = sum(numbers) / len(numbers)
        return average
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        average = calculate_average(filename)
        if average is not None:
            print(f"The average is: {average}")

