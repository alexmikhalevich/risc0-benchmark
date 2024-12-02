import struct
import subprocess
import os
import matplotlib.pyplot as plt
import sys

LOG_FILE = "log.bin"

def read_page_count(file_path):
    with open(file_path, "rb") as file:
        data = file.read(8)
        if len(data) < 8:
            raise ValueError("File is too small to contain a uint64_t at the beginning.")

        uint64_value = struct.unpack("<Q", data)[0]
        return uint64_value


def cartesi_log(steps, payload):
    try:
        command = f"PAYLOAD={payload} VERIFY_STEP_LENGTH_CYCLES={steps} dotenv make cartesi-log"
        subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing `make cartesi-count-cycles`: {e}")


def clean_log(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting log file: {e}")


if __name__ == "__main__":
    max_step_length = int(sys.argv[1])
    payload = "archive"
    data = []
    for step_length in range(50000, max_step_length, 10000):
        print(f"Calculating step length: {step_length}")
        cartesi_log(step_length, payload)
        page_count = read_page_count(LOG_FILE)
        data.append((step_length, page_count))
        clean_log(LOG_FILE)
    print(data)

    fig = plt.figure()
    x_values, y_values = zip(*data)
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, linestyle="-")
    plt.xlabel("Step length")
    plt.ylabel("Page count")
    plt.title("Amount of pages used by the Cartesi Machine for different step lengths")
    plt.suptitle(f"Payload: {payload}")
    plt.grid(True)
    plt.show()
