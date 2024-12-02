import struct
import matplotlib.pyplot as plt
import numpy as np

def analyze_density(file_path, page_size=4096):
    arr_density = []
    with open(file_path, 'rb') as f:
        data = f.read(8)
        if len(data) < 8:
            raise ValueError("File is too small to contain a uint64_t at the beginning.")
        num_pages = struct.unpack("<Q", data)[0]
        print(f"Number of pages: {num_pages}")

        total_non_zero_bytes = 0
        total_bytes_analyzed = 0

        for _ in range(num_pages):
            page_data = f.read(page_size)
            non_zero_bytes = sum(1 for byte in page_data if byte != 0)
            total_non_zero_bytes += non_zero_bytes
            total_bytes_analyzed += page_size

            density = non_zero_bytes / page_size * 100
            arr_density.append(density)
            print(f"Page {(_+1)}: {density:.2f}% non-zero data.")

        overall_density = total_non_zero_bytes / total_bytes_analyzed * 100
        print(f"Overall data density: {overall_density:.2f}% non-zero data in total.")

    plot_density(arr_density)

def plot_density(data):
    print(data)
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of density percentages')
    plt.xlabel('Density percentage')
    plt.ylabel('Number of pages')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='skyblue', color='black'))
    plt.title('Density percentages')
    plt.xlabel('Density percentage')
    plt.grid(True)
    plt.show()

    page_numbers = list(range(1, 411))
    plt.figure(figsize=(10, 6))
    plt.scatter(page_numbers, data, color='blue', alpha=0.6)
    plt.title('Density percentages across pages')
    plt.xlabel('Page number')
    plt.ylabel('Density percentage')
    plt.grid(True)
    plt.show()

analyze_density('log.bin')
