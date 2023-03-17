from collections import Counter


class Information:

    def __init__(self, fisier):
        with open(fisier, "r") as file:
            self.data = Counter(file.read().split())
        self._useful_information()

    def _useful_information(self):
        for i in list(self.data.keys()):
            if len(i) <= 3:
                del self.data[i]

    def get_information(self):
        result = []
        most_common_value = self.data.most_common(1)
        for i, j in self.data.items():
            if j == most_common_value[0][1]:
                result.append(i)
        return result


obiect = Information("data.txt")
print(obiect.get_information())
