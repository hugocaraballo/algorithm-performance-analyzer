"""Terminal tables and static charts for benchmark results."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Column order and display labels (matches simulation.run_simulation keys).
_ALGO_SPECS = (
    ("sele_sort", "Selection"),
    ("bubb_sort", "Bubble"),
    ("merg_sort", "Merge"),
)


def print_results_table(results: dict) -> None:
    """Prints benchmark results as an aligned ASCII table in the terminal.

    Expects ``results`` to contain ``sizes`` and per-algorithm time lists
    (``sele_sort``, ``bubb_sort``, ``merg_sort``) of equal length. Times are
    shown with four decimal places and an ``s`` suffix.

    Args:
        results: Mapping from benchmark keys to list sizes and timing arrays.
    """
    sizes = results["sizes"]
    headers = ["Size"] + [label for _, label in _ALGO_SPECS]
    rows: list[list[str]] = [headers]

    for i, size in enumerate(sizes):
        row = [str(size)]
        for key, _ in _ALGO_SPECS:
            t = results[key][i]
            row.append(f"{t:.4f} s")
        rows.append(row)

    col_widths = [0] * len(headers)
    for row in rows:
        for c, cell in enumerate(row):
            col_widths[c] = max(col_widths[c], len(cell))

    def _hline() -> str:
        """Builds the ASCII horizontal rule for the table border.

        Returns:
            A string of ``+`` and ``-`` characters spanning all columns.
        """
        return "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    def _print_row(row: list[str], header: bool) -> None:
        """Prints one row with padding derived from ``col_widths``.

        Args:
            row: Cell values for this row.
            header: If True, centers text (header row); otherwise right-aligns.
        """
        parts: list[str] = []
        for c, cell in enumerate(row):
            if header:
                parts.append(f" {cell:^{col_widths[c]}} ")
            else:
                parts.append(f" {cell:>{col_widths[c]}} ")
        print("|" + "|".join(parts) + "|")

    print(_hline())
    _print_row(rows[0], header=True)
    print(_hline())
    for row in rows[1:]:
        _print_row(row, header=False)
    print(_hline())


def save_results_chart(results: dict, filename: str = "benchmark.png") -> None:
    """Saves a line chart comparing algorithm runtimes vs list size.

    Uses a non-interactive matplotlib backend and writes only via
    ``savefig``; no GUI or ``show()`` is invoked.

    Args:
        results: Same structure as :func:`print_results_table`.
        filename: Output path for the PNG figure.
    """
    sizes = results["sizes"]
    fig, ax = plt.subplots(figsize=(10, 6))

    markers = ("o", "s", "^")
    for (key, label), m in zip(_ALGO_SPECS, markers):
        ax.plot(sizes, results[key], marker=m, label=f"{label} sort", linewidth=2)

    ax.set_xlabel("List size")
    ax.set_ylabel("Time (s)")
    ax.set_title("Benchmark: sorting algorithm comparison")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(filename, dpi=150)
    plt.close(fig)
    