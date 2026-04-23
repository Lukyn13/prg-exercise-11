import random
import matplotlib.pyplot as plt



def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



def selection_sort(numbers):
    numbers = numbers.copy()            # udělám kopii vstupu, abych ho nezměnil
    for krok in range(len(numbers)):
        aktualni_min_index = krok
        for index in range(krok+1,len(numbers)):    # beru od následujícího čísla dál, abych neprocházel již seřazené
            if numbers[index] < numbers[aktualni_min_index]:
                aktualni_min_index = index
        numbers[krok], numbers[aktualni_min_index] = numbers[aktualni_min_index], numbers[krok] #prohození

    return numbers



def bubble_sort(numbers):
    numbers = numbers.copy()
    pocet_cisel = len(numbers)
    plt.ion()
    plt.show()
    for idx in range(pocet_cisel - 1):
        for index in range(pocet_cisel - 1):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                index_highlight1 = index
                index_highlight2 = index + 1
                colors = ["steelblue"] * len(values)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(values)), values, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)
    plt.ioff()
    plt.show()
    return numbers






if __name__ == "__main__":

    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    # print("Výsledky Selection Sort:")
    # print(selection_sort([5, 1, 4, 2, 8, 100, 1, -2, 0]))
    # print(selection_sort(values))

    print("Výsledky Bubble Sort:")
    # print(bubble_sort([5, 1, 4, 2, 8, 100, 1, -2, 0]))
    print(bubble_sort(values))





