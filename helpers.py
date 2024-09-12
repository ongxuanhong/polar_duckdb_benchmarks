import os
import matplotlib.pyplot as plt
import psutil
from memory_profiler import memory_usage


# Helper function to get memory usage
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024**2)  # Convert bytes to MB


# Function to track memory usage and time for each benchmark
def track_memory_and_time(benchmark_func, *args):
    # Measure the memory usage during execution using memory profiler
    mem_usage, results = memory_usage((benchmark_func, args), retval=True)

    # Memory usage peak and elapsed time
    peak_memory = max(mem_usage)
    elapsed_time = results[0]  # Elapsed time is the first element in the results tuple
    result = results[1]  # Actual result of the benchmark function

    return elapsed_time, peak_memory, result


def plot_results(df_output, title1, title2):
    # Plot the benchmark times for comparison
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(
        df_output["Run"], df_output["Polars Time"], label="Polars Time", marker="s"
    )
    plt.plot(
        df_output["Run"], df_output["DuckDB Time"], label="DuckDB Time", marker="^"
    )
    plt.title(title1)
    plt.xlabel("Run")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(
        df_output["Run"],
        df_output["Polars Memory (MB)"],
        label="Polars Memory",
        marker="s",
    )
    plt.plot(
        df_output["Run"],
        df_output["DuckDB Memory (MB)"],
        label="DuckDB Memory",
        marker="^",
    )
    plt.title(title2)
    plt.xlabel("Run")
    plt.ylabel("Memory Usage (MB)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
