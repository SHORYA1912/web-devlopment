class carcompany:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print(f"Company: {self.company}, Model: {self.model}")

if __name__ == "__main__":
    company = input("Enter car company: ")
    model = input("Enter car model: ")
    car = carcompany(company, model)
    car.display()