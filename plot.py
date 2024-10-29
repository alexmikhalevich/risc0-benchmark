import subprocess
import json
import sys
import matplotlib.pyplot as plt

def cartesi_count_cycles(benchmark_name):
    try:
        command = f"PAYLOAD={benchmark_name} dotenv make cartesi-count-cycles"
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        results = json.loads(result.stdout)
        return results.get("cycles", None)
    except subprocess.CalledProcessError as e:
        print(f"Error executing `make cartesi-count-cycles`: {e}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from output.")
        return None

def execute_benchmark(benchmark_name, step_length):
    try:
        command = f"VERIFY_STEP_LENGTH_CYCLES={step_length} PAYLOAD={benchmark_name} dotenv make"
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing make command: {e}")

def read_results():
    """Reads the results from result.json and prints them."""
    try:
        with open('result.json', 'r') as f:
            results = json.load(f)
        return results
    except FileNotFoundError:
        print("result.json not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from result.json.")

if __name__ == "__main__":
    benchmark_name = sys.argv[1]

    data = []
    cycles = cartesi_count_cycles(benchmark_name)
    max_step = min(10000000, cycles)
    print(f"Total cartesi cycles: {cycles}, capping step length at {max_step} cycles.")
    for step in range(50000, max_step, 50000):
        execute_benchmark(benchmark_name, step)
        data.append(read_results())

    execution_times = [float(d['execution_time'][:-1]) for d in data]
    num_segments = [d['number_of_segments'] for d in data]
    total_cycles = [d['total_cycles'] for d in data]
    user_cycles = [d['user_cycles'] for d in data]
    step_lengths = [d['step'] for d in data]

    print(f"Execution Times: {execution_times}")
    print(f"Number of Segments: {num_segments}")
    print(f"Total Cycles: {total_cycles}")
    print(f"User Cycles: {user_cycles}")

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    plt.suptitle(f"Benchmark: {benchmark_name}")

    axs[0, 0].plot(step_lengths, execution_times, color='blue')
    axs[0, 0].set_title('Execution Time')
    axs[0, 0].set_xlabel('Step Length')
    axs[0, 0].set_ylabel('Execution Time')
    axs[0, 0].grid(axis='y')

    axs[0, 1].plot(step_lengths, num_segments, color='red')
    axs[0, 1].set_title('Number of Segments')
    axs[0, 1].set_xlabel('Step Length')
    axs[0, 1].set_ylabel('Number of Segments')
    axs[0, 1].grid(axis='y')

    axs[1, 0].plot(step_lengths, total_cycles, color='green')
    axs[1, 0].set_title('Total Cycles')
    axs[1, 0].set_xlabel('Step Length')
    axs[1, 0].set_ylabel('Total Cycles')
    axs[1, 0].grid(axis='y')

    axs[1, 1].plot(step_lengths, user_cycles, color='orange')
    axs[1, 1].set_title('User Cycles')
    axs[1, 1].set_xlabel('Step Length')
    axs[1, 1].set_ylabel('User Cycles')
    axs[1, 1].grid(axis='y')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
