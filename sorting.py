import random
import matplotlib.pyplot as plt



def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



# ----------------------------------------------------------------------------------------------
# Moje definované funkce

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
        pocet_zmen = 0
        for index in range(pocet_cisel - 1):
            index_highlight1 = index
            index_highlight2 = index + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                pocet_zmen += 1
        if pocet_zmen == 0:
            break                   # přidání ošetření případu, že vstup je již seřazen → O(n)

    plt.ioff()
    plt.show()
    return numbers



# ---------------------------------------------------------------------------
# Zkoušky výstupů

# list.sort() - seřadí původní seznam, nic nevrací
my_list_sort = [3, 8, 1, 2, 32]
my_list_sort.sort()
# print(my_list_sort)   # [1, 2, 3, 8, 32]


# sorted(list) - vytvoří se nový seznam, který je třeba předepsat,
# v něm bude seřazen obsah původního seznamu
my_list_sort_sorted = [3, 8, 1, 2, 32]
new_list = sorted(my_list_sort_sorted)
# print(my_list_sort_sorted)   # [3, 8, 1, 2, 32]   ← beze změny
# print(new_list)  # [1, 2, 3, 8, 32]


# argument reverse=True - seřadí sestupně
my_list_reverse = [3, 8, 1, 2, 32]
my_list = sorted(my_list_reverse, reverse=True)
# print(my_list)   # [32, 8, 3, 2, 1]


# argument key=... - nastavuje klíč, podle kterého řadíme
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words_sorted = sorted(list_of_words, key=len)
# print(list_of_words_sorted)   # ['MOO', 'woof', 'meeeoow', 'BZZZZZZ']
list_of_words_lower = sorted(list_of_words, key=str.lower)
# print(list_of_words_lower)      # ['BZZZZZZ', 'meeeoow', 'MOO', 'woof']



# -----------------------------------------------------------------------------------------------
# OOP


# přes tečkovou notaci se dostaneme ke specifickým METODÁM

# text = "acgt"
# text.upper()          # metoda upper() na objektu třídy str — vrátí "ACGT"
# numbers = [1, 2, 3]
# numbers.append(4)     # metoda append() na objektu třídy list — rozšíří seznam na [1, 2, 3, 4]


class Rectangle:            # Pascal case - začínáme velkým písmenem
    def __init__(self, width, height):      # def → METODY
        self.width = width                  # self.width přístup k datům - atributům třídy, na konci nejsou závorky
        self.height = height                # atributy šířka, délka třídy Rectangle (obdélník)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter


r1 = Rectangle(3, 5)                # vytvářím proměnnou, ve které bude objekt třídy Rectangle, bude obsahovat 2 parametry
r2 = Rectangle(10, 20)
r3 = Rectangle(1, 1)

print(r1.area())              # 15                  # k metodám přistupuju přes tečky
print(r2.perimeter())         # 60
print(r3.fencing_cost(250))   # 1000


# ------------------------------------------------------------------------------------------------
# funkce main

if __name__ == "__main__":

    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    # print("Výsledky Selection Sort:")
    # print(selection_sort([5, 1, 4, 2, 8, 100, 1, -2, 0]))
    selection = selection_sort(values)
    # print(selection)

    # print("Výsledky Bubble Sort:")
    # print(bubble_sort([5, 1, 4, 2, 8, 100, 1, -2, 0]))
    bubble = bubble_sort(values)
    # print(bubble)

    # print(f"Výstupy jsou stejné: {selection == bubble}")





