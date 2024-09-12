import os
import matplotlib.pyplot as plt
import psutil

# Helper function to get memory usage
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024**2)  # Convert bytes to MB


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