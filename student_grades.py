class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]
        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"

    def find(self, value):
        result =[]
        n = len(self.scores)
        for i in range(n):
            if self.scores[i] == value:
                result.append(i)
        return result

    def get_sorted(self):
        scores = self.scores.copy()
        n = len(scores)
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())
    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")
    print(results.find(100))
    print(results.get_sorted())
    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())




if __name__ == "__main__":
    main()