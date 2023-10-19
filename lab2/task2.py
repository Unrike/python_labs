from math import floor

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
for _ in range(months):
    money_capital = money_capital - salary + spend
    spend *= (1 + increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", floor(money_capital))
