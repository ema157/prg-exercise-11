import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[minimum]:
                minimum = j
        numbers[i], numbers[minimum] = numbers[minimum], numbers[i]

    return numbers




def bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)
    plt.ion()
    plt.show()
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                index_highlight1 = j
                index_highlight2 = j + 1
                colors = ["steelblue"] * len(numbers)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(numbers)), numbers, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    plt.ioff()
    plt.show()
    return numbers



if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20