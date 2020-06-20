bitcoins = float(input())
yuans = float(input())
comission = float(input())

totalMoney = bitcoins * 1168 / 1.95 + yuans * 0.15 * 1.76 / 1.95
result = totalMoney - totalMoney * comission / 100

print('%.2f' % result)
