import math

inputItems = input().split(' ')
sum = 0
numbers = []
operators = []
isFirst = True

for item in inputItems:
    if item == '*' or item == '/' or item == '+' or item == '-':
        for i in range(len(numbers)):
            if item == '*':
                if isFirst:
                    sum += int(numbers[i]) * int(numbers[i + 1])
                    isFirst = False
                else:
                    if len(numbers) == 1:
                        sum *= int(numbers[i])
                    else:
                        sum *= int(numbers[i]) * int(numbers[i + 1])
            elif item == '/':
                if isFirst:
                    sum += int(numbers[i]) / int(numbers[i + 1])
                    isFirst = False
                else:
                    if len(numbers) == 1:
                        sum /= int(numbers[i])
                    else:
                        sum = math.trunc(
                            sum / int(numbers[i]) / int(numbers[i + 1]))
            elif item == '+':
                if isFirst:
                    sum += int(numbers[i]) + int(numbers[i + 1])
                    isFirst = False
                else:
                    if len(numbers) == 1:
                        sum += int(numbers[i])
                    else:
                        sum += int(numbers[i]) + int(numbers[i + 1])
            else:
                if isFirst:
                    sum += int(numbers[i]) - int(numbers[i + 1])
                    isFirst = False
                else:
                    if len(numbers) == 1:
                        sum -= int(numbers[i])
                    else:
                        sum = sum - int(numbers[i]) - int(numbers[i + 1])

            del numbers[0]

            if len(numbers) >= 1:
                del numbers[0]

            if len(numbers) == 0:
                break
    else:
        numbers.append(item)

print(math.trunc(sum))
