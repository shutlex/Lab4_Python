class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            print("Сума п'ятірки елементів:", sum(self.buffer[:5]))
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer



buf = Buffer()


buf.add(1, 2, 3, 4, 5)  # Сума: 15
buf.add(6, 7, 8, 9, 10)  # Сума: 40
buf.add(11, 12, 13)  # Без виведення, очікуємо наступної частини
buf.add(14, 15, 16, 17, 18)  # Сума: 75
buf.add(19, 20)  # Сума: 69
