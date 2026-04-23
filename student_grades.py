from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        if self.scores[index] >= 90:
            return "A"
        elif self.scores[index] >= 80:
            return "B"
        elif self.scores[index] >= 70:
            return "C"
        elif self.scores[index] >= 60:
            return "D"
        elif self.scores[index] >= 50:
            return "E"
        else:
            return "F"

    def find(self, score):
        seznam_studentu = []
        for index, skore in enumerate(self.scores):
            if skore == score:
                seznam_studentu.append(index)
        return seznam_studentu

    def get_sorted(self):
        scores = self.scores.copy()
        pocet_studentu = len(scores)
        for idx in range(pocet_studentu - 1):
            pocet_zmen = 0
            for index in range(pocet_studentu - 1):
                if scores[index] > scores[index + 1]:
                    scores[index], scores[index + 1] = scores[index + 1], scores[index]
                    pocet_zmen += 1
            if pocet_zmen == 0:
                break  # přidání ošetření případu, že vstup je již seřazen → O(n)
        return scores

    def average_points(self):
        pocet_studentu = 0
        soucet = 0
        for point in self.scores:
            soucet += point
            pocet_studentu += 1
        return soucet / pocet_studentu


if __name__ == "__main__":
    # -------------------------------------------------------------------------
    # zkoušky

    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # print(results.count())          # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    #
    # print(results.get_grade(2))  # A (91 bodů)
    # print(results.get_grade(6))  # A (100 bodů)
    # print(results.get_grade(7))  # F (38 bodů)
    #
    # print(results.find(100))  # [6]
    # print(results.find(50))  # [4]
    # print(results.find(77))  # []
    #
    # print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny


    # -------------------------------------------------------------------------
    # Demonstrování

    print(f"Number of students: {results.count()}")

    for index in range(results.count()):
        print(f"Student {index}: {results.get_by_index(index)} points - {results.get_grade(index)}")

    print(f"Students with 100 points: {len(results.find(100))}")

    print(f"Results sorted by points: {results.get_sorted()}")

    print(f"Average points: {results.average_points():.2f}")

    # -------------------------------------------------------------------------
    # Demonstrování random

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(f"Number of random students: {random_results.count()}")

    for index in range(random_results.count()):
        print(f"Random student {index}: {random_results.get_by_index(index)} points - {random_results.get_grade(index)}")

    print(f"Random students with 100 points: {len(random_results.find(100))}")

    print(f"Results sorted by points: {random_results.get_sorted()}")

    print(f"Average points: {random_results.average_points():.2f}")






