# Algorithm Performance Analyzer

A modular Python benchmarking tool designed to analyze, compare, and visualize the time complexity and performance of classic sorting algorithms. 

This project demonstrates software architecture principles (like Separation of Concerns) by dividing data generation, algorithm logic, execution timing, and data visualization into independent modules.

## Features
* **Interactive CLI:** Prompts the user to dynamically input custom array sizes with robust error handling and execution warnings for massively large inputs.
* **Accurate Benchmarking:** Uses Python's high-resolution `time.perf_counter()` to measure execution time.
* **Multiple Algorithms:** Currently compares $O(n^2)$ algorithms (Bubble Sort, Selection Sort) against $O(n \log n)$ algorithms (Merge Sort).
* **Terminal UI:** Outputs a clean, formatted ASCII table with the results.
* **Data Visualization:** Automatically generates and saves a line chart comparing the performance curves of each algorithm.

## Project Architecture
The code is structured into highly cohesive, single-responsibility modules:
* `main.py`: The entry point and orchestrator of the application (handles the interactive CLI).
* `utils.py`: Handles the generation of randomized data arrays.
* `algorithms.py`: Contains the pure implementations of the sorting algorithms.
* `simulation.py`: The core engine that clones arrays and records execution times.
* `visualization.py`: Responsible for formatting terminal output and generating Matplotlib charts.

## Quick Start

### Prerequisites
Make sure you have Python 3 installed. You will also need the `matplotlib` library for generating the charts. You can install the required dependencies using:

```
pip install -r requirements.txt
```

## Running the Benchmark
Simply run the main script from your terminal:

```
python src/main.py
```
*(Note: Depending on your system, you might need to use* ```python3 src/main.py```*)*

The program will prompt you to enter the array sizes you want to test. For example:
```
Introduce the size of the arrays (separated with spaces): 100 200 300
```

## Stack & Tools
* Language: Python 3

* Libraries: matplotlib (for data visualization), time, random, sys.

**Development Approach (AI-Assisted):** This project was developed using **Cursor AI** as a pair-programming assistant. AI was leveraged to accelerate the implementation of standard sorting algorithms and handle the tedious syntax of terminal formatting and Matplotlib charts. This allowed me to focus my efforts on the core software architecture, data flow, CLI logic and the benchmarking engine.