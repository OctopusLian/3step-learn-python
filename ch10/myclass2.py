class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        result = self.weight / (self.height * self.height)
        print(self.name, '的BMI为', result, '。')
        