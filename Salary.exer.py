BasicSalary = 1500
CommissionRate = 0.02
PriceOfLap = 500
numOfLap = int(input("Number of laptops"))
BonusRate = 200

bonus = (BonusRate * numOfLap)
print(bonus)
commission = (CommissionRate * numOfLap * PriceOfLap)
print(commission)
Gross_salary = (BasicSalary + bonus + commission)
print(Gross_salary)