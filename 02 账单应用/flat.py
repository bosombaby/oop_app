# 账单
class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


# 室友
class Flatmate:
    def __init__(self, name, day_in_house):
        self.name = name
        self.day_in_house = day_in_house

    def pays(self, bill, other_flatmate):
        weight = self.day_in_house / (self.day_in_house + other_flatmate.day_in_house)
        pay_bill = round(bill.amount * weight, 2)
        return pay_bill