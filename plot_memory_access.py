import subprocess
import os
import matplotlib.pyplot as plt
import sys
from collections import Counter


ACCESS_LOG = ".access.log"
MACHINE_LOG = "log.bin"
DATA_LABELS = {
    "touch_page",
    "read shadow",
    "write shadow",
    "read pma",
    "read memory",
    "write memory",
    "translate vaddr",
    "replace tlb",
    "flush tlb"
}


def read_memory_access(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    filtered_lines = [line for line in lines if line.strip() in DATA_LABELS]
    return Counter(line.strip() for line in filtered_lines)


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


if __name__ == "__main__":
    max_step_length = int(sys.argv[1])
    payload = sys.argv[2]
    data = []
    for step_length in range(50000, max_step_length, 10000):
        print(f"Calculating step length: {step_length}")
        cartesi_log(step_length, payload)
        access_data = read_memory_access(ACCESS_LOG)
        data.append((step_length, access_data))
        clean_log()
    print(data)


    touch_page = [access_data["touch_page"] for _, access_data in data]

    read_shadow = [access_data["read shadow"] for _, access_data in data]
    write_shadow = [access_data["write shadow"] for _, access_data in data]
    read_memory = [access_data["read memory"] for _, access_data in data]
    write_memory = [access_data["write memory"] for _, access_data in data]

    translate_vaddr = [access_data["translate vaddr"] for _, access_data in data]
    replace_tlb = [access_data["replace tlb"] for _, access_data in data]
    flush_tlb = [access_data["flush tlb"] for _, access_data in data]
    read_pma = [access_data["read pma"] for _, access_data in data]

    step_lengths = [step_length for step_length, _ in data]

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    plt.suptitle(f"Benchmark: {payload}")
    axs[0, 0].plot(step_lengths, read_shadow, color='blue')
    axs[0, 0].set_title('Shadow page reads')
    axs[0, 0].set_xlabel('Step Length')
    axs[0, 0].set_ylabel('Shadow page reads')
    axs[0, 0].grid(axis='y')

    axs[0, 1].plot(step_lengths, write_shadow, color='red')
    axs[0, 1].set_title('Shadow page writes')
    axs[0, 1].set_xlabel('Step Length')
    axs[0, 1].set_ylabel('Shadow page writes')
    axs[0, 1].grid(axis='y')

    axs[1, 0].plot(step_lengths, read_memory, color='green')
    axs[1, 0].set_title('Memory page reads')
    axs[1, 0].set_xlabel('Step Length')
    axs[1, 0].set_ylabel('Memory page reads')
    axs[1, 0].grid(axis='y')

    axs[1, 1].plot(step_lengths, write_memory, color='orange')
    axs[1, 1].set_title('Memory page writes')
    axs[1, 1].set_xlabel('Step Length')
    axs[1, 1].set_ylabel('Memory page writes')
    axs[1, 1].grid(axis='y')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    plt.suptitle(f"Benchmark: {payload}")
    axs[0, 0].plot(step_lengths, translate_vaddr, color='blue')
    axs[0, 0].set_title('Vaddr translation')
    axs[0, 0].set_xlabel('Step Length')
    axs[0, 0].set_ylabel('Vaddr translations')
    axs[0, 0].grid(axis='y')

    axs[0, 1].plot(step_lengths, replace_tlb, color='red')
    axs[0, 1].set_title('TLB replacements')
    axs[0, 1].set_xlabel('Step Length')
    axs[0, 1].set_ylabel('TLB replacements')
    axs[0, 1].grid(axis='y')

    axs[1, 0].plot(step_lengths, flush_tlb, color='green')
    axs[1, 0].set_title('TLB flushes')
    axs[1, 0].set_xlabel('Step Length')
    axs[1, 0].set_ylabel('TLB flushes')
    axs[1, 0].grid(axis='y')

    axs[1, 1].plot(step_lengths, write_memory, color='orange')
    axs[1, 1].set_title('PMA reads')
    axs[1, 1].set_xlabel('Step Length')
    axs[1, 1].set_ylabel('PMA reads')
    axs[1, 1].grid(axis='y')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    fig = plt.figure()
    plt.figure(figsize=(8, 6))
    plt.plot(step_lengths, touch_page, linestyle="-")
    plt.xlabel("Step length")
    plt.ylabel("Page touches")
    plt.title("Page touches for different step lengths")
    plt.suptitle(f"Payload: {payload}")
    plt.grid(True)
    plt.show()
