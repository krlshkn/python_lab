money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
budget = money_capital + salary
expense = spend

while budget >= expense:
    month += 1
    budget = budget - expense + salary
    expense += expense*increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
