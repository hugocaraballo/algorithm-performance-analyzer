from simulation import run_simulation
from visualization import print_results_table, save_results_chart

def main() -> None:
    """Runs the sorting benchmark, prints a results table, and saves a chart.

    Uses predefined test sizes, runs the simulation, prints the ASCII table,
    and writes ``benchmark.png``.
    """
    print ("Starting algorithms Benchmarking...")
    test_sizes = [100, 200, 1000, 2000, 5000]

    results = run_simulation(test_sizes)

    print("\n" + "=" * 42)
    print("    FINAL RESULTS ")
    print("=" * 42)
    print_results_table(results)

    print("\n   Generating image ")
    save_results_chart(results)
    print("   Image saved as 'benchmark.png'")

    
if __name__ == "__main__":
    main()
