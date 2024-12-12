from collections import defaultdict
import subprocess
import os
import matplotlib.pyplot as plt
import sys


ACCESS_LOG = ".access.log"
MACHINE_LOG = "log.bin"


def cartesi_log(steps, payload):
    try:
        command = f"PAYLOAD={payload} VERIFY_STEP_LENGTH_CYCLES={steps} dotenv make cartesi-log"
        subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing `make cartesi-count-cycles`: {e}")


def clean_log():
    try:
        os.remove(ACCESS_LOG)
        os.remove(MACHINE_LOG)
    except Exception as e:
        print(f"Error deleting log file: {e}")


def count_touched_bytes(file_path, mode_1, mode_2=None):
    page_data = defaultdict(set)

    with open(file_path, 'r') as file:
        for line in file:
            take_line = line.startswith(f"[{mode_1}]")
            if mode_2:
                take_line = take_line or line.startswith(f"[{mode_2}]")
            if take_line:
                try:
                    parts = line.split(";")
                    bytes_touched = int(parts[0].split()[1])
                    page_address = parts[0].split("@")[1].strip()
                    offset_raw = parts[1].split("=")[1].strip()
                    offset = int(offset_raw, 16)
                    for i in range(bytes_touched):
                        page_data[page_address].add(offset + i)
                except (IndexError, ValueError):
                    print(f"Skipping invalid line: {line.strip()}")

    result = {page: len(offsets) for page, offsets in page_data.items()}
    print(result)
    return result


def visualize_bar_chart(page_data, mode):
    pages = sorted(page_data.keys())
    bytes_touched = [page_data[page] for page in pages]

    plt.figure(figsize=(12, 6))
    plt.bar(pages, bytes_touched, color="skyblue")
    plt.xlabel("Memory pages")
    plt.ylabel("Bytes touched")
    plt.title(f"Bytes touched per memory page, {mode}")
    plt.xticks([])
    plt.tight_layout()
    plt.show()


def main():
    step_length = int(sys.argv[1])
    payload = sys.argv[2]

    print(f"Calculating step length: {step_length}")
    cartesi_log(step_length, payload)
    data_read = count_touched_bytes(ACCESS_LOG, "read")
    data_write = count_touched_bytes(ACCESS_LOG, "write")
    data_total = count_touched_bytes(ACCESS_LOG, "read", "write")
    clean_log()

    visualize_bar_chart(data_read, "memory reads")
    visualize_bar_chart(data_write, "memory writes")
    visualize_bar_chart(data_total, "memory writes and reads")

    print(f"reads: {data_read}")
    print(f"writes: {data_write}")


if __name__ == "__main__":
    main()
