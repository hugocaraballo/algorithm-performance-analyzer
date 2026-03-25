from simulation import run_simulation
from visualization import print_results_table, save_results_chart
import sys

def main() -> None:
    """Runs the sorting benchmark, prints a results table, and saves a chart.

    Asks the user for sizes, runs the simulation, prints the ASCII table,
    and writes ``benchmark.png``.
    """
    
    in_data = input("Introduce the size of the arrays (separated with spaces): ")
    sizes = []
    for data in in_data.split():
        try:
            number = int(data)
            if (number <= 0):
                print(f"Error: {number} is not a valid positive number.")
                sys.exit(1)
            sizes.append(number)
    
        except ValueError:
            print(f"Error: {data} is not a valid number.")
            sys.exit(1)
        
    if max(sizes) >= 10000:
        print("Warning: Array sizes over 10,000 might take a long time to " \
              "complete with O(n^2) algorithms like Bubble Sort.")
        decision = input("Do you want to proceed (y/n): ")
        if decision.lower() == "n":
            sys.exit(1)

    print("Starting algorithms Benchmarking...")
    results = run_simulation(sizes)

    print("\n" + "=" * 42)
    print("    FINAL RESULTS ")
    print("=" * 42)
    print_results_table(results)

    print("\n   Generating image ")
    save_results_chart(results)
    print("   Image saved as 'benchmark.png'")

    
if __name__ == "__main__":
    main()
