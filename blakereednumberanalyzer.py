def main():
    try:
        # Open the file
        with open("numbers8.txt", "r") as file:
            # Read all lines and convert them to floats
            numbers = [float(line.strip()) for line in file if line.strip()]

        # Check if file was empty
        if not numbers:
            print("The file is empty.")
            return

        # Calculate statistics
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        largest = max(numbers)
        smallest = min(numbers)

        # Display results
        print(f"Sum: {total:.0f}")
        print(f"Average: {average:.2f}")
        print(f"Number of numbers: {count}")
        print(f"Largest number: {largest}")
        print(f"Smallest number: {smallest}")

    except FileNotFoundError:
        print("Error: The file 'numbers8.txt' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")

# Run the program
main()
