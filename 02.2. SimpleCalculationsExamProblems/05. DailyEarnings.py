workDays = int(input())
moneyPerDay = float(input())
dollarLeva = float(input())

yearsMoney = workDays * moneyPerDay * 12 + workDays * moneyPerDay * 2.5
taxMoney = yearsMoney * 0.25
clearMoney = yearsMoney - taxMoney
clearMoneyPerDay = clearMoney / 365 * dollarLeva

print('%.2f' % clearMoneyPerDay)
