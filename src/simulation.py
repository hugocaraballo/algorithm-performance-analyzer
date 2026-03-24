import time
from utils import create_vector
from algorithms import bubble_sort, selection_sort, merge_sort

def run_simulation(sizes: list) -> dict:
    """Runs the sorting benchmark for each requested list size.

    For every size, builds a random vector and measures elapsed time for
    selection sort, bubble sort, and merge sort (same input order).

    Args:
        sizes: List lengths to benchmark.

    Returns:
        A dict with keys ``sizes``, ``sele_sort``, ``bubb_sort``, and
        ``merg_sort``. Each algorithm key holds a list of durations in seconds,
        one entry per size in the same order as ``sizes``.
    """
    results = {
        "sizes": sizes,
        "sele_sort": [],
        "bubb_sort": [],
        "merg_sort": [],
    }

    for size in sizes:
        print(f"Benchmarking for {size} elements...")
        base_vec = create_vector(size)

        start_time = time.perf_counter()
        selection_sort(base_vec)
        end_time = time.perf_counter()
        results["sele_sort"].append (end_time - start_time)

        start_time = time.perf_counter()
        bubble_sort(base_vec)
        end_time = time.perf_counter()
        results["bubb_sort"].append (end_time - start_time)

        start_time = time.perf_counter()
        merge_sort(base_vec)
        end_time = time.perf_counter()
        results["merg_sort"].append (end_time - start_time)
    
    return results

if __name__ == "__main__":
    test_sizes = [100, 500, 1000]
    data = run_simulation(test_sizes)
    print("Test finished")
    print(data)
