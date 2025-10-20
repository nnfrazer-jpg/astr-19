import numpy as np

def main():
    # Define the range and number of entries
    start = 0
    end = 2*np.pi
    num_entries = 1000

    # Calculate the step size
    step = (end - start) / (num_entries - 1)

    # Print a header for the table
    print("x \t\t\t| sin(x)")
    print("-" * 23)

    # Loop to generate and print values
    for i in range(num_entries):
        x = start + i * step
        y = np.sin(x)
        print(f"{x:.6f} \t| {y:.6f}")

# Run the main function
if __name__ == "__main__":
    main()